# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.


# ============================================================
# FILE: MrManager/plugins/settings.py
# ============================================================
import os
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from ..helpers.decorators import admin_only, group_only, log_command
from ..logger import logger

@Client.on_message(filters.command("lock") & filters.group)
@log_command
@group_only
@admin_only
async def lock_chat(client: Client, message: Message):
    """Lock the chat so only admins can send messages."""
    try:
        await client.set_chat_permissions(message.chat.id, ChatPermissions())
        await message.reply_text("🔒 Chat locked! Only admins can send messages now.")
        logger.info(f"Chat {message.chat.id} locked")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error locking chat: {e}")

@Client.on_message(filters.command("unlock") & filters.group)
@log_command
@group_only
@admin_only
async def unlock_chat(client: Client, message: Message):
    """Unlock the chat so members can send messages."""
    try:
        await client.set_chat_permissions(
            message.chat.id,
            ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_send_polls=True,
                can_invite_users=True,
                can_pin_messages=True
            )
        )
        await message.reply_text("🔓 Chat unlocked! Members can send messages now.")
        logger.info(f"Chat {message.chat.id} unlocked")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error unlocking chat: {e}")

@Client.on_message(filters.command("setphoto") & filters.group)
@log_command
@group_only
@admin_only
async def set_chat_photo(client: Client, message: Message):
    """Set chat photo."""
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply_text("Reply to a photo to set it as chat photo!")
        return
    
    try:
        photo = await message.reply_to_message.download()
        await client.set_chat_photo(message.chat.id, photo=photo)
        await message.reply_text("🖼️ Chat photo updated successfully!")
        os.remove(photo)
        logger.info(f"Chat photo updated for chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error setting chat photo: {e}")

@Client.on_message(filters.command("settitle") & filters.group)
@log_command
@group_only
@admin_only
async def set_chat_title(client: Client, message: Message):
    """Set chat title."""
    if len(message.command) < 2:
        await message.reply_text("Usage: /settitle <new title>")
        return
    
    title = message.text.split(None, 1)[1]
    try:
        await client.set_chat_title(message.chat.id, title)
        await message.reply_text(f"📝 Chat title updated to: {title}")
        logger.info(f"Chat title updated for chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error setting chat title: {e}")

@Client.on_message(filters.command("setdesc") & filters.group)
@log_command
@group_only
@admin_only
async def set_chat_desc(client: Client, message: Message):
    """Set chat description."""
    if len(message.command) < 2:
        await message.reply_text("Usage: /setdesc <new description>")
        return
    
    desc = message.text.split(None, 1)[1]
    try:
        await client.set_chat_description(message.chat.id, desc)
        await message.reply_text("📄 Chat description updated successfully!")
        logger.info(f"Chat description updated for chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error setting chat description: {e}")