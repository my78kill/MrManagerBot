# Copyright warning,  PN-Projects 2025
# Do not kang withour proper credits and accredations or it will be considered as copyright infringement
# This code is liscensed under AGPL V3.0 
# Do not use this code to spam or to send any malicious code to others.

# ============================================================
# FILE: MrManager/helpers/utils.py
# ============================================================
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

async def is_admin(client, chat_id: int, user_id: int) -> bool:
    """Check if user is admin in the chat."""
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except:
        return False

def extract_user_id(message: Message) -> int:
    """Extract user ID from message (reply or mention)."""
    if message.reply_to_message:
        return message.reply_to_message.from_user.id
    
    # Extract from command arguments (for future use)
    if len(message.command) > 1:
        try:
            return int(message.command[1])
        except ValueError:
            return None
    
    return None
