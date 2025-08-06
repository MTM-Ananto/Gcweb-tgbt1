import logging
import os
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBAPP_URL = os.getenv('WEBAPP_URL', 'http://localhost:5000')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with a button that opens the webapp."""
    user = update.effective_user
    
    # Create webapp button
    webapp = WebAppInfo(url=f"{WEBAPP_URL}/webapp")
    keyboard = [
        [InlineKeyboardButton("🚀 Open Profile Dashboard", web_app=webapp)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = f"""
🎉 Welcome to Profile Dashboard Bot, {user.first_name}!

Click the button below to view your interactive profile with:
• User information & stats
• Premium status
• Profile picture
• Account details
• Interactive animations

✨ Enjoy the elegant experience!
"""
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
🤖 <b>Profile Dashboard Bot Commands</b>

/start - Open your interactive profile dashboard
/help - Show this help message
/profile - Quick access to your profile

<b>Features:</b>
• Real-time user data display
• Premium status tracking
• Interactive animations
• Mobile-optimized design
• Touch-friendly interface

Just click the webapp button to get started! 🚀
"""
    await update.message.reply_text(help_text, parse_mode='HTML')

async def profile_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Quick profile access command."""
    webapp = WebAppInfo(url=f"{WEBAPP_URL}/webapp")
    keyboard = [
        [InlineKeyboardButton("📱 View Profile", web_app=webapp)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "📊 Access your profile dashboard:",
        reply_markup=reply_markup
    )

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle data sent from the webapp."""
    try:
        data = json.loads(update.effective_message.web_app_data.data)
        user = update.effective_user
        
        # Process webapp data here if needed
        await update.message.reply_text(
            f"✅ Data received from webapp! Thanks {user.first_name}!"
        )
    except Exception as e:
        logger.error(f"Error processing webapp data: {e}")
        await update.message.reply_text("❌ Error processing data from webapp.")

def main() -> None:
    """Start the bot."""
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN not found in environment variables!")
        return
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("profile", profile_command))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))

    # Run the bot
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()