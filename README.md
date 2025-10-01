# MrManager Bot

A modular Telegram group management bot built with Pyrogram.

## Features

✨ **Moderation Commands**
- Kick, ban, unban users
- Mute and unmute members
- Delete and purge messages

📌 **Admin Tools**
- Pin and unpin messages
- Promote and demote users
- Manage chat settings

ℹ️ **Information Commands**
- User and chat info
- Statistics and admin list
- ID lookup

⚙️ **Chat Settings**
- Lock and unlock chat
- Set chat photo, title, and description

## Installation

1. **Clone or download this repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Create .env file**
Create a `.env` file in the root directory with your credentials:
```env
API_ID=12345678
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here
LOG_LEVEL=INFO
SUDO_USERS=your_user_id
```

4. **Run the bot**
```bash
python -m MrManager
```

## Project Structure

```
MrManager/
├── __init__.py           # Package initialization
├── __main__.py           # Entry point
├── config.py             # Configuration management
├── logger.py             # Logging setup
├── bot.py                # Bot client
├── plugins/              # Command handlers
│   ├── __init__.py
│   ├── start.py          # Start command
│   ├── help.py           # Help command
│   ├── admin.py          # Admin commands
│   ├── moderation.py     # Moderation commands
│   ├── info.py           # Info commands
│   └── settings.py       # Settings commands
└── helpers/              # Helper utilities
    ├── __init__.py
    ├── decorators.py     # Custom decorators
    └── utils.py          # Utility functions
```

## Configuration

### Environment Variables

- `API_ID`: Your Telegram API ID (required)
- `API_HASH`: Your Telegram API hash (required)
- `BOT_TOKEN`: Your bot token from @BotFather (required)
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL) - default: INFO
- `BOT_USERNAME`: Your bot's username
- `SUDO_USERS`: Comma-separated list of user IDs with sudo access

### Log Levels

- **DEBUG**: Detailed information for debugging
- **INFO**: General informational messages (default)
- **WARNING**: Warning messages
- **ERROR**: Error messages
- **CRITICAL**: Critical issues

## Adding New Plugins

To add a new plugin, create a new file in the `plugins/` directory:

```python
from pyrogram import Client, filters
from pyrogram.types import Message
from ..helpers.decorators import log_command, admin_only, group_only
from ..logger import logger

@Client.on_message(filters.command("mycommand"))
@log_command
@group_only
@admin_only
async def my_command(client: Client, message: Message):
    """My custom command."""
    await message.reply_text("Hello from my command!")
    logger.info("My command executed")
```

## Available Decorators

The bot includes several useful decorators in `helpers/decorators.py`:

- `@admin_only`: Restricts command to group admins
- `@sudo_only`: Restricts command to sudo users (defined in config)
- `@group_only`: Restricts command to group chats
- `@private_only`: Restricts command to private chats
- `@log_command`: Logs command usage

## Usage Examples

### Basic Commands
- `/start` - Start the bot (private chat only)
- `/help` - Show help message
- `/id` - Get your user ID and chat ID
- `/info` - Get user information (reply to get other user's info)

### Admin Commands (Groups Only)
- `/kick` - Kick a user (reply to their message)
- `/ban` - Ban a user (reply to their message)
- `/mute` - Mute a user (reply to their message)
- `/pin` - Pin a message (reply to the message)
- `/promote` - Promote user to admin (reply to their message)
- `/lock` - Lock chat for non-admins
- `/settitle New Title` - Set new chat title

## Requirements

- Python 3.7+
- Pyrogram 2.0+
- TgCrypto
- python-dotenv

## Getting API Credentials

1. Go to https://my.telegram.org
2. Log in with your phone number
3. Click on "API Development Tools"
4. Create a new application
5. Copy your `API_ID` and `API_HASH`

## Getting Bot Token

1. Message @BotFather on Telegram
2. Send `/newbot` and follow the instructions
3. Copy the bot token provided

## License

This project is open source and available under the [AGPL v3.0 License](LICENSE).

## Developer

Developed by [@dotenv](https://telegram.me/dotenv) with ❤️

## Support

For issues and questions, please open an issue on the repository.

---

