
import asyncio
import logging
import os

import a2s
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID", "0"))
DAYZ_HOST = os.getenv("DAYZ_HOST", "")
DAYZ_QUERY_PORT = int(os.getenv("DAYZ_QUERY_PORT", "26541"))

POLL_INTERVAL = 60
NICKNAME_PREFIX = "NV+ | "
OFFLINE_NAME = NICKNAME_PREFIX + "OFFLINE"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("NVPlayerCount")


def get_player_count():
    """Query the DayZ server using Steam A2S."""

    info = a2s.info(
        (DAYZ_HOST, DAYZ_QUERY_PORT),
        timeout=5.0
    )

    return info.player_count, info.max_players


class PlayerCountBot(discord.Client):

    def __init__(self):
        intents = discord.Intents.default()
        intents.guilds = True

        super().__init__(intents=intents)

        self.last_nickname = None
        self.update_task = None

    async def on_ready(self):
        logger.info("Logged into Discord as %s", self.user)

        if self.update_task is None or self.update_task.done():
            self.update_task = asyncio.create_task(
                self.player_count_loop()
            )

    async def player_count_loop(self):

        await self.wait_until_ready()

        while not self.is_closed():

            try:
                players, max_players = await asyncio.to_thread(
                    get_player_count
                )

                nickname = (
                    f"{NICKNAME_PREFIX}"
                    f"{players}/{max_players}"
                )

                logger.info(
                    "DayZ player count: %s/%s",
                    players,
                    max_players
                )

            except Exception as error:
                logger.warning(
                    "DayZ query failed: %s",
                    error
                )

                nickname = OFFLINE_NAME

            try:
                guild = self.get_guild(GUILD_ID)

                if guild is None:
                    logger.error(
                        "Discord guild not found: %s",
                        GUILD_ID
                    )

                else:
                    member = guild.me

                    if member is None:
                        member = await guild.fetch_member(
                            self.user.id
                        )

                    if member.nick != nickname:
                        await member.edit(
                            nick=nickname,
                            reason="Automatic DayZ player count update"
                        )

                        logger.info(
                            "Updated Discord nickname: %s",
                            nickname
                        )

                    self.last_nickname = nickname

            except discord.Forbidden:
                logger.error(
                    "Missing permission to change bot nickname."
                )

            except discord.HTTPException as error:
                logger.error(
                    "Discord API error: %s",
                    error
                )

            await asyncio.sleep(POLL_INTERVAL)


def main():

    if not TOKEN:
        raise RuntimeError(
            "DISCORD_TOKEN is missing from .env"
        )

    if not GUILD_ID:
        raise RuntimeError(
            "DISCORD_GUILD_ID is missing from .env"
        )

    if not DAYZ_HOST:
        raise RuntimeError(
            "DAYZ_HOST is missing from .env"
        )

    bot = PlayerCountBot()
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
