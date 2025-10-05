import os
import subprocess
import time
from pyngrok import ngrok
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("NGROK_AUTHTOKEN")

if not token:
    print("Please add NGROK_AUTHTOKEN to your .env file.")
    exit(1)

ngrok.set_auth_token(token)

try:
    ngrok.kill()

    print("🚀 Starting Streamlit...")
    streamlit_process = subprocess.Popen(["python", "-m", "streamlit", "run", "app.py", "--server.port", "8501"])

    print("⏳ Waiting 5 seconds for Streamlit to launch...")
    time.sleep(5)

    public_url = ngrok.connect(8501)
    print(f"✅ Streamlit app is live at: {public_url.public_url}")

    print("🌍 The dashboard is now running! Close this window or press CTRL+C to stop.")

    streamlit_process.wait()
except Exception as e:
    print(f"❌ An error occurred: {e}")
    print("Please ensure your token is correct and Streamlit is installed.")

finally:
    print("Closing ngrok tunnel...")
    ngrok.kill()
    print("✅ Shutdown complete.")