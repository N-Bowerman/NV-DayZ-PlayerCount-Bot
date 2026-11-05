
# NV DayZ Player Count Bot

A lightweight Python Discord bot that displays the live player count of a DayZ dedicated server in the Discord member list.

## Features

- Live DayZ player count
- Updates every 60 seconds
- Uses Steam A2S server queries
- No RCON or DayZ admin password required
- No Discord commands or chat messages
- Automatic Discord reconnection
- Offline status when the DayZ query fails
- Minimal CPU and memory requirements

## Example

NV+ | 20/60

## Requirements

- Python 3.11 or newer
- Discord bot token
- Discord server ID
- DayZ server hostname and Steam query port
- Network access to Discord and the DayZ query port

## Installation (Windows)

1. Download or clone the repository.
2. Run setup.bat to install dependencies.
3. Create a .env file using .env.example.
4. Enter your Discord bot token and server ID.
5. Run start.bat.

## Environment Configuration

DISCORD_TOKEN - Discord bot authentication token

DISCORD_GUILD_ID - Target Discord server ID

DAYZ_HOST - DayZ server hostname

DAYZ_QUERY_PORT - Steam A2S query port

## Discord Permissions

The bot only requires:

- Change Nickname

It does not require Administrator, Message Content Intent, Server Members Intent or Presence Intent.

## Hosting

The bot currently runs successfully on Windows.

It may also be deployed on Linux or a compatible hosting environment with Python 3.11+.

Aussie Server Hosts deployment is pending hosting-provider approval.

## Security

Never commit the .env file or disclose the Discord bot token.

The bot does not require access to DayZ admin credentials, RCON, game files or the Pterodactyl API.
