import discord
from discord.ext import commands
import random
import requests
import json
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import datetime
import tempfile
from discord import SelectOption, Embed


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="-", intents=intents)

STEAM_API_KEY = os.getenv("STEAM_API_KEY")
DISCOD_BOT_TOKEN = os.getenv("DISCOD_BOT_TOKEN")
HYPIXEL_API_KEY = os.getenv("HYPIXEL_API_KEY")
LASTFM_API_KEY = os.getenv("FM_API_KEY")

LASTFM_LINK_FILE = "lastfm_links.json"
GHOST_JSON_PATH = "phasmophobia_ghosts.json"

cwd = os.getcwd()

#----------Hypixel leveling----------#
SKILL_XP_TABLE = [
    0, 50, 175, 375, 675, 1175, 1925, 2925, 4425, 6425,
    9925, 14925, 22425, 32425, 47425, 67425, 97425, 147425, 222425, 322425,
    522425, 822425, 1222425, 1722425, 2322425, 3022425, 3822425, 4722425, 5722425, 6822425,
    8022425, 9322425, 10722425, 12222425, 13822425, 15522425, 17322425, 19222425, 21222425, 23322425,
    25522425, 27822425, 30222425, 32722425, 35322425, 38022425, 40822425, 43722425, 46722425, 49822425,
    53022425, 56322425, 59722425, 63222425, 66822425, 70522425, 74322425, 78222425, 82222425, 86322425
]

def xp_to_level(xp: float) -> int:
    for level, required in enumerate(SKILL_XP_TABLE):
        if xp < required:
            return level - 1
    return len(SKILL_XP_TABLE) - 1

SLAYER_XP_TABLE = [0, 5, 15, 200, 1000, 5000, 20000, 100000, 400000, 1000000]

def slayer_xp_to_level(xp: int) -> int:
    for level, required in enumerate(SLAYER_XP_TABLE):
        if xp < required:
            return level - 1
    return len(SLAYER_XP_TABLE) - 1

# -------- Steam ID Store --------
STEAM_LINK_FILE = "steam_links.json"

# Load Steam ID links from file
if os.path.exists(STEAM_LINK_FILE):
    with open(STEAM_LINK_FILE, "r") as f:
        user_steam_ids = json.load(f)
else:
    user_steam_ids = {}

# Save Steam ID links to file
def save_steam_links():
    with open(STEAM_LINK_FILE, "w") as f:
        json.dump(user_steam_ids, f)

# -------- Bot Events --------
@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send("I gotta poopy")
    
    await bot.process_commands(message)

# -------- Commands --------
@bot.command(name="bark")
async def bark(ctx):
    folder = os.path.join(cwd, 'pics', 'benno_pics')
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No benno pics found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending benno image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="twink")
async def twink(ctx):
    folder = os.path.join(cwd, 'pics', 'twink')
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No twink pics found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending twink image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="varun")
async def varun(ctx):
    folder = os.path.join(cwd, 'pics', 'varun')
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No varun pics found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending varun image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="twins")
async def twins(ctx):
    folder = os.path.join(cwd, 'pics', 'twins')
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No twin pics found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending twins image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="nate")
async def nate(ctx):
    folder = os.path.join(cwd, 'pics', 'nate')
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No nate pics found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending nate image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="oppshoota")
async def oppshoota(ctx):
    folder = os.path.join(cwd, 'pics', 'oppshoota')
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No opps found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending shoota image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="meow")
async def meow(ctx):
    folder = os.path.join(cwd, 'pics', 'sophie_pics')
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No cat images found.")
        return
    image_path = os.path.join(folder, random.choice(images))
    try:
        print("Sending image:", image_path)
        await ctx.send(file=discord.File(image_path))
    except Exception as e:
        print("❌ Failed to send:", image_path)
        print("Error:", e)
        await ctx.send("⚠️ Could not send that image. It may be too large or corrupted.")

@bot.command(name="woof")
async def woof(ctx):
    folder = os.path.join(cwd, 'pics', 'franklin_pics')
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No dog images found.")
        return
    image_path = os.path.join(folder, random.choice(images))
    try:
        print("Sending image:", image_path)
        await ctx.send(file=discord.File(image_path))
    except Exception as e:
        print("❌ Failed to send:", image_path)
        print("Error:", e)
        await ctx.send("⚠️ Could not send that image. It may be too large or corrupted.")

