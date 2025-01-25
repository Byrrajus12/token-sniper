from flask import Flask, jsonify, request
from flask_cors import CORS
from liquidity_check import liquidity

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests from the frontend

@app.route('/')
def home():
    return {"message": "Welcome to the Token Sniper API!"}
@app.route('/api/contracts', methods=['GET'])
def get_contracts():
    # Dummy data for testing the endpoint
    contracts = [
        {"contract": "0x123456789...", "liquidity": 20000, "marketCap": "1,000,000"},
        {"contract": "0x987654321...", "liquidity": 15000, "marketCap": "500,000"}
    ]
    return jsonify(contracts)

@app.route('/api/set_twitter', methods=['POST'])
def set_twitter():
    data = request.json
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Save the username for monitoring (in memory or a file for now)
    app.config['MONITORED_USERNAME'] = username
    return jsonify({"message": f"Monitoring tweets for {username}"}), 200

from threading import Thread
import time

@app.route('/api/tokens', methods=['GET'])
def get_tokens():
    # Simulate fetching tokens (in production, use real scraping logic)
    username = app.config.get('MONITORED_USERNAME', 'default_user')
    if not username:
        return jsonify({"error": "No username configured"}), 400

    # Dummy token data for now
    tokens = [
        {"contract": "0x123456789...", "liquidity": 20000, "marketCap": "1,000,000", "tweetLink": "https://twitter.com/tweet1"},
        {"contract": "0x987654321...", "liquidity": 15000, "marketCap": "500,000", "tweetLink": "https://twitter.com/tweet2"}
    ]
    return jsonify(tokens)

# Background thread for scraping tweets
def background_scraper():
    while True:
        username = app.config.get('MONITORED_USERNAME', None)
        if username:
            # TODO: Implement real scraping logic here using tweet_scraper.py
            print(f"Scraping tweets for {username}")
        time.sleep(60)  # Run every 60 seconds

# Start background scraper
thread = Thread(target=background_scraper)
thread.daemon = True
thread.start()


if __name__ == '__main__':
    app.run(debug=True)
