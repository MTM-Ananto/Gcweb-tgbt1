# 🚀 FREE Setup Guide - No Website Needed!

This guide shows you how to run your Telegram Profile Dashboard Bot **completely FREE** from your own computer without needing any paid hosting or website.

## 🎯 What You Need

1. **Your computer** (Windows, Mac, or Linux)
2. **Python 3.8+** installed
3. **Your bot token** (already configured!)

## 📦 Installation Methods

### Method 1: Automatic Setup (Recommended)

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Run the automatic setup (includes ngrok)
python run_local.py
```

### Method 2: Manual Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Install ngrok manually
# Windows: Download from https://ngrok.com/download
# Mac: brew install ngrok/ngrok/ngrok
# Linux: sudo snap install ngrok

# 3. Start ngrok in one terminal
ngrok http 5000

# 4. Copy the https URL (like https://abc123.ngrok.io)
# 5. Update .env file: WEBAPP_URL=https://abc123.ngrok.io

# 6. Run the bot
python main.py
```

## 🌐 What is ngrok?

**ngrok** is a FREE tool that creates a secure tunnel from the internet to your computer. This means:

- ✅ **FREE forever** for basic use
- ✅ **No website hosting needed**
- ✅ **Secure HTTPS tunnel**
- ✅ **Works from anywhere**
- ✅ **No technical setup required**

## 🔧 Step-by-Step Instructions

### Step 1: Prepare Your Environment

```bash
# Make sure you're in the project directory
cd /path/to/your/telegram-bot

# Install all required packages
pip install -r requirements.txt
```

### Step 2: Run the Bot

**Option A - Automatic (Easiest):**
```bash
python run_local.py
```

**Option B - Manual Control:**
```bash
# Terminal 1: Start ngrok
ngrok http 5000

# Note the HTTPS URL (like https://abc123.ngrok.io)
# Update .env: WEBAPP_URL=https://abc123.ngrok.io

# Terminal 2: Start the bot
python main.py
```

### Step 3: Test Your Bot

1. Open Telegram
2. Find your bot (search for the username you created)
3. Send `/start`
4. Click "🚀 Open Profile Dashboard"
5. Enjoy your interactive profile!

## 💡 Free Hosting Alternatives

### 1. **ngrok (Recommended)**
- ✅ Completely FREE
- ✅ Instant setup
- ✅ No registration needed for basic use
- ❌ URL changes each restart (Pro version has static URLs)

### 2. **Railway.app**
- ✅ FREE tier available
- ✅ Static URL
- ✅ Git integration
- ❌ Requires account signup

### 3. **Render.com**
- ✅ FREE tier available
- ✅ Static URL
- ✅ Easy deployment
- ❌ Requires account signup

### 4. **Heroku**
- ✅ FREE tier available (limited hours)
- ✅ Static URL
- ❌ Requires credit card verification

## 🛠️ Troubleshooting

### Bot Not Responding?
```bash
# Check if bot token is correct
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('Bot token loaded:', bool(os.getenv('BOT_TOKEN')))"
```

### ngrok Issues?
```bash
# Check if ngrok is installed
ngrok version

# Check if port 5000 is free
netstat -tulpn | grep :5000
```

### WebApp Not Loading?
1. Make sure ngrok URL is HTTPS (not HTTP)
2. Check that WEBAPP_URL in .env matches ngrok URL
3. Restart the bot after updating .env

## 🎉 Success!

Once everything is running, you'll see:

```
🚀 Telegram Profile Dashboard Bot - Local Setup
============================================================
✅ ngrok is already installed
🌐 Starting ngrok tunnel...
✅ Updated .env with ngrok URL: https://abc123.ngrok.io
🌍 Public URL: https://abc123.ngrok.io
📱 Your bot is now accessible from anywhere!

============================================================
🎯 HOW TO USE:
1. Open Telegram and find your bot
2. Send /start to the bot
3. Click 'Open Profile Dashboard'
4. Enjoy your interactive profile!
============================================================

🌐 Starting webapp server...
🤖 Starting Telegram bot...
```

Your bot is now running **completely FREE** and accessible from anywhere in the world! 🌍

## 💰 Cost Breakdown

- **Python**: FREE ✅
- **ngrok**: FREE ✅
- **Your computer**: Already have it ✅
- **Bot token**: FREE ✅
- **Total cost**: **$0.00** ✅

Enjoy your beautiful, interactive Telegram profile dashboard! 🎨✨