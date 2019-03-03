from discord.ext import commands
import random
import datetime
import config

class Plg:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        print("Running command: hello")
        return await ctx.send("Hello")


    @commands.command()
    async def invite(self, ctx):
        print("Running command: invite")
        return await ctx.send("discord.gg/9AEpU33")

    @commands.command()
    async def watch(self, ctx):
        print("Running command: watch")
        return await ctx.send("https://www.watch2gether.com/rooms/forfunz-wfwuj0h0rho6v60fgk")

    @commands.command()
    async def rollstats(self, ctx):
        print("Running command: rollstats")
        stats = ""

        def rollStats():
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)
            dice4 = random.randint(1, 6)

            stats = [dice1, dice2, dice3, dice4]
            stats.remove(min(stats))

            stat = sum(stats)

            return stat

        stats = "Your stats: \n Strength: {str} \n Dexterity: {dex} \n Constitution: {con} \n Intelligence: {int} \n Wisdom: {wis} \n Charisma: {cha}".format(str=rollStats(), dex=rollStats(), con=rollStats(), int=rollStats(), wis=rollStats(), cha=rollStats())
        print("Running command: rollstats")
        return await ctx.send(stats)

    @commands.command()
    async def uptime(self, ctx):
        print("Running command: uptime")
        uptime_string = "Raspberry pi uptime:\n"

        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string += str(timedelta(seconds = uptime_seconds))

        print("Running command: uptime")
        return await ctx.send(uptime_string)

    @commands.command()
    async def roll(self, ctx):
        print("Running command: roll")
        try:
            args[0].upper()
        except:
            print("Running command: roll")
            return await ctx.send("Roll dices by typing: !roll <numberOfDices>D<sizeOfDice>")

        single = False
        diceInput = args[0].upper()
        diceResult = []
        dices = diceInput.split("D")

        if len(dices) < 2:
            single = True

        i = 0
        if(single == False):

            while i < int(dices[0]):
                diceResult.append(random.randint(1, int(dices[1])))
                i += 1

            result = "Rolling dices: \n"
            for dice in diceResult:
                result += "D{}: {} \n".format(dices[1], dice)

            result += "Sum: {}".format(sum(diceResult))
        else:
            diceResult.append(random.randint(1, int(dices[0])))
            result = "Rolling dice: \n"
            result += "D{}: {} \n".format(dices[0], diceResult[0])

        print("Running command: roll")
        return await ctx.send(result)

    @commands.command()
    async def pc(self, ctx):
        print("Running command: pc")
        print("Running command: pc")
        return await ctx.send("```" + config.pc + "```")

    @commands.command()
    async def manythings(self, ctx):
        print("Running command: manythings")


        card = random.randint(0, 21)

        return await ctx.send(config.deck[card])

def setup(bot):
    bot.add_cog(Plg(bot))
