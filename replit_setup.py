#!/usr/bin/env python3
"""
Replit Setup Script for Telegram Profile Dashboard Bot
Automatically configures the bot for Replit environment
"""

import os
import time
import threading
import subprocess
import sys
from pathlib import Path

def setup_replit_environment():
    """Configure environment for Replit"""
    print("🔧 Setting up Replit environment...")
    
    # Get Replit URL
    repl_name = os.getenv('REPL_SLUG', 'telegram-bot')
    repl_owner = os.getenv('REPL_OWNER', 'user')
    replit_url = f"https://{repl_name}.{repl_owner}.repl.co"
    
    print(f"📍 Detected Replit URL: {replit_url}")
    
    # Update .env file with Replit URL
    env_file = Path('.env')
    if env_file.exists():
        content = env_file.read_text()
        
        # Replace the webapp URL with Replit URL
        if 'WEBAPP_URL=' in content:
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('WEBAPP_URL='):
                    lines[i] = f'WEBAPP_URL={replit_url}'
                    break
            content = '\n'.join(lines)
        else:
            content += f'\nWEBAPP_URL={replit_url}'
        
        env_file.write_text(content)
        print(f"✅ Updated .env with Replit URL: {replit_url}")
    
    return replit_url

def check_bot_token():
    """Check if bot token is configured"""
    from dotenv import load_dotenv
    load_dotenv()
    
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token:
        print("❌ BOT_TOKEN not found!")
        print("Please add your bot token to Replit Secrets:")
        print("1. Click the lock icon (🔒) on the left sidebar")
        print("2. Add key: BOT_TOKEN")
        print("3. Add value: your_bot_token_here")
        return False
    
    print(f"✅ Bot token configured: {bot_token[:10]}...")
    return True

def run_webapp():
    """Run the Flask webapp"""
    print("🌐 Starting webapp server...")
    subprocess.run([sys.executable, "webapp.py"])

def run_bot():
    """Run the Telegram bot"""
    print("🤖 Starting Telegram bot...")
    subprocess.run([sys.executable, "bot.py"])

def main():
    """Main function for Replit setup"""
    print("🚀 Telegram Profile Dashboard Bot - Replit Setup")
    print("=" * 60)
    
    # Setup Replit environment
    replit_url = setup_replit_environment()
    
    # Check bot token
    if not check_bot_token():
        return
    
    print("\n" + "=" * 60)
    print("🎯 REPLIT SETUP COMPLETE!")
    print(f"🌍 Your bot webapp URL: {replit_url}")
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
        time.sleep(2)
        
        # Start bot in main thread
        run_bot()
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()