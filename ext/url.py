from discord.ext import commands
from urllib.request import urlopen
import config, praw, json, urllib



class Reddit:
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def pvst(self, ctx):
        print("Running command: pvst")

        g_api = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="

        def get_subs(yt_name):
            data = urllib.request.urlopen(g_api + yt_name + "&key=" + config.googleKey).read()
            subs = json.loads(data.decode("utf-8"))["items"][0]["statistics"]["subscriberCount"]
            return subs

        subspew = get_subs("PewDiePie")
        substs = get_subs("tseries")
        res = """
PewDiePie:
{}
T-Series:
{}
Difference:
{}""".format(int(subspew), int(substs), abs(int(subspew) - int(substs)))

        return await ctx.send(res)

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
