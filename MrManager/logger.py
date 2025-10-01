# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.



# ============================================================
# FILE: MrManager/logger.py
# ============================================================
import logging
import sys
from .config import Config

def setup_logger():
    """Setup logging configuration."""
    
    # Create logger
    logger = logging.getLogger("MrManager")
    
    # Set log level from config
    log_level = getattr(logging, Config.LOG_LEVEL, logging.INFO)
    logger.setLevel(log_level)
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    
    # Create formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(console_handler)
    
    # Set Pyrogram logger level
    pyrogram_logger = logging.getLogger("pyrogram")
    pyrogram_logger.setLevel(logging.WARNING)
    
    return logger

# Create global logger instance
logger = setup_logger()