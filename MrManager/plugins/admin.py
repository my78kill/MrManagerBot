# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.


# ============================================================
# FILE: MrManager/plugins/admin.py
# ============================================================
from pyrogram import Client, filters
from pyrogram.types import Message
from ..helpers.decorators import admin_only, group_only, log_command
from ..logger import logger

@Client.on_message(filters.command("pin") & filters.group)
@log_command
@group_only
@admin_only
async def pin_message(client: Client, message: Message):
    """Pin a message in the group."""
    if not message.reply_to_message:
        await message.reply_text("Reply to a message to pin it!")
        return
    
    try:
        await client.pin_chat_message(message.chat.id, message.reply_to_message.id)
        await message.reply_text("📌 Message pinned successfully!")
        logger.info(f"Message pinned in chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error pinning message: {e}")

@Client.on_message(filters.command("unpin") & filters.group)
@log_command
@group_only
@admin_only
async def unpin_message(client: Client, message: Message):
    """Unpin a message in the group."""
    try:
        if message.reply_to_message:
            await client.unpin_chat_message(message.chat.id, message.reply_to_message.id)
            await message.reply_text("📍 Message unpinned successfully!")
        else:
            await client.unpin_chat_message(message.chat.id)
            await message.reply_text("📍 Last pinned message unpinned!")
        logger.info(f"Message unpinned in chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error unpinning message: {e}")

@Client.on_message(filters.command("unpinall") & filters.group)
@log_command
@group_only
@admin_only
async def unpin_all_messages(client: Client, message: Message):
    """Unpin all messages in the group."""
    try:
        await client.unpin_all_chat_messages(message.chat.id)
        await message.reply_text("📍 All pinned messages unpinned successfully!")
        logger.info(f"All messages unpinned in chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error unpinning all messages: {e}")

@Client.on_message(filters.command("promote") & filters.group)
@log_command
@group_only
@admin_only
async def promote_user(client: Client, message: Message):
    """Promote a user to admin."""
    if not message.reply_to_message:
        await message.reply_text("Reply to a user's message to promote them!")
        return
    
    user_id = message.reply_to_message.from_user.id
    try:
        await client.promote_chat_member(
            message.chat.id,
            user_id,
            privileges={
                "can_manage_chat": True,
                "can_delete_messages": True,
                "can_manage_video_chats": True,
                "can_restrict_members": True,
                "can_promote_members": False,
                "can_change_info": True,
                "can_invite_users": True,
                "can_pin_messages": True
            }
        )
        await message.reply_text("⬆️ User promoted to admin successfully!")
        logger.info(f"User {user_id} promoted in chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error promoting user: {e}")

@Client.on_message(filters.command("demote") & filters.group)
@log_command
@group_only
@admin_only
async def demote_user(client: Client, message: Message):
    """Demote an admin to member."""
    if not message.reply_to_message:
        await message.reply_text("Reply to an admin's message to demote them!")
        return
    
    user_id = message.reply_to_message.from_user.id
    try:
        await client.promote_chat_member(
            message.chat.id,
            user_id,
            privileges={
                "can_manage_chat": False,
                "can_delete_messages": False,
                "can_manage_video_chats": False,
                "can_restrict_members": False,
                "can_promote_members": False,
                "can_change_info": False,
                "can_invite_users": False,
                "can_pin_messages": False
            }
        )
        await message.reply_text("⬇️ Admin demoted to member successfully!")
        logger.info(f"User {user_id} demoted in chat {message.chat.id}")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        logger.error(f"Error demoting user: {e}")