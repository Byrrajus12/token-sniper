import tweet_scraper
import time
def monitor_tweets():
    """Continuously monitor Twitter for new posts from the user."""
    user_id = tweet_scraper.get_user_id(tweet_scraper.USERNAME)
    if not user_id:
        print("Failed to retrieve user ID. Exiting.")
        return

    print(f"✅ Monitoring tweets from @{tweet_scraper.USERNAME}")

    while True:
        tweet_text, tweet_link = tweet_scraper.get_latest_tweet(user_id)

        if tweet_text:
            print(f"\n New Tweet: {tweet_text}")
            print(f" Tweet Link: {tweet_link}")

        time.sleep(30)
monitor_tweets()