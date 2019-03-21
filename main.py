#!/usr/bin/python
from discord.ext import commands
import datetime
import config

class PlgBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super(PlgBot, self).__init__(*args, **kwargs)

    async def on_ready(self):
        print(self.user.name)


    async def process_commands(self, message):
        ctx = await self.get_context(message)

        if ctx.command is None:
            return

        await self.invoke(ctx)

startup_ext = [
    "ext.plg",
    "ext.reddit",
    "ext.url",
]

bot = PlgBot(command_prefix=".")

if __name__ == "__main__":
    for cog in startup_ext:
            try:
                bot.load_extension(cog)
            except Exception as e:
                print(f"{type(e).__name__} : {e}")
    bot.run(config.token)
