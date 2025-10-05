import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title='Ibraheem Project',
    page_icon='🌐🧠',
    layout='wide'
)

@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/Steven-Alvarado/Global-Temperature-Analysis/refs/heads/main/GlobalTemperatures.csv'
    df = pd.read_csv(url)
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    df.dropna(subset=['LandAverageTemperature'], inplace=True)
    df = df.rename(columns={'dt':'Date' , 'LandAverageTemperature':'AVG_Temperature'})
    return df

df = load_data()

st.title("Ibraheem Project")
st.markdown('Explore how average land temperatures have changed over time')

st.sidebar.header("Select Range")

year_range = st.sidebar.slider(
    "Select year range",
    int(df['Year'].min()),
    int(df['Year'].max()),
    (1900, 2015)
)

filtered_df = df[
    (df['Year'] >= year_range[0]) &
    (df['Year'] <= year_range[1])
]

st.write(f'## Temperature trend from {year_range[0]} to {year_range[1]}')

yearly_temp = filtered_df.groupby('Year')['AVG_Temperature'].mean().reset_index()

st.write("## Average Temperature trend")
fig_line = px.line(
    yearly_temp,
    x='Year',
    y='AVG_Temperature',
    title='Global Average land temp over time',
    labels={'Year':'Year', 'AVG_Temperature':'AVG Temperature (°C)'}
)

fig_line.update_traces(mode='lines+markers')
fig_line.add_scatter(
    x=yearly_temp['Year'],
    y=yearly_temp['AVG_Temperature'].rolling(window=10).mean(),
    mode='lines',
    name='10-Year Moving AVG'
)
st.plotly_chart(fig_line, use_container_width=True)

st.write('### Raw Data')
with st.expander("Show filtered data"):
    st.dataframe(filtered_df)
