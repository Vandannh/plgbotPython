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
        data = get_jsonparsed_data(url)

        res = """
{}
Totalskill: {}
Total experience: {}
Combat level: {}
Quests completed: {}

""".format(data.get("name"), data.get("totalskill"), data.get("totalxp"), data.get("combatlevel"), data.get("questscomplete"))

        return await ctx.send(res)

def setup(bot):
    bot.add_cog(Reddit(bot))
