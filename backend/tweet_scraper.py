import tweepy
import re

# 🔹 Twitter API Authentication
BEARER_TOKEN = ""

client = tweepy.Client(bearer_token=BEARER_TOKEN)

# 🔹 Target Username
USERNAME = "tweettrack10358"
LAST_TWEET_ID = None

def get_user_id(username):
    """Fetch the user's Twitter ID."""
    try:
        user = client.get_user(username=username, user_fields=["id"])
        return user.data.id if user.data else None
    except Exception as e:
        print(f"Error fetching user ID: {e}")
        return None


def get_latest_tweet(user_id):
    """Fetch the latest tweet from the user."""
    global LAST_TWEET_ID
    try:
        tweets = client.get_users_tweets(id=user_id, max_results=5, tweet_fields=["id", "text"])
        if tweets.data:
            tweet = tweets.data[0]
            tweet_id = tweet.id
            tweet_text = tweet.text
            tweet_link = f"https://twitter.com/{USERNAME}/status/{tweet_id}"

            # Only process new tweets
            if tweet_id != LAST_TWEET_ID:
                LAST_TWEET_ID = tweet_id  # Update the last tweet ID
                return tweet_text, tweet_link

    except Exception as e:
        print(f"Error fetching tweets: {e}")
    return None, None

def extract_token_addresses(tweet):
    """Extract addresses."""
    return re.findall(r'\b[A-Za-z0-9]{30,}pump\b', tweet)