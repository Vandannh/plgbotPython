from discord.ext import commands
import plgtestcommands

class PlgBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super(PlgBot, self).__init__(*args, **kwargs)

    async def on_ready(self):
        print(self.user.name)



bot = PlgBot(command_prefix="$")

bot.load_extension("plgtestcommands")

bot.run("NTM5MDYyODA3OTQ2MzMwMTEz.Dy9OzA.AcEq0vEgt3jzKK8HCJd4S1gmTds")
