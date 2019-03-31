from discord.ext import commands
from urllib.request import urlopen
import config, praw, json, urllib, locale



class Reddit:
    def __init__(self, bot):
        self.bot = bot
        locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')


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
        difference = int(subspew) - int(substs)
        subspew = locale.format("%d", int(subspew), grouping=True)
        substs = locale.format("%d", int(substs), grouping=True)
        difference = locale.format("%d", int(difference), grouping=True)
        res = """
PewDiePie:
{}
T-Series:
{}
Difference:
{}""".format(subspew, substs, difference)

        return await ctx.send(res)

    @commands.command()
    async def rs(self, ctx, username: str):
        print("Running command: rs")
        def get_jsonparsed_data(url):
            response = urlopen(url)
            data = response.read().decode("utf-8")
            return json.loads(data)

        url = ("https://apps.runescape.com/runemetrics/profile/profile?user=" + username)
        data = get_jsonparsed_data(url)

        res = """
**{}**
**Totalskill:** {}
**Total experience:** {}
**Combat level:** {}
**Quests completed:** {}
""".format(data.get("name"), data.get("totalskill"), locale.format("%d", data.get("totalxp"), grouping=True), data.get("combatlevel"), data.get("questscomplete"))
        return await ctx.send(res)

    @commands.command()
    async def rsskills(self, ctx, username: str):
        print("Running command: rsskills")
        def get_jsonparsed_data(url):
            response = urlopen(url)
            data = response.read().decode("utf-8")
            return json.loads(data)


        i = 0

        url = ("https://apps.runescape.com/runemetrics/profile/profile?user=" + username)
        data = get_jsonparsed_data(url)

        res = """
**{}**
**Totalskill:** {}
**Total experience:** {}
**Combat level:** {}
**Quests completed:** {}
""".format(data.get("name"), data.get("totalskill"), locale.format("%d", data.get("totalxp"), grouping=True), data.get("combatlevel"), data.get("questscomplete"))


        while (i < len(config.rsSkills)):

            skills = data.get("skillvalues")
            res += "\n" + "**" + config.rsSkills[i] + "**"
            for skill in skills:
                if int(skill["id"]) == i:
                    res += str(locale.format("%d", skill["level"], grouping=True)) + " **xp:** " + str(locale.format("%d", (skill["xp"]/10), grouping=True))
            i+=1

        return await ctx.send(res)

def setup(bot):
    bot.add_cog(Reddit(bot))
