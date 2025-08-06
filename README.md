# 🤖 Telegram Profile Dashboard Bot

A sophisticated Telegram bot with an interactive webapp that displays comprehensive user profile information with elegant animations and mobile-optimized design.

## ✨ Features

### 🎯 Core Features
- **Real-time User Data Display**: Shows all available Telegram user information
- **Premium Status Tracking**: Detects and displays Telegram Premium subscription
- **Profile Photo Display**: Shows user's profile picture or initials
- **Interactive Dashboard**: Beautiful cards with user stats and information
- **Mobile Optimized**: Touch-friendly interface designed for Android devices

### 🎨 Design & UX
- **Elegant Theme**: Black, white, grey, and light blue color scheme
- **Smooth Animations**: Loading animations, card transitions, and hover effects
- **Touch Support**: Swipe gestures and haptic feedback
- **Responsive Design**: Adapts to all screen sizes
- **Modern UI**: Glassmorphism effects and gradient backgrounds

### 📱 User Information Displayed
- User ID and Username
- First Name and Last Name
- Profile Picture
- Language Code
- Premium Status
- PM Permissions
- Attachment Menu Status
- Account Statistics
- Join Date and Activity

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- A Telegram Bot Token (from [@BotFather](https://t.me/botfather))

### Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your configuration:
   ```env
   BOT_TOKEN=your_bot_token_from_botfather
   WEBAPP_URL=https://your-domain.com
   SECRET_KEY=your_secret_key_here
   PORT=5000
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Telegram Bot Token from @BotFather | ✅ Yes |
| `WEBAPP_URL` | Your webapp's public URL | ✅ Yes |
| `SECRET_KEY` | Flask secret key for sessions | ❌ No |
| `PORT` | Port for the webapp server | ❌ No (default: 5000) |

### Getting a Bot Token

1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` and follow the instructions
3. Choose a name and username for your bot
4. Copy the token and add it to your `.env` file

### Setting Up WebApp URL

For development:
- Use `http://localhost:5000` for local testing
- Use tools like ngrok for external access: `ngrok http 5000`

For production:
- Deploy to a cloud service (Heroku, Railway, DigitalOcean, etc.)
- Use your domain URL

## 📂 Project Structure

```
telegram-profile-bot/
├── main.py              # Main application runner
├── bot.py               # Telegram bot implementation
├── webapp.py            # Flask webapp server
├── requirements.txt     # Python dependencies
├── .env.example        # Environment template
├── README.md           # This file
└── templates/
    ├── index.html      # Home page
    └── webapp.html     # Main webapp interface
```

## 🎮 Usage

### For Users

1. **Start the bot**: Send `/start` to your bot
2. **Open Dashboard**: Tap "🚀 Open Profile Dashboard"
3. **Explore Features**: 
   - View your profile information
   - Check premium status
   - See account statistics
   - Refresh data anytime
   - Share your profile

### Bot Commands

- `/start` - Show welcome message and webapp button
- `/help` - Display help information
- `/profile` - Quick access to profile dashboard

## 🛠️ Development

### Running Locally

1. Set up the environment as described above
2. For development, you can run components separately:
   ```bash
   # Run webapp only
   python webapp.py
   
   # Run bot only  
   python bot.py
   
   # Run both (recommended)
   python main.py
   ```

### File Structure Details

- **`bot.py`**: Handles Telegram bot logic, commands, and webapp integration
- **`webapp.py`**: Flask server with API endpoints and authentication
- **`templates/webapp.html`**: Main interactive dashboard with animations
- **`templates/index.html`**: Landing page with bot information

## 🔐 Security Features

- **Telegram WebApp Authentication**: Verifies data integrity using HMAC
- **Secure Data Transmission**: All user data is validated server-side
- **No Data Storage**: User information is fetched in real-time
- **CORS Protection**: Configured for secure cross-origin requests

## 🎨 Customization

### Themes
The webapp uses CSS custom properties for easy theming. Main colors:
- Primary: `#87CEEB` (Light Blue)
- Background: `#1a1a1a` (Dark)
- Text: `#ffffff` (White)
- Secondary: `#b0b0b0` (Grey)

### Animations
All animations are CSS-based and can be customized:
- Loading spinner
- Card hover effects
- Slide-in animations
- Float animation for profile photo
- Glowing premium badge

## 📱 Mobile Features

- **Touch Optimized**: Large touch targets and gestures
- **Swipe Support**: Swipe up/down detection
- **Haptic Feedback**: For supported devices
- **Responsive Design**: Works on all screen sizes
- **No Zoom**: Prevents accidental zooming

## 🚀 Deployment

### Heroku
1. Create a new Heroku app
2. Set environment variables in Heroku dashboard
3. Deploy using Git or GitHub integration

### Railway
1. Connect your GitHub repository
2. Set environment variables
3. Deploy automatically

### DigitalOcean App Platform
1. Create a new app
2. Connect repository
3. Configure environment variables

## ❗ Troubleshooting

### Common Issues

**Bot not responding**:
- Check BOT_TOKEN is correct
- Ensure bot is not blocked
- Verify internet connection

**WebApp not loading**:
- Check WEBAPP_URL is accessible
- Verify SSL certificate (HTTPS required for production)
- Check Flask server is running

**Authentication errors**:
- Ensure BOT_TOKEN matches the webapp configuration
- Check Telegram WebApp data integrity

**Mobile issues**:
- Clear browser cache
- Check touch events in developer tools
- Verify viewport settings

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 🆘 Support

If you need help:
1. Check this README
2. Review the troubleshooting section
3. Open an issue on GitHub
4. Check Telegram Bot API documentation

---

**Made with ❤️ for the Telegram community**