# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.

# ============================================================
# FILE: MrManager/plugins/start.py
# ============================================================
from pyrogram import Client, filters
from pyrogram.types import Message
from ..helpers.decorators import private_only, log_command
from ..logger import logger

@Client.on_message(filters.command("start") & filters.private)
@log_command
@private_only
async def start_command(client: Client, message: Message):
    """Start command handler."""
    welcome_text = (
        "🎉 **Welcome to MrManager Bot!** 🎉\n\n"
        "I'm here to help you manage your groups and channels with ease!\n\n"
        "✨ **Features:**\n"
        "• Group Management (kick, ban, mute, pin, etc.)\n"
        "• Channel Management (post, edit, delete)\n"
        "• User Info & Statistics\n\n"
        "Use /help to see all available commands.\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "Developed by @dotenv with <3"
    )
    await message.reply_text(welcome_text)
    logger.debug(f"Start command sent to user {message.from_user.id}")