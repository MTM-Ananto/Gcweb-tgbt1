#!/usr/bin/env python3
"""
Railway Deployment Setup for Telegram Profile Dashboard Bot
Automatically configures the bot for Railway environment
"""

import os
import threading
import subprocess
import sys
from pathlib import Path

def setup_railway_environment():
    """Configure environment for Railway"""
    print("🚂 Setting up Railway environment...")
    
    # Railway automatically sets RAILWAY_STATIC_URL
    railway_url = os.getenv('RAILWAY_STATIC_URL')
    if not railway_url:
        # Fallback to environment variable or local
        railway_url = os.getenv('WEBAPP_URL', 'http://localhost:5000')
    
    print(f"📍 Detected Railway URL: {railway_url}")
    
    # Update environment
    os.environ['WEBAPP_URL'] = railway_url
    
    return railway_url

def check_environment():
    """Check if all required environment variables are set"""
    from dotenv import load_dotenv
    load_dotenv()
    
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token:
        print("❌ BOT_TOKEN not found!")
        print("Please set BOT_TOKEN in Railway environment variables:")
        print("1. Go to Railway dashboard")
        print("2. Select your project")
        print("3. Go to Variables tab")
        print("4. Add BOT_TOKEN with your bot token")
        return False
    
    print(f"✅ Bot token configured: {bot_token[:10]}...")
    return True

def run_webapp():
    """Run the Flask webapp"""
    print("🌐 Starting webapp server on Railway...")
    subprocess.run([sys.executable, "webapp.py"])

def run_bot():
    """Run the Telegram bot"""
    print("🤖 Starting Telegram bot...")
    subprocess.run([sys.executable, "bot.py"])

def main():
    """Main function for Railway deployment"""
    print("🚂 Telegram Profile Dashboard Bot - Railway Deployment")
    print("=" * 60)
    
    # Setup Railway environment
    railway_url = setup_railway_environment()
    
    # Check environment variables
    if not check_environment():
        return
    
    print("\n" + "=" * 60)
    print("🎯 RAILWAY DEPLOYMENT COMPLETE!")
    print(f"🌍 Your bot webapp URL: {railway_url}")
    print("📱 Your bot is now accessible from anywhere!")
    print("\n" + "=" * 60)
    print("🎯 HOW TO USE:")
    print("1. Open Telegram and find your bot")
    print("2. Send /start to the bot")
    print("3. Click 'Open Profile Dashboard'")
    print("4. Enjoy your interactive profile!")
    print("=" * 60 + "\n")
    
    try:
        # Start webapp in a separate thread
        webapp_thread = threading.Thread(target=run_webapp, daemon=True)
        webapp_thread.start()
        
        # Small delay to let webapp start
        import time
        time.sleep(2)
        
        # Start bot in main thread
        run_bot()
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()