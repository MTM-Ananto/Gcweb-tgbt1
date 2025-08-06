#!/usr/bin/env python3
"""
Local runner with ngrok integration for free hosting
This script automatically sets up ngrok and updates the webapp URL
"""

import subprocess
import sys
import os
import time
import threading
import requests
import json
from pathlib import Path

def install_ngrok():
    """Install ngrok if not available"""
    try:
        subprocess.run(["ngrok", "version"], capture_output=True, check=True)
        print("✅ ngrok is already installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("📦 Installing ngrok...")
        if sys.platform.startswith('win'):
            print("Please install ngrok manually from: https://ngrok.com/download")
            print("1. Download ngrok for Windows")
            print("2. Extract to a folder in your PATH")
            print("3. Run this script again")
            sys.exit(1)
        elif sys.platform.startswith('linux'):
            try:
                # Try to install via snap
                subprocess.run(["sudo", "snap", "install", "ngrok"], check=True)
            except:
                print("Please install ngrok manually:")
                print("wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz")
                print("tar xvzf ngrok-v3-stable-linux-amd64.tgz")
                print("sudo mv ngrok /usr/local/bin")
                sys.exit(1)
        elif sys.platform.startswith('darwin'):
            try:
                subprocess.run(["brew", "install", "ngrok/ngrok/ngrok"], check=True)
            except:
                print("Please install ngrok via Homebrew: brew install ngrok/ngrok/ngrok")
                sys.exit(1)

def get_ngrok_url():
    """Get the ngrok public URL"""
    try:
        response = requests.get("http://localhost:4040/api/tunnels")
        tunnels = response.json()
        for tunnel in tunnels['tunnels']:
            if tunnel['config']['addr'] == 'http://localhost:5000':
                return tunnel['public_url']
    except:
        return None

def update_env_file(ngrok_url):
    """Update the .env file with the ngrok URL"""
    env_file = Path('.env')
    if env_file.exists():
        content = env_file.read_text()
        # Replace the webapp URL
        new_content = content.replace(
            'WEBAPP_URL=https://your-ngrok-url.ngrok.io',
            f'WEBAPP_URL={ngrok_url}'
        )
        env_file.write_text(new_content)
        print(f"✅ Updated .env with ngrok URL: {ngrok_url}")

def start_ngrok():
    """Start ngrok tunnel"""
    print("🌐 Starting ngrok tunnel...")
    ngrok_process = subprocess.Popen(
        ["ngrok", "http", "5000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait a bit for ngrok to start
    time.sleep(3)
    
    # Get the public URL
    ngrok_url = get_ngrok_url()
    if ngrok_url:
        update_env_file(ngrok_url)
        return ngrok_process, ngrok_url
    else:
        print("❌ Failed to get ngrok URL")
        ngrok_process.kill()
        return None, None

def run_webapp():
    """Run the Flask webapp"""
    print("🌐 Starting webapp server...")
    subprocess.run([sys.executable, "webapp.py"])

def run_bot():
    """Run the Telegram bot"""
    print("🤖 Starting Telegram bot...")
    subprocess.run([sys.executable, "bot.py"])

def main():
    """Main function"""
    print("🚀 Telegram Profile Dashboard Bot - Local Setup")
    print("=" * 60)
    
    # Check if .env exists
    if not Path('.env').exists():
        print("❌ .env file not found!")
        print("Please make sure .env file exists with your bot token")
        return
    
    # Install ngrok if needed
    install_ngrok()
    
    try:
        # Start ngrok
        ngrok_process, ngrok_url = start_ngrok()
        if not ngrok_process:
            print("❌ Failed to start ngrok")
            return
        
        print(f"🌍 Public URL: {ngrok_url}")
        print("📱 Your bot is now accessible from anywhere!")
        print("\n" + "=" * 60)
        print("🎯 HOW TO USE:")
        print("1. Open Telegram and find your bot")
        print("2. Send /start to the bot")
        print("3. Click 'Open Profile Dashboard'")
        print("4. Enjoy your interactive profile!")
        print("=" * 60 + "\n")
        
        # Start webapp in a separate thread
        webapp_thread = threading.Thread(target=run_webapp, daemon=True)
        webapp_thread.start()
        
        # Small delay to let webapp start
        time.sleep(2)
        
        # Start bot in main thread
        run_bot()
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")
        if 'ngrok_process' in locals():
            ngrok_process.kill()
    except Exception as e:
        print(f"❌ Error: {e}")
        if 'ngrok_process' in locals():
            ngrok_process.kill()

if __name__ == "__main__":
    main()