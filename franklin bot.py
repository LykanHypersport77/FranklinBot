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

if os.path.exists(LASTFM_LINK_FILE):
    with open(LASTFM_LINK_FILE, "r") as f:
        lastfm_users = json.load(f)
else:
    lastfm_users = {}

# Save updated links
def save_lastfm_links():
    with open(LASTFM_LINK_FILE, "w") as f:
        json.dump(lastfm_users, f)

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
    folder = r"C:\Users\pkpq4127\Downloads\Franklin Bot\pics\benno pics"
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No benno pics found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending benno image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="twink")
async def twink(ctx):
    folder = r"C:\Users\pkpq4127\Downloads\Franklin Bot\pics\twink"
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No twink pics found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending twink image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="varun")
async def varun(ctx):
    folder = r"C:\Users\pkpq4127\Downloads\Franklin Bot\pics\varun"
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No varun pics found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending varun image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="twins")
async def twins(ctx):
    folder = r"C:\Users\pkpq4127\Downloads\Franklin Bot\pics\twins"
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No twin pics found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending twins image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="nate")
async def nate(ctx):
    folder = r"C:\Users\pkpq4127\Downloads\Franklin Bot\pics\nate"
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No nate pics found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending nate image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="oppshoota")
async def oppshoota(ctx):
    folder = r"C:\Users\pkpq4127\Downloads\Franklin Bot\pics\oppshoota"
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No opps found")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending shoota image:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="meow")
async def meow(ctx):
    folder = r"C:\Users\pkpq4127\Downloads\Franklin Bot\pics\sophie pics"
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
    folder = r"C:\Users\pkpq4127\Downloads\Franklin Bot\pics\franklin pics"
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
    folder = r"C:\Users\pkpq4127\Downloads\Franklin Bot\pics\big booty latina"
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No big booty latinas found.")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending big booty latinas:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="rangrang")
async def rangrang(ctx):
    folder = r"C:\Users\pkpq4127\Downloads\Franklin Bot\pics\rangrang"
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("No chinese found.")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("Sending chinese pics:", image_path)
    await ctx.send(file=discord.File(image_path))

@bot.command(name="jesus")
async def jesus(ctx):
    folder = r"C:\Users\pkpq4127\Downloads\Franklin Bot\pics\jesus"
    images = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    if not images:
        await ctx.send("jesus is dead")
        return
    image_path = os.path.join(folder, random.choice(images))
    print("reviving jesus:", image_path)
    await ctx.send(file=discord.File(image_path))

