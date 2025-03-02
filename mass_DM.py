import tweepy
import time

# ================== SETUP API KEYS ==================
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"
BEARER_TOKEN = "your_bearer_token"

# ================== AUTHENTICATE TWITTER API ==================
auth = tweepy.OAuth1UserHandler(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)
api = tweepy.API(auth, wait_on_rate_limit=True)

# ================== FUNCTION TO SEND MASS DMS ==================


def send_mass_dms(user_list, message):
    for user in user_list:
        try:
            # ✅ Correct DM function for Tweepy
            api.send_direct_message(
                recipient_id=user,
                text=message
            )
            print(f"✅ Sent DM to {user}")

            # Sleep to avoid rate limits
            time.sleep(10)  # Adjust if needed
        except Exception as e:
            print(f"❌ Failed to send DM to {user}: {e}")

# ================== USAGE ==================


if __name__ == "_main_":
    user_ids = ["123456789", "987654321"]  # Replace with actual Twitter user IDs
    DM_MESSAGE = "Hey! This is a test DM from my Twitter bot 🚀"

    send_mass_dms(user_ids, DM_MESSAGE)