@bot.command(name="bigbootylatina")
async def bigbootylatina(ctx):
    folder = os.path.join(cwd, 'pics', 'big_booty_latina')
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No big booty latinas found.")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending big booty latinas:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="rangrang")
async def rangrang(ctx):
    folder = os.path.join(cwd, 'pics', 'rangrang')
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No chinese found.")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending chinese pics:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="jesus")
async def jesus(ctx):
    folder = os.path.join(cwd, 'pics', 'jesus')
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("jesus is dead")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("reviving jesus:", image_path)
    await ctx.send(file=discord.File(image_path))

#----------LASTFM--------#
if os.path.exists(LASTFM_LINK_FILE):
    with open(LASTFM_LINK_FILE, "r") as f:
        lastfm_users = json.load(f)
else:
    lastfm_users = {}
# Save updated links
def save_lastfm_links():
    with open(LASTFM_LINK_FILE, "w") as f:
        json.dump(lastfm_users, f)

@bot.command(name="linkfm")
async def linkfm(ctx, username: str):
    user_id = str(ctx.author.id)

    # Load existing links or initialize
    if os.path.exists("lastfm_links.json"):
        with open("lastfm_links.json", "r") as f:
            user_links = json.load(f)
    else:
        user_links = {}

    user_links[user_id] = username

    with open("lastfm_links.json", "w") as f:
        json.dump(user_links, f)

    await ctx.send(f"✅ Linked your Last.fm as `{username}`.")

@bot.command(name="fmtop")
async def fm(ctx, username: str = None):
    user_id = str(ctx.author.id)

    # Use linked username if none provided
    if not username:
        username = lastfm_users.get(user_id)
        if not username:
            await ctx.send("⚠️ You haven’t linked your Last.fm. Use `-linkfm <username>` first.")
            return

    url = f"http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={username}&api_key={LASTFM_API_KEY}&format=json&limit=5&period=7day"
    res = requests.get(url)

    if res.status_code != 200:
        await ctx.send("❌ Failed to fetch Last.fm data. Check your username or try again later.")
        print("Status:", res.status_code)
        print("Raw response:", res.text)
        return

    data = res.json()
    tracks = data.get("toptracks", {}).get("track", [])
    if not tracks:
        await ctx.send(f"⚠️ No recent tracks found for `{username}`.")
        return

    embed = discord.Embed(
        title=f"🎶 Top Tracks This Week for {username}",
        color=discord.Color.purple()
    )

    for i, track in enumerate(tracks):
        name = track["name"]
        artist = track["artist"]["name"]
        playcount = track["playcount"]
        embed.add_field(name=f"{i+1}. {name}", value=f"Artist: {artist} — {playcount} plays", inline=False)

    await ctx.send(embed=embed)

@bot.command(name="fm", description="Show now playing or last played track from Last.fm")
async def lastfm_nowplaying(ctx, target_username: str = None):
    user_id = str(ctx.author.id)

    # Load Last.fm links
    if os.path.exists("lastfm_links.json"):
        with open("lastfm_links.json", "r") as f:
            user_links = json.load(f)
    else:
        user_links = {}

    if user_id not in user_links:
        await ctx.send("⚠️ You haven’t linked your Last.fm. Use `-linkfm <username>`.")
        return

    if target_username:
        username = target_username
        display_name = target_username
    else:
        username = user_links[user_id]
        display_name = ctx.author.display_name

    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&api_key={LASTFM_API_KEY}&format=json&limit=1"
    res = requests.get(url)

    if res.status_code != 200:
        await ctx.send("❌ Failed to fetch Last.fm data. Try again later.")
        return

    data = res.json()
    tracks = data.get("recenttracks", {}).get("track", [])
    if not tracks:
        await ctx.send(f"📭 No recent tracks found for `{display_name}`.")
        return

    track = tracks[0]
    artist = track.get("artist", {}).get("#text", "Unknown Artist")
    title = track.get("name", "Unknown Track")
    album = track.get("album", {}).get("#text", "Unknown Album")
    now_playing = track.get("@attr", {}).get("nowplaying", "false") == "true"
    image_url = track.get("image", [{}])[-1].get("#text", "")

    embed = discord.Embed(
        title="🎧 Now Playing" if now_playing else "🎶 Last Played",
        description=f"**{title}** by *{artist}*",
        color=discord.Color.blue()
    )
    embed.set_author(name=display_name)
    embed.add_field(name="Album", value=album, inline=True)
    embed.add_field(name="Last.fm", value=f"[View on Last.fm](https://www.last.fm/user/{username})", inline=True)
    if image_url:
        embed.set_thumbnail(url=image_url)

    await ctx.send(embed=embed)

