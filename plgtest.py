#!/usr/bin/python3.6
from discord.ext import commands
import datetime
import MySQLdb

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

    async def on_command_error(self, ctx, exc):
        e = getattr(exc, 'original', exc)
        if isinstance(e, (commands.CommandOnCooldown, discord.Forbidden)):
            print(str(e))
        elif isinstance(e, (commands.MissingRequiredArgument, commands.BadArgument)):
            await ctx.invoke(bot.get_command('help'), ctx.command.name)
            print(str(e))
        else:
            tb = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
            print(tb)


startup_ext = [
    "ext.plg",
]

bot = PlgBot(command_prefix="$")

if __name__ == "__main__":
    for cog in startup_cogs:
            try:
                bot.load_extension(cog)
            except Exception as e:
                print(f"{type(e).__name__} : {e}")
    bot.run()
