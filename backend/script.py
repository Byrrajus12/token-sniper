import tweet_scraper
import time
from backend import liquidity_check
import os
import pandas as pd

# Saving contract addresses
CSV_FILE = "contracts.csv"

# Ensure the file exists
if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=["contract", "tweet_link", "time"]).to_csv(CSV_FILE, index=False)


def save_contract(contract, tweet_link):
    """Saving contract addresses."""
    df = pd.read_csv(CSV_FILE)

    # Check if contract already exists
    if contract in df["contract"].values:
        return

    # Append new contract
    new_entry = pd.DataFrame([{"contract": contract, "tweet_link": tweet_link, "time": pd.Timestamp.now()}])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    print(f"Contract address saved: {contract}")


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

            contracts = tweet_scraper.extract_token_addresses(tweet_text)
            if contracts:
                for contract in contracts:
                    liquidity, market_cap = liquidity_check.liquidity(contract)
                    save_contract(contract, tweet_link)
                    if liquidity > 10000 and market_cap:  # Only buy if liquidity > $10K
                        print(f"Safe to trade: {contract}")
                        # Call the buy function
                    else:
                        print(f"Low liquidity {contract}")
            else:
                print("No contract addresses found.")

        time.sleep(900)


if __name__ == "__main__":
    monitor_tweets()