@bot.command(name="lyrics")
async def lyrics(ctx, username: str = None):
    user_id = str(ctx.author.id)

    # Load linked Last.fm usernames
    if os.path.exists("lastfm_links.json"):
        with open("lastfm_links.json", "r") as f:
            user_links = json.load(f)
    else:
        user_links = {}

    # Use linked username if none provided
    if not username:
        if user_id not in user_links:
            await ctx.send("⚠️ You haven’t linked your Last.fm account. Use `-linkfm <username>`.")
            return
        username = user_links[user_id]

    # Get now playing or last played track
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&api_key={LASTFM_API_KEY}&format=json&limit=1"
    res = requests.get(url)

    if res.status_code != 200:
        await ctx.send("❌ Failed to fetch Last.fm data.")
        return

    data = res.json()
    tracks = data.get("recenttracks", {}).get("track", [])
    if not tracks:
        await ctx.send(f"📭 No recent tracks found for `{username}`.")
        return

    track = tracks[0]
    artist = track.get("artist", {}).get("#text", "Unknown Artist")
    title = track.get("name", "Unknown Track")

    # Get lyrics
    lyrics_res = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{title}")
    if lyrics_res.status_code != 200:
        await ctx.send(f"❌ Lyrics not found for **{title}** by *{artist}*.")
        return

    lyrics = lyrics_res.json().get("lyrics", "Lyrics not available.").strip()

    # Build embed
    embed = discord.Embed(
        title=f"🎶 Lyrics for {title}",
        description=f"By {artist}",
        color=discord.Color.magenta()
    )

    # Split lyrics into chunks of 1024 characters (Discord limit per field)
    chunks = [lyrics[i:i+1024] for i in range(0, len(lyrics), 1024)]

    for i, chunk in enumerate(chunks[:5]):  # Limit to first 5 parts
        name = "Lyrics" if i == 0 else f"Part {i+1}"
        embed.add_field(name=name, value=chunk, inline=False)

    await ctx.send(embed=embed)


#-------STEAM GAMES-----------#
@bot.command(name="linksteam")
async def linksteam(ctx, steam_id: str):
    user_steam_ids[str(ctx.author.id)] = steam_id
    save_steam_links()
    await ctx.send(f"✅ Linked your Steam ID: `{steam_id}`")

@bot.command(name="stats")
async def stats(ctx):
    steam_id = user_steam_ids.get(str(ctx.author.id))
    if not steam_id:
        await ctx.send("⚠️ You haven’t linked your Steam account. Use `-linksteam <steam_id>`.")
        return

    url = f"http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={STEAM_API_KEY}&steamid={steam_id}&format=json"
    response = requests.get(url)

    if response.status_code != 200:
        await ctx.send("❌ Failed to fetch stats. Try again later.")
        return

    data = response.json()
    games = data.get("response", {}).get("games", [])
    if not games:
        await ctx.send("📭 You haven’t played any games in the last 2 weeks.")
        return

    embed = discord.Embed(
        title=f"🎮 Recent Steam Playtime (Last 2 Weeks)",
        description="Here are your most recently played games:",
        color=discord.Color.green()
    )

    for game in games:
        name = game['name']
        hours = round(game.get('playtime_2weeks', 0) / 60, 1)
        embed.add_field(name=name, value=f"{hours} hrs", inline=False)

    await ctx.send(embed=embed)


@bot.command(name="topgames")
async def topgames(ctx):
    steam_id = user_steam_ids.get(str(ctx.author.id))
    if not steam_id:
        await ctx.send("⚠️ You haven’t linked your Steam account. Use `-linksteam <steam_id>`.")
        return

    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={STEAM_API_KEY}&steamid={steam_id}&include_appinfo=1&format=json"
    response = requests.get(url)

    if response.status_code != 200:
        await ctx.send("❌ Could not retrieve your top games. Try again later.")
        return

    data = response.json()
    games = data.get("response", {}).get("games", [])
    if not games:
        await ctx.send("📭 You don’t seem to own any games.")
        return

    sorted_games = sorted(games, key=lambda g: g.get("playtime_forever", 0), reverse=True)
    top_games = sorted_games[:5]

    embed = discord.Embed(
        title=f"🏆 Top 5 Played Games on Steam",
        description=f"For {ctx.author.display_name}",
        color=discord.Color.orange()
    )

    for game in top_games:
        name = game['name']
        hours = round(game.get('playtime_forever', 0) / 60, 1)
        embed.add_field(name=name, value=f"{hours} hrs", inline=False)

    await ctx.send(embed=embed)


