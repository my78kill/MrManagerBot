# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.

# ============================================================
# FILE: MrManager/plugins/info.py
# ============================================================
from pyrogram import Client, filters
from pyrogram.types import Message
from ..helpers.decorators import log_command, group_only
from ..logger import logger

@Client.on_message(filters.command("info"))
@log_command
async def info_command(client: Client, message: Message):
    """Get user information."""
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        user = message.from_user
    
    info_text = (
        f"**👤 User Information**\n\n"
        f"**Name:** {user.first_name} {user.last_name or ''}\n"
        f"**Username:** @{user.username or 'None'}\n"
        f"**User ID:** `{user.id}`\n"
        f"**Is Bot:** {'Yes ✅' if user.is_bot else 'No ❌'}\n"
        f"**Is Premium:** {'Yes 🌟' if user.is_premium else 'No'}\n"
    )
    await message.reply_text(info_text)
    logger.debug(f"Info sent for user {user.id}")

@Client.on_message(filters.command("id"))
@log_command
async def id_command(client: Client, message: Message):
    """Get user/chat ID."""
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        text = f"**User ID:** `{user_id}`"
    else:
        text = f"**Your ID:** `{message.from_user.id}`\n**Chat ID:** `{message.chat.id}`"
    
    await message.reply_text(text)
    logger.debug(f"ID command used in chat {message.chat.id}")

@Client.on_message(filters.command("stats") & filters.group)
@log_command
@group_only
async def stats_command(client: Client, message: Message):
    """Get chat statistics."""
    try:
        chat = await client.get_chat(message.chat.id)
        member_count = await client.get_chat_members_count(message.chat.id)
        
        stats_text = (
            f"**📊 Chat Statistics**\n\n"
            f"**Chat Name:** {chat.title}\n"
            f"**Chat ID:** `{chat.id}`\n"
            f"**Type:** {chat.type}\n"
            f"**Members:** {member_count}\n"
            f"**Username:** @{chat.username or 'None'}\n"
        )
        await message.reply_text(stats_text)
        logger.debug(f"Stats sent for chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error getting stats: {e}")

@Client.on_message(filters.command("admins") & filters.group)
@log_command
@group_only
async def admins_list(client: Client, message: Message):
    """List all admins in the group."""
    try:
        admins = []
        async for member in client.get_chat_members(message.chat.id, filter="administrators"):
            if member.user.is_bot:
                admins.append(f"🤖 [{member.user.first_name}](tg://user?id={member.user.id})")
            else:
                admins.append(f"👤 [{member.user.first_name}](tg://user?id={member.user.id})")
        
        admin_text = "**👥 Chat Administrators:**\n\n" + "\n".join(admins)
        await message.reply_text(admin_text)
        logger.debug(f"Admin list sent for chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error getting admin list: {e}")