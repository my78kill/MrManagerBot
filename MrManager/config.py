# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.


# ============================================================
# FILE: MrManager/config.py
# ============================================================
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Bot configuration from environment variables."""
    
    # Bot credentials
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    
    # Logging configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    
    # Bot settings
    BOT_NAME = "MrManager Bot"
    BOT_USERNAME = os.getenv("BOT_USERNAME", "mrmanager_bot")
    
    # Sudo users (comma-separated user IDs)
    SUDO_USERS = [
        int(x) for x in os.getenv("SUDO_USERS", "").split(",") if x.strip()
    ]
    
    @staticmethod
    def validate():
        """Validate required configuration."""
        if not Config.API_ID or Config.API_ID == 0:
            raise ValueError("API_ID is required in .env file")
        if not Config.API_HASH:
            raise ValueError("API_HASH is required in .env file")
        if not Config.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is required in .env file")