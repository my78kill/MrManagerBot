# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.

# ============================================================
# FILE: MrManager/helpers/decorators.py
# ============================================================
from functools import wraps
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus, ChatType
from ..config import Config
from ..logger import logger

def admin_only(func):
    """Decorator to restrict command to admins only."""
    @wraps(func)
    async def wrapper(client, message: Message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        
        try:
            member = await client.get_chat_member(chat_id, user_id)
            if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                await message.reply_text("❌ You need to be an admin to use this command!")
                return
        except Exception as e:
            logger.error(f"Error checking admin status: {e}")
            await message.reply_text("❌ Error checking permissions!")
            return
        
        return await func(client, message)
    return wrapper

def sudo_only(func):
    """Decorator to restrict command to sudo users only."""
    @wraps(func)
    async def wrapper(client, message: Message):
        user_id = message.from_user.id
        
        if user_id not in Config.SUDO_USERS:
            await message.reply_text("❌ This command is restricted to sudo users only!")
            logger.warning(f"Unauthorized sudo command attempt by user {user_id}")
            return
        
        return await func(client, message)
    return wrapper

def group_only(func):
    """Decorator to restrict command to groups only."""
    @wraps(func)
    async def wrapper(client, message: Message):
        if message.chat.type == ChatType.PRIVATE:
            await message.reply_text("❌ This command can only be used in groups!")
            return
        
        return await func(client, message)
    return wrapper

def private_only(func):
    """Decorator to restrict command to private chats only."""
    @wraps(func)
    async def wrapper(client, message: Message):
        if message.chat.type != ChatType.PRIVATE:
            await message.reply_text("❌ This command can only be used in private chat!")
            return
        
        return await func(client, message)
    return wrapper

def log_command(func):
    """Decorator to log command usage."""
    @wraps(func)
    async def wrapper(client, message: Message):
        user = message.from_user
        chat = message.chat
        command = message.text.split()[0] if message.text else "unknown"
        
        logger.info(
            f"Command: {command} | User: {user.id} (@{user.username or 'none'}) | "
            f"Chat: {chat.id} ({chat.title or 'Private'})"
        )
        
        return await func(client, message)
    return wrapper
