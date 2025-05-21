from flask import Flask, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_API_KEY")
REDIRECT_URI = "http://127.0.0.1:8888/callback"

# CLIENT_ID = "2122b5793eb440ea9e0b977ec95a0d29"
# CLIENT_SECRET = "c66f81f3b14e494bb9fc4318f759873b"
# REDIRECT_URI = "http://127.0.0.1:8888/callback"


SCOPE = 'user-top-read'

app = Flask(__name__)
TOKENS_FILE = 'spotify_tokens.json'

# Load/save token mapping
if os.path.exists(TOKENS_FILE):
    with open(TOKENS_FILE, 'r') as f:
        token_store = json.load(f)
else:
    token_store = {}

@app.route('/login/<discord_id>')
def login(discord_id):
    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=SCOPE,
                            cache_path=None,
                            show_dialog=True)
    auth_url = sp_oauth.get_authorize_url(state=discord_id)
    return f'<a href="{auth_url}">Login with Spotify</a>'

@app.route('/callback')
def callback():
    try:
        code = request.args.get('code')
        discord_id = request.args.get('state')

        print("🔁 Received callback with:")
        print("   - Code:", code)
        print("   - State (Discord ID):", discord_id)

        if not code or not discord_id:
            return "❌ Missing code or state in redirect. Try again."

        sp_oauth = SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE
        )

        token_info = sp_oauth.get_access_token(code)
        print("✅ Token received:", token_info)

        token_store[discord_id] = token_info
        with open(TOKENS_FILE, 'w') as f:
            json.dump(token_store, f, indent=2)

        return f"✅ Spotify linked for user ID {discord_id}. You may now close this tab."

    except Exception as e:
        import traceback
        print("❌ OAuth error:", e)
        traceback.print_exc()
        return f"❌ Internal server error: {e}"

if __name__ == '__main__':
    app.run(port=8888)
