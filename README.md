# README.md

## Project Overview

This is a Streamlit-based data visualization dashboard called "Ibraheem Project" that displays global temperature trends over time. The application fetches temperature data from an external CSV source and provides interactive visualizations with filtering capabilities.

## Architecture

### Core Components

- **`app.py`**: Main Streamlit application containing the dashboard logic, data processing, and visualization components
- **`run_app.py`**: Application launcher that starts Streamlit with ngrok tunneling for public access
- **`.env`**: Environment configuration containing ngrok authentication token

### Key Architecture Patterns

1. **Data Pipeline**: Uses `@st.cache_data` decorator for efficient data loading and caching of remote CSV data
2. **Interactive Filtering**: Year range slider in sidebar filters the dataset dynamically
3. **Public Access**: Integration with ngrok for creating public URLs to the locally running Streamlit app
4. **Visualization Layer**: Uses Plotly Express for interactive charts with moving averages

## Development Commands

### Running the Application

```powershell
# Standard local development (runs on localhost:8501)
python3.11 -m streamlit run app.py

# Run with public access via ngrok (requires NGROK_AUTHTOKEN in .env)
python3.11 run_app.py
```

### Installing Dependencies

```powershell
# Core dependencies required
python3.11 -m pip install streamlit pandas plotly pyngrok python-dotenv
```

### Environment Setup

Ensure `.env` file contains:
```
NGROK_AUTHTOKEN=your_token_here
```

### Development Server Options

```powershell
# Run on specific port
python3.11 -m streamlit run app.py --server.port 8502

# Run with specific host
python3.11 -m streamlit run app.py --server.address 0.0.0.0
```

## Data Source

The application loads temperature data from:
- URL: `https://raw.githubusercontent.com/Steven-Alvarado/Global-Temperature-Analysis/refs/heads/main/GlobalTemperatures.csv`
- Data Processing: Converts date strings to datetime, extracts year column, filters null values, renames columns for clarity

## Key Features

- **Interactive Year Range Selection**: Sidebar slider allows filtering data by year range (default: 1900-2015)
- **Temperature Trend Visualization**: Line chart with markers showing yearly average temperatures
- **Moving Average Overlay**: 10-year rolling average displayed as additional line
- **Raw Data Explorer**: Expandable section showing filtered dataset
- **Responsive Design**: Wide layout configuration for better data visualization

## Environment Notes

- Python executable: `python3.11` (available via Chocolatey installation)
- Shell: PowerShell 5.1 on Windows
- Default Streamlit port: 8501
- Uses ngrok for public URL generation when running via `run_app.py`

## File Dependencies

- **External Data**: Relies on GitHub-hosted CSV file for temperature data
- **Environment Variables**: Requires ngrok token for public access functionality
- **Git Ignored**: `.env` file is excluded from version control for security

## Troubleshooting

- If ngrok fails, verify `NGROK_AUTHTOKEN` is properly set in `.env`
- For data loading issues, check internet connectivity and external CSV URL availability
- Python installation issues may require checking Chocolatey-installed Python path