@bot.command(name="gameinfo")
async def gameinfo(ctx, *, game_name: str):
    search_url = f"https://store.steampowered.com/api/storesearch/?term={game_name}&cc=us&l=en"
    search_res = requests.get(search_url)

    if search_res.status_code != 200:
        await ctx.send("❌ Failed to contact Steam Store.")
        return

    search_data = search_res.json()
    items = search_data.get("items", [])
    if not items:
        await ctx.send(f"No results found for `{game_name}`.")
        return

    appid = items[0]["id"]
    details_url = f"https://store.steampowered.com/api/appdetails?appids={appid}&cc=us&l=en"
    details_res = requests.get(details_url)

    if details_res.status_code != 200:
        await ctx.send("❌ Could not fetch game details.")
        return

    details = details_res.json().get(str(appid), {}).get("data")
    if not details:
        await ctx.send("⚠️ Game details unavailable.")
        return

    name = details.get("name", "Unknown")
    release = details.get("release_date", {}).get("date", "Unknown")
    is_free = details.get("is_free", False)
    price_info = details.get("price_overview", {})
    price = "Free" if is_free else f"{price_info.get('final_formatted', 'Unknown')}"
    score = details.get("metacritic", {}).get("score", "N/A")
    desc = details.get("short_description", "No description.")
    image = details.get("header_image", "")
    url = f"https://store.steampowered.com/app/{appid}/"

    embed = discord.Embed(title=name, description=desc, color=discord.Color.green(), url=url)
    embed.add_field(name="🗓 Release Date", value=release, inline=True)
    embed.add_field(name="💰 Price", value=price, inline=True)
    embed.add_field(name="📈 Metacritic", value=score, inline=True)
    embed.set_thumbnail(url=image)

    await ctx.send(embed=embed)

#----------ACHIEVMENTS----------#

import matplotlib.pyplot as plt

@bot.command(name="achievements")
async def achievements(ctx, game: str = "btd6"):
    steam_id = user_steam_ids.get(str(ctx.author.id))
    if not steam_id:
        await ctx.send("⚠️ Link your Steam first using `-linksteam`.")
        return

    # Support multiple games ill add more later ig
    game_ids = {
        "btd6": 960090,
        "phas": 739630,
        "tf2": 440,
        "smite": 386360,
        "satisfactory": 526870,
    }

    if game.lower() not in game_ids:
        await ctx.send("❌ Unknown game. Try `btd6`, `phas`, `smite`, `satisfactory`, or `tf2`.")
        return
    appid = game_ids[game.lower()]
    url = f"http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={appid}&key={STEAM_API_KEY}&steamid={steam_id}"
    res = requests.get(url)
    if res.status_code != 200:
        await ctx.send("❌ Failed to fetch achievement data.")
        return

    achievements = res.json().get("playerstats", {}).get("achievements", [])
    if not achievements:
        await ctx.send("❌ No unlocked achievements found.")
        return

    # Filter and sort unlocked achievements by unlock time
    unlocks = sorted([
        datetime.datetime.fromtimestamp(a['unlocktime'])
        for a in achievements if a.get('achieved') == 1 and a.get('unlocktime') > 0
    ])

    if not unlocks:
        await ctx.send("⚠️ No dated achievements found.")
        return

    # Build cumulative graph
    dates = []
    counts = []
    total = 0
    for date in unlocks:
        total += 1
        dates.append(date)
        counts.append(total)

    plt.figure(figsize=(7, 4))
    plt.plot(dates, counts, marker='o', linestyle='-', color='blue')
    plt.title(f"{ctx.author.display_name}'s {game.upper()} Achievement Progress")
    plt.xlabel("Date")
    plt.ylabel("Total Achievements Unlocked")
    plt.grid(True)
    plt.tight_layout()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        filename = tmpfile.name
        plt.savefig(filename)

    plt.close()

    try:
        await ctx.send(file=discord.File(filename))
    finally:
        os.remove(filename)

