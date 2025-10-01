# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.


# ============================================================
# FILE: MrManager/bot.py
# ============================================================
from pyrogram import Client
from .config import Config
from .logger import logger

class MrManagerBot(Client):
    """Custom bot client with enhanced features."""
    
    def __init__(self):
        super().__init__(
            name="mrmanager_bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="MrManager.plugins"),
            workers=4
        )
        
    async def start(self):
        """Start the bot."""
        await super().start()
        me = await self.get_me()
        logger.info(f"🚀 Bot started as @{me.username}")
        logger.info(f"📝 Log level: {Config.LOG_LEVEL}")
        
    async def stop(self):
        """Stop the bot."""
        await super().stop()
        logger.info("🛑 Bot stopped")