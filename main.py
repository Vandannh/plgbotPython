from discord.ext.commands import Bot


plg = Bot(command_prefix=".")

@plg.event
async def on_ready():
    print("User logged in")

@plg.command()
async def hello(*args):
    print("Running command: hello")
    return await plg.say("Hello")

@plg.command()
async def watch(*args):

    return await plg.say("https://www.watch2gether.com/rooms/forfunz-wfwuj0h0rho6v60fgk")


plg.run("Mzc3NTEzMzE3Njk2MDEyMjkx.DOOCVw.TPzCZWONF_QBYB0VpYe23_1Gjlw")
