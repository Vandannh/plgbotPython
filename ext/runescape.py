from discord.ext import commands
from urllib.request import urlopen
import config, praw, json



class Reddit:
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def runescape(self, ctx, username: str):
        print("Running command: runescape")
        def get_jsonparsed_data(url):
            response = urlopen(url)
            data = response.read().decode("utf-8")
            return json.loads(data)



        url = ("https://apps.runescape.com/runemetrics/profile/profile?user=" + username + "&activities=20")
        res = get_jsonparsed_data(url)



        print(res.get("totalskill"))

        return await ctx.send(res.get("totalskill"))

def setup(bot):
    bot.add_cog(Reddit(bot))
