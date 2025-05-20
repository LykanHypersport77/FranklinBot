import asyncio
from playwright.async_api import async_playwright

async def scrape_r6_stats(username):
    url = f"https://r6.tracker.network/r6siege/profile/ubi/{username}/overview"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        page = await browser.new_page()
        await page.goto(url, timeout=90000)

        await page.wait_for_timeout(10000)  # wait 10 sec for Cloudflare & JS

        # Adjust these based on what you find in HTML
        labels = await page.locator("span.stat__label").all_inner_texts()
        values = await page.locator("span.stat-value--text").all_inner_texts()

        # Debug what we got
        print("Labels:", labels)
        print("Values:", values)

        stat_dict = dict(zip(labels, values))

        stats = {
            "Level": stat_dict.get("Level", "?"),
            "Playtime": stat_dict.get("Playtime", "?"),
            "Kills": stat_dict.get("Kills", "?"),
            "Deaths": stat_dict.get("Deaths", "?"),
            "K/D": stat_dict.get("KD", "?"),
            "Wins": stat_dict.get("Wins", "?"),
            "Losses": stat_dict.get("Losses", "?"),
            "Win Rate": stat_dict.get("Win Rate", "?"),
            "HS%": stat_dict.get("HS%", "?"),
            "Avg Kills": stat_dict.get("Avg Kills", "?"),
        }

        await browser.close()
        return stats

# Run it once
if __name__ == "__main__":
    username = "Roudro77"
    stats = asyncio.run(scrape_r6_stats(username))
    print(stats)