#--------BTD6------------#
@bot.command(name="btd6")
async def btd6(ctx):
    steam_id = user_steam_ids.get(str(ctx.author.id))
    if not steam_id:
        await ctx.send("⚠️ You haven’t linked your Steam account. Use `-linksteam <steam_id>`.")
        return

    # Get playtime
    url_games = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={STEAM_API_KEY}&steamid={steam_id}&include_appinfo=1&format=json"
    games_res = requests.get(url_games)
    if games_res.status_code != 200:
        await ctx.send("❌ Could not fetch Steam game data.")
        return

    games_data = games_res.json()
    btd6_data = None
    for game in games_data["response"].get("games", []):
        if game["appid"] == 960090:
            btd6_data = game
            break

    if not btd6_data:
        await ctx.send("❌ You don't appear to own Bloons TD 6 on Steam.")
        return

    playtime_hours = round(btd6_data["playtime_forever"] / 60, 1)

    # Get achievements
    url_achievements = f"http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=960090&key={STEAM_API_KEY}&steamid={steam_id}"
    ach_res = requests.get(url_achievements)

    if ach_res.status_code != 200:
        await ctx.send(f"🎈 **BTD6 Stats**\n• Playtime: {playtime_hours} hrs\n⚠️ Achievements unavailable (private or hidden).")
        return

    ach_data = ach_res.json()
    achievements = ach_data.get("playerstats", {}).get("achievements", [])
    unlocked_count = sum(1 for a in achievements if a.get("achieved") == 1)

    msg = f"🎈 **BTD6 Stats for {ctx.author.display_name}**\n"
    msg += f"• 🕒 Playtime: {playtime_hours} hrs\n"
    msg += f"• 🏆 Achievements Unlocked: {unlocked_count} / {len(achievements)}"

    await ctx.send(msg)

#---------CSGO2-------------#

@bot.command(name="cs2")
async def cs2(ctx, steam_id: str = None):
    # Use linked Steam ID
    if not steam_id:
        steam_id = user_steam_ids.get(str(ctx.author.id))

    if not steam_id:
        await ctx.send("⚠️ You haven’t linked your Steam ID. Use `-linksteam <steam_id>` or pass it with `-cs2 <steam_id>`.")
        return

    try:
        stats_url = f"https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/?appid=730&key={STEAM_API_KEY}&steamid={steam_id}"
        res = requests.get(stats_url)
        data = res.json()

        player_stats = data.get("playerstats", {}).get("stats", [])
        if not player_stats:
            await ctx.send("⚠️ Couldn’t retrieve CS2 stats. Make sure your game stats are public.")
            return

        # Extract stats
        stat_dict = {stat['name']: stat['value'] for stat in player_stats}
        total_kills = stat_dict.get("total_kills", 0)
        total_deaths = stat_dict.get("total_deaths", 0)
        kd_ratio = round(total_kills / total_deaths, 2) if total_deaths else "∞"
        matches_played = stat_dict.get("total_matches_played", 0)
        mvps = stat_dict.get("total_mvps", 0)
        headshots = stat_dict.get("total_kills_headshot", 0)

        # Try to get playtime
        try:
            games_url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={STEAM_API_KEY}&steamid={steam_id}&include_played_free_games=1"
            games_res = requests.get(games_url)
            games_data = games_res.json()

            cs2_game = next((g for g in games_data.get("response", {}).get("games", []) if g.get("appid") == 730), None)
            playtime_mins = cs2_game.get("playtime_forever", 0) if cs2_game else 0
            playtime_hours = round(playtime_mins / 60, 1)
        except Exception as e:
            print("CS2 playtime fetch failed:", e)
            playtime_hours = None

        summary_url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_API_KEY}&steamids={steam_id}"
        summary_res = requests.get(summary_url)
        steam_name = steam_id  # fallback

        if summary_res.status_code == 200:
            players = summary_res.json().get("response", {}).get("players", [])
        if players:
            steam_name = players[0].get("personaname", steam_id)

        # Build embed
            embed = discord.Embed(
        title="🎮 CS2 Stats",
        description=f"Stats for **{steam_name}**",
        color=discord.Color.dark_gold()
)

        embed.add_field(name="🧠 Headshots", value=f"{headshots:,}", inline=True)
        embed.add_field(name="🔫 Kills", value=f"{total_kills:,}", inline=True)
        embed.add_field(name="💀 Deaths", value=f"{total_deaths:,}", inline=True)
        embed.add_field(name="⚖️ K/D Ratio", value=str(kd_ratio), inline=True)
        embed.add_field(name="🏆 MVPs", value=f"{mvps:,}", inline=True)
        embed.add_field(name="📊 Matches", value=f"{matches_played:,}", inline=True)

        if playtime_hours is not None:
            embed.add_field(name="⏱ Playtime", value=f"{playtime_hours} hrs", inline=True)
        else:
            embed.add_field(name="⏱ Playtime", value="Unknown (private)", inline=True)

        await ctx.send(embed=embed)

    except Exception as e:
        print("CS2 stats error:", e)
        await ctx.send("❌ Failed to fetch CS2 stats. Steam may be down or the profile might be private.")


