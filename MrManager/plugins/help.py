# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.


# ============================================================
# FILE: MrManager/plugins/help.py
# ============================================================
from pyrogram import Client, filters
from pyrogram.types import Message
from ..helpers.decorators import log_command
from ..logger import logger

@Client.on_message(filters.command("help"))
@log_command
async def help_command(client: Client, message: Message):
    """Help command handler."""
    help_text = (
        "📚 **Available Commands** 📚\n\n"
        
        "**👥 Group Management:**\n"
        "• `/kick` - Kick a user from the group\n"
        "• `/ban` - Ban a user from the group\n"
        "• `/unban` - Unban a user\n"
        "• `/mute` - Mute a user\n"
        "• `/unmute` - Unmute a user\n"
        "• `/pin` - Pin a message (reply to message)\n"
        "• `/unpin` - Unpin a message (reply to message)\n"
        "• `/unpinall` - Unpin all pinned messages\n"
        "• `/promote` - Promote user to admin\n"
        "• `/demote` - Demote admin to member\n"
        "• `/del` - Delete a message (reply to message)\n"
        "• `/purge` - Delete messages (reply to start message)\n\n"
        
        "**ℹ️ Information:**\n"
        "• `/info` - Get user/chat information\n"
        "• `/id` - Get user/chat ID\n"
        "• `/stats` - Get chat statistics\n"
        "• `/admins` - List all admins\n\n"
        
        "**⚙️ Chat Settings:**\n"
        "• `/lock` - Lock chat (members can't send messages)\n"
        "• `/unlock` - Unlock chat\n"
        "• `/setphoto` - Set chat photo (reply to photo)\n"
        "• `/settitle` - Set chat title\n"
        "• `/setdesc` - Set chat description\n\n"
        
        "**Note:** Admin commands require bot to have admin privileges!\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "Developed by @dotenv with <3"
    )
    await message.reply_text(help_text)
    logger.debug(f"Help command sent to user {message.from_user.id}")