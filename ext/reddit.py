from discord.ext import commands
import config
import praw


class Reddit:
    def __init__(self, bot):
        self.bot = bot

    def loginR(self):
        reddit = praw.Reddit(client_id=config.redditID, \
                             client_secret=config.redditSecret, \
                             user_agent='PLGbot', \
                             username='Vandann', \
                             password=config.redditPass)
        return reddit

    @commands.command()
    async def destiny(self, ctx):
        print("Running command: xur")
        subreddit = self.loginR().subreddit('destiny2')
        post = subreddit.hot(limit=2)
        for f in subreddit.hot(limit=2):
            post = f.url

        return await ctx.send(post)

def setup(bot):
    bot.add_cog(Reddit(bot))