#---------R6---------------#
@bot.command(name="r6")
async def r6stats(ctx, username: str):
    from playwright.async_api import async_playwright

    async def scrape_r6_stats(username):
        url = f"https://r6.tracker.network/r6siege/profile/ubi/{username}/overview"

        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    "--no-sandbox",
                    "--disable-setuid-sandbox",
                    "--disable-blink-features=AutomationControlled"
                ]
            )
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                viewport={"width": 1280, "height": 800},
                locale="en-US"
            )
            page = await context.new_page()
            await page.goto(url, timeout=90000)
            await page.wait_for_timeout(10000)

            values = await page.locator("span.stat-value--text").all_inner_texts()

            try:
                rank_text = await page.locator("div.grid span.truncate").first.inner_text()
                rp_text = await page.locator("span.rank-points").first.inner_text()
                rp_full = f"{rp_text} RP"
            except Exception as e:
                print("Rank fetch error:", e)
                rank_text = "Unranked"
                rp_full = "N/A"

            await browser.close()

            return {
                "values": values,
                "rank": rank_text,
                "rp": rp_full
            }

    try:
        result = await scrape_r6_stats(username)
        values = result["values"]
        rank = result["rank"]
        rp = result["rp"]

        def extract_mode_stats(mode):
            if mode in values:
                i = values.index(mode)
                kd = values[i + 1] if i + 1 < len(values) else "?"
                win = values[i + 2] if i + 2 < len(values) else "?"
                return kd, win
            return "?", "?"

        ranked_kd, ranked_win = extract_mode_stats("Ranked")
        standard_kd, standard_win = extract_mode_stats("Standard")
        quick_kd, quick_win = extract_mode_stats("Quick Match")

        embed = discord.Embed(
            title=f"🔫 Rainbow Six Siege Stats: {username}",
            description=f"[View Full Stats](https://r6.tracker.network/r6siege/profile/ubi/{username}/overview)",
            color=discord.Color.blurple()
        )

        embed.add_field(name="🏅 Current Rank", value=f"{rank} ({rp})", inline=False)
        embed.add_field(name="📊 Ranked", value=f"KD: {ranked_kd} | Win Rate: {ranked_win}", inline=False)
        embed.add_field(name="🎯 Standard", value=f"KD: {standard_kd} | Win Rate: {standard_win}", inline=False)
        embed.add_field(name="💥 Quick Match", value=f"KD: {quick_kd} | Win Rate: {quick_win}", inline=False)

        await ctx.send(embed=embed)

    except Exception as e:
        print("R6 scrape error:", e)
        await ctx.send("❌ Failed to fetch R6 stats. Check the username/platform or try again later.")

#---------PHASMOPHOBIA--------#
if os.path.exists(GHOST_JSON_PATH):
    with open(GHOST_JSON_PATH, "r") as f:
        PHAS_GHOSTS = json.load(f)
else:
    PHAS_GHOSTS = {}

@bot.command(name="phas")
async def phas(ctx, *, ghost_name: str = None):
    if not ghost_name:
        await ctx.send("👻 Please specify a ghost name. Example: `-phas hantu`")
        return

    ghost_key = ghost_name.lower().strip()
    ghost = PHAS_GHOSTS.get(ghost_key)

    if not ghost:
        await ctx.send(f"❌ Unknown ghost type: `{ghost_name}`. Check your spelling.")
        return

    embed = discord.Embed(
        title=f"👻 Phasmophobia Ghost Info: {ghost_key.title()}",
        color=discord.Color.dark_teal()
    )
    embed.add_field(name="🔎 Evidence", value=", ".join(ghost["evidence"]), inline=False)
    embed.add_field(name="💪 Strength", value=ghost["strength"], inline=False)
    embed.add_field(name="⚠️ Weakness", value=ghost["weakness"], inline=False)
    embed.add_field(name="🧠 Tips/Fun Facts", value=ghost["info"], inline=False)

    speed = ghost.get("speed", "Unknown")
    embed.add_field(name="🏃 Speed", value=speed, inline=False)

    await ctx.send(embed=embed)

