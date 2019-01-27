from discord.ext import commands

class Plg:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        print("Running command: hello")
        return await ctx.send("Hello")


def setup(bot):
    bot.add_cog(Plg(bot))
