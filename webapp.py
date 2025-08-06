from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import hmac
import hashlib
import urllib.parse
import json
import base64
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

BOT_TOKEN = os.getenv('BOT_TOKEN')

def verify_telegram_webapp_data(init_data: str, bot_token: str) -> dict:
    """
    Verify Telegram WebApp init data and return user data if valid.
    """
    try:
        # Parse the init data
        parsed_data = urllib.parse.parse_qs(init_data)
        
        # Extract the hash
        received_hash = parsed_data.get('hash', [''])[0]
        if not received_hash:
            return None
        
        # Remove hash from data for verification
        data_check_dict = {k: v[0] for k, v in parsed_data.items() if k != 'hash'}
        
        # Create data check string
        data_check_string = '\n'.join([f"{k}={v}" for k, v in sorted(data_check_dict.items())])
        
        # Create secret key
        secret_key = hmac.new("WebAppData".encode(), bot_token.encode(), hashlib.sha256).digest()
        
        # Calculate hash
        calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
        
        # Verify hash
        if calculated_hash == received_hash:
            # Parse user data
            user_data = json.loads(data_check_dict.get('user', '{}'))
            return user_data
        
        return None
    except Exception as e:
        print(f"Error verifying webapp data: {e}")
        return None

@app.route('/')
def index():
    """Home page with bot info."""
    return render_template('index.html')

@app.route('/webapp')
def webapp():
    """Main webapp page."""
    return render_template('webapp.html')

@app.route('/api/user', methods=['POST'])
def get_user_data():
    """Get user data from Telegram WebApp init data."""
    try:
        data = request.get_json()
        init_data = data.get('initData', '')
        
        if not init_data:
            return jsonify({'error': 'No init data provided'}), 400
        
        # Verify and get user data
        user_data = verify_telegram_webapp_data(init_data, BOT_TOKEN)
        
        if not user_data:
            return jsonify({'error': 'Invalid init data'}), 401
        
        # Enhance user data with additional info
        enhanced_data = {
            'id': user_data.get('id'),
            'first_name': user_data.get('first_name', ''),
            'last_name': user_data.get('last_name', ''),
            'username': user_data.get('username', ''),
            'language_code': user_data.get('language_code', 'en'),
            'is_premium': user_data.get('is_premium', False),
            'photo_url': user_data.get('photo_url', ''),
            'allows_write_to_pm': user_data.get('allows_write_to_pm', False),
            'added_to_attachment_menu': user_data.get('added_to_attachment_menu', False)
        }
        
        return jsonify({
            'success': True,
            'user': enhanced_data
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['POST'])
def get_user_stats():
    """Get additional user statistics."""
    try:
        data = request.get_json()
        init_data = data.get('initData', '')
        
        user_data = verify_telegram_webapp_data(init_data, BOT_TOKEN)
        if not user_data:
            return jsonify({'error': 'Unauthorized'}), 401
        
        # Mock statistics (in real app, fetch from database)
        stats = {
            'join_date': '2024-01-15',
            'total_interactions': 127,
            'last_seen': 'Just now',
            'favorite_feature': 'Profile Dashboard',
            'account_age_days': 350,
            'premium_since': '2024-06-01' if user_data.get('is_premium') else None
        }
        
        return jsonify({
            'success': True,
            'stats': stats
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)