#---------SKYBLOCK----------#
@bot.command(name="skyblock")
async def skyblock(ctx, username: str, profile_name: str = None):
    # Step 1: Get UUID from Mojang
    mojang_url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    mojang_res = requests.get(mojang_url)
    if mojang_res.status_code != 200:
        await ctx.send(f"❌ Could not find Minecraft user `{username}`.")
        return
    uuid = mojang_res.json().get("id")

    # Step 2: Get profiles
    hypixel_url = f"https://api.hypixel.net/v2/skyblock/profiles?key={HYPIXEL_API_KEY}&uuid={uuid}"
    hypixel_res = requests.get(hypixel_url)
    if hypixel_res.status_code != 200 or not hypixel_res.json().get("success"):
        await ctx.send("❌ Failed to fetch Hypixel data.")
        return

    profiles = hypixel_res.json().get("profiles", [])
    if not profiles:
        await ctx.send(f"⚠️ `{username}` has no SkyBlock profiles.")
        return

    # find profile
    selected = None
    if profile_name:
        profile_name = profile_name.lower()
        for profile in profiles:
            if profile.get("cute_name", "").lower() == profile_name:
                selected = profile
                break

    # Fallback: use most recently saved profile
    if not selected:
        def get_last_save(profile):
            return profile.get("members", {}).get(uuid, {}).get("last_save", 0)
        selected = max(profiles, key=get_last_save)

    members = selected.get("members", {})
    uuid_stripped = uuid.replace("-", "").lower()
    member_data = members.get(uuid_stripped, {})
    profile_label = selected.get("cute_name", "Unknown")

    purse = member_data.get("currencies", {}).get("coin_purse", 0)
    bank = selected.get("bank_account", 0)
    fairy_souls = member_data.get("fairy_soul", {}).get("total_collected", 0)

    xp = member_data.get("player_data", {}).get("experience", {})

    combat_level = xp_to_level(xp.get("SKILL_COMBAT", 0))
    farming_level = xp_to_level(xp.get("SKILL_FARMING", 0))
    alchemy_level = xp_to_level(xp.get("SKILL_ALCHEMY", 0))
    mining_level = xp_to_level(xp.get("SKILL_MINING", 0))
    foraging_level = xp_to_level(xp.get("SKILL_FORAGING", 0))
    fishing_level = xp_to_level(xp.get("SKILL_FISHING", 0))
    enchanting_level = xp_to_level(xp.get("SKILL_ENCHANTING", 0))
    taming_level = xp_to_level(xp.get("SKILL_TAMING", 0))
    carpentry_level = xp_to_level(xp.get("SKILL_CARPENTRY", 0))
    social_level = xp_to_level(xp.get("SKILL_SOCIAL", 0))
    runecrafting_level = xp_to_level(xp.get("SKILL_RUNECRAFTING", 0))

    slayer_data = member_data.get("slayer", {}).get("slayer_bosses", {})
    zombie_xp = slayer_data.get("zombie", {}).get("xp", 0)
    spider_xp = slayer_data.get("spider", {}).get("xp", 0)
    wolf_xp = slayer_data.get("wolf", {}).get("xp", 0)

    zombie_level = slayer_xp_to_level(zombie_xp)
    spider_level = slayer_xp_to_level(spider_xp)
    wolf_level = slayer_xp_to_level(wolf_xp)

    embed = discord.Embed(
        title=f"🧱 SkyBlock Stats for {username}",
        description=f"Profile: `{profile_label}`",
        color=discord.Color.gold()
    )
    embed.add_field(name="💰 Purse", value=f"{purse:,.0f} coins", inline=True)
    embed.add_field(name="🏦 Bank", value=f"{bank if isinstance(bank, str) else f'{bank:,.0f}'} coins", inline=True)
    embed.add_field(name="🧚 Fairy Souls", value=str(fairy_souls), inline=True)

    embed.add_field(name="⚔️ Combat", value=str(combat_level), inline=True)
    embed.add_field(name="🌾 Farming", value=str(farming_level), inline=True)
    embed.add_field(name="⛏ Mining", value=str(mining_level), inline=True)
    embed.add_field(name="🪵 Foraging", value=str(foraging_level), inline=True)
    embed.add_field(name="🎣 Fishing", value=str(fishing_level), inline=True)
    embed.add_field(name="📚 Enchanting", value=str(enchanting_level), inline=True)
    embed.add_field(name="🧠 Alchemy", value=str(alchemy_level), inline=True)
    embed.add_field(name="🐕 Taming", value=str(taming_level), inline=True)
    embed.add_field(name="🛠 Carpentry", value=str(carpentry_level), inline=True)
    embed.add_field(name="🧑‍🤝‍🧑 Social", value=str(social_level), inline=True)
    embed.add_field(name="✨ Runecrafting", value=str(runecrafting_level), inline=True)

    embed.add_field(name="🧟 Zombie Slayer", value=f"Level {zombie_level}", inline=True)
    embed.add_field(name="🕷 Spider Slayer", value=f"Level {spider_level}", inline=True)
    embed.add_field(name="🐺 Wolf Slayer", value=f"Level {wolf_level}", inline=True)

    embed.add_field(name="🔗 SkyCrypt", value=f"[View Full Profile](https://sky.shiiyu.moe/stats/{username}/{profile_label})", inline=False)

    await ctx.send(embed=embed)
