from discord.ext import commands



class Plg:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        print("Running command: hello")
        return await ctx.send("Hello")

    async def level_up(self):
        while True:
            cur_time = time.time()
            time_from_ten = cur_time % 600
            time_to_ten = 600 - time_from_ten
            time_to_level_up = min(600, max(time_to_ten, 5))
            await asyncio.sleep(time_to_level_up)




def setup(bot):
    bot.add_ext(Plg(bot))
