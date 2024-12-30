import tweepy

# Replace with your credentials
BEARER_TOKEN = "your_bearer_token"
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Authenticate with Twitter API
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Function to get followers
def get_followers(client, user_id):
    followers = set()
    for follower in tweepy.Paginator(client.get_users_followers, id=user_id, max_results=1000):
        followers.update([user["id"] for user in follower.data or []])
    return followers

# Function to get following
def get_following(client, user_id):
    following = set()
    for follow in tweepy.Paginator(client.get_users_following, id=user_id, max_results=1000):
        following.update([user["id"] for user in follow.data or []])
    return following

# Get your user ID
user = client.get_me()
user_id = user.data["id"]

# Get followers and following lists
followers = get_followers(client, user_id)
following = get_following(client, user_id)

# Find non-followers
non_followers = following - followers
print(f"Users not following back: {non_followers}")

# Unfollow users who don’t follow back
for user_id in non_followers:
    response = client.unfollow_user(target_user_id=user_id)
    if response.data["following"] is False:
        print(f"Unfollowed user ID {user_id}")
    else:
        print(f"Failed to unfollow user ID {user_id}")