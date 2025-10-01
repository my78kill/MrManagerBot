# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.

# ============================================================
# FILE: MrManager/plugins/moderation.py
# ============================================================
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from ..helpers.decorators import admin_only, group_only, log_command
from ..logger import logger

@Client.on_message(filters.command("kick") & filters.group)
@log_command
@group_only
@admin_only
async def kick_user(client: Client, message: Message):
    """Kick a user from the group."""
    if not message.reply_to_message:
        await message.reply_text("Reply to a user's message to kick them!")
        return
    
    user_id = message.reply_to_message.from_user.id
    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await client.unban_chat_member(message.chat.id, user_id)
        await message.reply_text(f"✅ User kicked successfully!")
        logger.info(f"User {user_id} kicked from chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error kicking user: {e}")

@Client.on_message(filters.command("ban") & filters.group)
@log_command
@group_only
@admin_only
async def ban_user(client: Client, message: Message):
    """Ban a user from the group."""
    if not message.reply_to_message:
        await message.reply_text("Reply to a user's message to ban them!")
        return
    
    user_id = message.reply_to_message.from_user.id
    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply_text(f"✅ User banned successfully!")
        logger.info(f"User {user_id} banned from chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error banning user: {e}")

@Client.on_message(filters.command("unban") & filters.group)
@log_command
@group_only
@admin_only
async def unban_user(client: Client, message: Message):
    """Unban a user from the group."""
    if not message.reply_to_message:
        await message.reply_text("Reply to a user's message to unban them!")
        return
    
    user_id = message.reply_to_message.from_user.id
    try:
        await client.unban_chat_member(message.chat.id, user_id)
        await message.reply_text(f"✅ User unbanned successfully!")
        logger.info(f"User {user_id} unbanned from chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error unbanning user: {e}")

@Client.on_message(filters.command("mute") & filters.group)
@log_command
@group_only
@admin_only
async def mute_user(client: Client, message: Message):
    """Mute a user in the group."""
    if not message.reply_to_message:
        await message.reply_text("Reply to a user's message to mute them!")
        return
    
    user_id = message.reply_to_message.from_user.id
    try:
        await client.restrict_chat_member(
            message.chat.id, 
            user_id,
            ChatPermissions()
        )
        await message.reply_text(f"✅ User muted successfully!")
        logger.info(f"User {user_id} muted in chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error muting user: {e}")

@Client.on_message(filters.command("unmute") & filters.group)
@log_command
@group_only
@admin_only
async def unmute_user(client: Client, message: Message):
    """Unmute a user in the group."""
    if not message.reply_to_message:
        await message.reply_text("Reply to a user's message to unmute them!")
        return
    
    user_id = message.reply_to_message.from_user.id
    try:
        await client.restrict_chat_member(
            message.chat.id, 
            user_id,
            ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True
            )
        )
        await message.reply_text(f"✅ User unmuted successfully!")
        logger.info(f"User {user_id} unmuted in chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error unmuting user: {e}")

@Client.on_message(filters.command("del") & filters.group)
@log_command
@group_only
@admin_only
async def delete_message(client: Client, message: Message):
    """Delete a message."""
    if not message.reply_to_message:
        await message.reply_text("Reply to a message to delete it!")
        return
    
    try:
        await message.reply_to_message.delete()
        await message.delete()
        logger.info(f"Message deleted in chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error deleting message: {e}")

@Client.on_message(filters.command("purge") & filters.group)
@log_command
@group_only
@admin_only
async def purge_messages(client: Client, message: Message):
    """Purge messages from replied message to current message."""
    if not message.reply_to_message:
        await message.reply_text("Reply to the starting message to purge from there!")
        return
    
    msg_ids = list(range(message.reply_to_message.id, message.id + 1))
    try:
        await client.delete_messages(message.chat.id, msg_ids)
        status = await message.reply_text(f"🗑️ Purged {len(msg_ids)} messages!")
        logger.info(f"Purged {len(msg_ids)} messages in chat {message.chat.id}")
        await status.delete()
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error purging messages: {e}")
