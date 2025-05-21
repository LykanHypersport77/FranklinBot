import discord
from discord.ext import commands
import random
import requests
import json
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="-", intents=intents)

STEAM_API_KEY = os.getenv("STEAM_API_KEY")
DISCOD_BOT_TOKEN = os.getenv("DISCOD_BOT_TOKEN")
HYPIXEL_API_KEY = os.getenv("HYPIXEL_API_KEY")
SPOTIFY_API_KEY = os.getenv("SPOTIFY_API_KEY")

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
    if bot.user.mentioned_in(message) and not message.author.bot:
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


#----------SPOTIFY--------#
@bot.command(name="linkspotify")
async def linkspotify(ctx):
    user_id = str(ctx.author.id)
    link = f"http://localhost:8888/login/{user_id}"
    await ctx.author.send(f"🎧 Click to link your Spotify account:\n{link}")
    await ctx.send("📩 Check your DMs to link Spotify!")


@bot.command(name="spotify")
async def spotify(ctx):
    user_id = str(ctx.author.id)

    # Load tokens
    with open("spotify_tokens.json", "r") as f:
        token_store = json.load(f)

    if user_id not in token_store:
        await ctx.send("❌ You haven't linked Spotify. Use `-linkspotify` first.")
        return

    token_info = token_store[user_id]

    sp = spotipy.Spotify(auth=token_info['access_token'])

    try:
        top_tracks = sp.current_user_top_tracks(limit=5, time_range='short_term')
    except spotipy.exceptions.SpotifyException:
        await ctx.send("❌ Your token expired. Please `-linkspotify` again.")
        return

    msg = "🎶 **Your Top Tracks This Week:**\n"
    total_duration = 0

    for i, item in enumerate(top_tracks['items']):
        name = item['name']
        artist = item['artists'][0]['name']
        duration_ms = item['duration_ms']
        total_duration += duration_ms
        msg += f"{i+1}. {name} – {artist}\n"

    hours = round(total_duration / 1000 / 60 / 60, 2)
    msg += f"\n⏱ Estimated Listening Time: **{hours} hrs**"

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

#---------CSGO2-------------#
@bot.command(name="cs2")
async def cs2(ctx, steam_id: str = None):
    # Use linked Steam ID if available
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

        # Extract some common stats
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
            await page.goto(url, timeout=90000)

            # Let JS and Cloudflare load content
            await page.wait_for_timeout(2000)

            # Extract values (KD, Win Rate etc.)
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

        # Safely extract mode stats
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

        # Format message
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

    # Step 3: Find matching profile
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