#-------------Bazaar----------#

def fetch_bazaar_data():
    url = f"https://api.hypixel.net/skyblock/bazaar?key={HYPIXEL_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    return data.get("products", {})

# View with buttons
class BazaarView(discord.ui.View):
    def __init__(self, products, page=0):
        super().__init__(timeout=60)
        self.products = products
        self.page = page
        self.per_page = 10  # Number of items per page (adjust as needed)

        keys = list(products.keys())
        start = page * self.per_page
        end = start + self.per_page
        self.items_list = keys[start:end]

        for item in self.items_list:
            button = discord.ui.Button(label=item[:80], style=discord.ButtonStyle.primary)
            button.callback = self.make_callback(item)
            self.add_item(button)

        if start > 0:
            prev = discord.ui.Button(label="⬅️ Prev", style=discord.ButtonStyle.secondary)
            prev.callback = self.make_nav_callback(page - 1)
            self.add_item(prev)

        if end < len(keys):
            next = discord.ui.Button(label="➡️ Next", style=discord.ButtonStyle.secondary)
            next.callback = self.make_nav_callback(page + 1)
            self.add_item(next)

    def make_callback(self, item_name):
        async def callback(interaction: discord.Interaction):
            item_data = self.products.get(item_name, {}).get("quick_status", {})
            buy_price = item_data.get("buyPrice", 0)
            sell_price = item_data.get("sellPrice", 0)
            buy_volume = item_data.get("buyVolume", 0)
            sell_volume = item_data.get("sellVolume", 0)

            embed = discord.Embed(
                title=f"📊 Bazaar Item: {item_name}",
                description=(
                    f"**Buy Price:** {buy_price:.2f}\n"
                    f"**Sell Price:** {sell_price:.2f}\n"
                    f"**Buy Volume:** {buy_volume}\n"
                    f"**Sell Volume:** {sell_volume}"
                ),
                color=discord.Color.blue()
            )
            # Add a placeholder image; if you have real item icons, replace this with their URLs!
            embed.set_thumbnail(url="https://hypixel.net/styles/hypixel-v2/images/favicon-96x96.png")
            await interaction.response.edit_message(embed=embed, view=self)
        return callback

    def make_nav_callback(self, target_page):
        async def callback(interaction: discord.Interaction):
            new_view = BazaarView(self.products, page=target_page)
            embed = discord.Embed(
                title=f"🛒 Hypixel SkyBlock Bazaar (Page {target_page + 1})",
                description="Click an item button to view details.",
                color=discord.Color.gold()
            )
            await interaction.response.edit_message(embed=embed, view=new_view)
        return callback

# Command
@bot.command(name="bz")
async def bz(ctx):
    products = fetch_bazaar_data()
    if not products:
        await ctx.send("❌ Failed to fetch Bazaar data.")
        return

    embed = discord.Embed(
        title="🛒 Hypixel SkyBlock Bazaar",
        description="Click an item button to view details.",
        color=discord.Color.gold()
    )
    view = BazaarView(products)
    await ctx.send(embed=embed, view=view)

bot.run(DISCOD_BOT_TOKEN)
