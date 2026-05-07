from config import Config
from pyrogram import Client as bot, idle
import asyncio
import logging
from aiohttp import web

logging.basicConfig(
    level=logging.INFO,    
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
LOGGER = logging.getLogger(__name__)
LOGGER.info("Live log streaming to telegram.")

plugins = dict(root="plugins")

async def health_check(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    LOGGER.info("Health check server started on port 8080")

if __name__ == "__main__":
    bot = bot(
        "Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=plugins,
        workers=10,
    )
    
    async def main():
        await bot.start()
        # Start the health check server for Render
        await start_web_server()
        
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started --->")
        for user_id in Config.AUTH_USERS:
            try:
                await bot.send_message(chat_id=user_id, text=f"__Congrats! You Are DRM member ... if You get any error then contact me -  {Config.CREDIT}__ ")
            except Exception as e:
                LOGGER.error(f"Failed to send message to user {user_id}: {e}")
                continue
        await idle()
        
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info("<--- Bot Stopped --->")
