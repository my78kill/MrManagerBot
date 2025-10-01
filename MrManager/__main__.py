# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.


# ============================================================
# FILE: MrManager/__main__.py
# ============================================================
from .bot import MrManagerBot
from .config import Config
from .logger import logger

def main():
    """Main entry point for the bot."""
    try:
        # Validate configuration
        Config.validate()
        
        # Create and run bot
        logger.info("⚙️ Initializing MrManager Bot...")
        bot = MrManagerBot()
        bot.run()
        
    except ValueError as e:
        logger.error(f"❌ Configuration error: {e}")
    except KeyboardInterrupt:
        logger.info("⚠️ Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}", exc_info=True)

if __name__ == "__main__":
    main()