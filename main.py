#!/usr/bin/env python3
"""
Telegram Profile Dashboard Bot
A comprehensive bot with webapp integration for displaying user profile data
"""

import asyncio
import threading
import subprocess
import sys
import os
from pathlib import Path

def run_webapp():
    """Run the Flask webapp server"""
    print("🌐 Starting webapp server...")
    subprocess.run([sys.executable, "webapp.py"], cwd=Path(__file__).parent)

def run_bot():
    """Run the Telegram bot"""
    print("🤖 Starting Telegram bot...")
    subprocess.run([sys.executable, "bot.py"], cwd=Path(__file__).parent)

def main():
    """Main function to start both bot and webapp"""
    print("🚀 Starting Telegram Profile Dashboard Bot...")
    print("=" * 50)
    
    # Check if .env file exists
    env_file = Path(".env")
    if not env_file.exists():
        print("⚠️  .env file not found!")
        print("Please create a .env file based on .env.example")
        print("Add your BOT_TOKEN and other configuration")
        return
    
    try:
        # Start webapp in a separate thread
        webapp_thread = threading.Thread(target=run_webapp, daemon=True)
        webapp_thread.start()
        
        # Start bot in main thread
        run_bot()
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