#----------LASTFM--------#
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

    msg = f"🎶 **Top Tracks This Week for `{username}`:**\n"
    for i, track in enumerate(tracks):
        name = track["name"]
        artist = track["artist"]["name"]
        playcount = track["playcount"]
        msg += f"{i+1}. {name} – {artist} ({playcount} plays)\n"

    await ctx.send(msg)

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
        display_name = target_username  # Use queried Last.fm name
    else:
        if user_id not in user_links:
            await ctx.send("⚠️ You haven’t linked your Last.fm account. Use `-linkfm <username>`.")
            return
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

    if now_playing:
        msg = f"🎧 {display_name} is currently listening to:\n**{title}** by *{artist}* (Album: {album})"
    else:
        msg = f"🎶 Last played by {display_name}:\n**{title}** by *{artist}* (Album: {album})"
    await ctx.send(msg)

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
        await ctx.send("You haven’t played any games in the last 2 weeks.")
        return

    msg = "**🎮 Your last 2 weeks of Steam playtime:**\n"
    for game in games:
        name = game['name']
        hours = round(game.get('playtime_2weeks', 0) / 60, 1)
        msg += f"• {name}: {hours} hrs\n"

    await ctx.send(msg)

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
        await ctx.send("You don’t seem to own any games.")
        return

    sorted_games = sorted(games, key=lambda g: g.get("playtime_forever", 0), reverse=True)
    top_games = sorted_games[:5]  # Top 5

    msg = "**🏆 Your Top Played Games:**\n"
    for game in top_games:
        name = game['name']
        hours = round(game.get('playtime_forever', 0) / 60, 1)
        msg += f"• {name}: {hours} hrs\n"

    await ctx.send(msg)

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

        msg = f"**🎮 CS2 Stats for `<{steam_id}>`:**\n"
        msg += f"• 🧠 Headshots: {headshots:,}\n"
        msg += f"• 🔫 Total Kills: {total_kills:,}\n"
        msg += f"• 💀 Total Deaths: {total_deaths:,}\n"
        msg += f"• ⚖️ K/D Ratio: {kd_ratio}\n"
        msg += f"• 🏆 MVPs: {mvps:,}\n"
        msg += f"• 📊 Matches Played: {matches_played:,}"
        if playtime_hours is not None:
            msg += f"\n• ⏱ Playtime: {playtime_hours} hrs"
        else:
            msg += f"\n• ⏱ Playtime: Unknown (profile may be private)"

        await ctx.send(msg)

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
            # Launch headless but spoof as a real browser
            browser = await p.chromium.launch(
                headless=True,
                args=["--disable-blink-features=AutomationControlled"]
            )
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                viewport={"width": 1280, "height": 800},
                locale="en-US"
            )
            page = await context.new_page()
            await page.goto(url, timeout=20000)

            await page.wait_for_timeout(2000)

            values = await page.locator("span.stat-value--text").all_inner_texts()

            # Extract rank info
            try:
                # Check if a ranked element exists
                rank_elements = page.locator("div.grid span.truncate")
                rp_elements = page.locator("span.rank-points")

                rank_count = await rank_elements.count()
                rp_count = await rp_elements.count()

                if rank_count > 0 and rp_count > 0:
                    rank_text = await rank_elements.first.inner_text()
                    rp_text = await rp_elements.first.inner_text()
                    rp_full = f"{rp_text} RP"
                else:
                    rank_text = "Unranked"
                    rp_full = "N/A"
            except Exception as e:
                print("Rank fetch error:", e)
                rank_text = "Unranked"
                rp_full = "N/A"

            rank_text = await page.locator("div.grid span.truncate").first.inner_text()
            rp_text = await page.locator("span.rank-points").first.inner_text()
            rp_full = f"{rp_text} RP"

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

        # build message
        msg = f"**🔫 Rainbow Six Siege Stats for `{username}`**\n"
        msg += f"🏅 **Current Rank**: {rank} ({rp})\n\n"
        msg += f"📊 **Ranked**\n• KD: {ranked_kd} | Win Rate: {ranked_win}\n"
        msg += f"🎯 **Standard**\n• KD: {standard_kd} | Win Rate: {standard_win}\n"
        msg += f"💥 **Quick Match**\n• KD: {quick_kd} | Win Rate: {quick_win}\n"
        msg += f"\n🔗 [Full Stats](https://r6.tracker.network/r6siege/profile/ubi/{username}/overview)"

        await ctx.send(msg)

    except Exception as e:
        print("R6 scrape error:", e)
        await ctx.send("❌ Failed to fetch R6 stats. Check the username/platform or try again later.")

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

    # networth
    # try:
    #     skycrypt_url = f"https://sky.shiiyu.moe/api/v2/profile/{uuid_stripped}"
    #     skycrypt_res = requests.get(skycrypt_url)
    #     print("SkyCrypt raw response:", skycrypt_res.status_code, skycrypt_res.text[:200])  # Print first 200 chars
    #     skycrypt_data = skycrypt_res.json()
    #     networth = skycrypt_data.get("networth", {}).get("networth", 0)
    # except Exception as e:
    #     print("Failed to get SkyCrypt net worth:", e)
    #     networth = None

    # Stats
    purse = member_data.get("currencies", {}).get("coin_purse", 0)
    bank = selected.get("bank_account", 0)
    fairy_souls = member_data.get("fairy_soul", {}).get("total_collected", 0)

    # Skills
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

    # Slayer
    slayer_data = member_data.get("slayer", {}).get("slayer_bosses", {})

    zombie_xp = slayer_data.get("zombie", {}).get("xp", 0)
    spider_xp = slayer_data.get("spider", {}).get("xp", 0)
    wolf_xp = slayer_data.get("wolf", {}).get("xp", 0)

    zombie_level = slayer_xp_to_level(zombie_xp)
    spider_level = slayer_xp_to_level(spider_xp)
    wolf_level = slayer_xp_to_level(wolf_xp)

    # Build message
    msg = f"**🧱 SkyBlock Stats for `{username}` (Profile: {profile_label})**\n"
    msg += f"• 💰 Purse: {purse:,.0f} coins\n"
    msg += f"• 🏦 Bank: {bank if isinstance(bank, str) else f'{bank:,.0f}'} coins\n"
    msg += f"• 🧚 Fairy Souls: {fairy_souls}\n"
    msg += f"• ⚔️ Combat Level: {combat_level}\n"
    msg += f"• 🌾 Farming Level: {farming_level}\n"
    msg += f"• ⛏ Mining Level: {mining_level}\n"
    msg += f"• 🪵 Foraging Level: {foraging_level}\n"
    msg += f"• 🎣 Fishing Level: {fishing_level}\n"
    msg += f"• 📚 Enchanting Level: {enchanting_level}\n"
    msg += f"• 🧠 Alchemy Level: {alchemy_level}\n"
    msg += f"• 🐕 Taming Level: {taming_level}\n"
    msg += f"• 🛠 Carpentry Level: {carpentry_level}\n"
    msg += f"• 🧑‍🤝‍🧑 Social Level: {social_level}\n"
    msg += f"• ✨ Runecrafting Level: {runecrafting_level}\n"
    msg += f"• 🧟 Zombie Slayer: Level {zombie_level}\n"
    msg += f"• 🕷 Spider Slayer: Level {spider_level}\n"
    msg += f"• 🐺 Wolf Slayer: Level {wolf_level}\n"
    msg += f"🔗 View full profile: https://sky.shiiyu.moe/stats/{username}/{profile_label}\n"

    await ctx.send(msg)

bot.run(DISCOD_BOT_TOKEN)
