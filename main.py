from discord.ext.commands import Bot
import random
import config

plg = Bot(command_prefix=".")

@plg.event
async def on_ready():
    print(plg.user.name)
    print(plg.user.id)

@plg.command()
async def hello(*args):
    print("Running command: hello")
    return await plg.send("Hello")

@plg.command()
async def invite(*args):
    print("Running command: invite")
    return await plg.send("discord.gg/9AEpU33")

@plg.command()
async def watch(*args):

    return await plg.send("https://www.watch2gether.com/rooms/forfunz-wfwuj0h0rho6v60fgk")

@plg.command()
async def rollstats(*args):
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
    return await plg.send(stats)

@plg.command()
async def uptime(*args):
    uptime_string = "Raspberry pi uptime:\n"

    with open("/proc/uptime", "r") as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string += str(timedelta(seconds = uptime_seconds))

    print("Running command: uptime")
    return await plg.send(uptime_string)

@plg.command()
async def roll(*args):
    try:
        args[0].upper()
    except:
        print("Running command: roll")
        return await plg.send("Roll dices by typing: !roll <numberOfDices>D<sizeOfDice>")

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
    return await plg.send(result)

@plg.command()
async def pc(*args):
    print("Running command: pc")
    return await plg.send("What the fuck did you just say about me, you sexist pig? I'll have you know I graduated top of my class in women's studies and have been involved in numerous false-flaggings against anti-feminist Youtube videos, and I have over 300 confirmed user bannings. I am trained in professional self-victimization and I have the top Patreon account in the entire feminist blogosphere. You are nothing to me but another blocked user. I will shut you the fuck up with feigned outrage the likes of which has never been seen before on Tumblr, mark my fucking tits. You think you can get away with saying that shit to me over the internet? Think again, shitlord. As we speak, I am contacting my secret network of progressive journalists whom I've fucked and your words are being taken out of context right now, so you better prepare for their white-knighting, bigot. The white-knighting that wipes out the pathetic little thing you call your reputation. You're fucking dead, fedora. I can doxx you anywhere, anytime, and I can check your privilege in over seven hundred ways, and that's just for your gender. Not only am I extensively trained in redefining words, but I have access to the entire database of the postmodern Marxist curriculum of my university and will use it to its full extent to wipe your mansplanation off the face of the internet, you little shit. If only you could have known what hysterical femtribution your “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn misogynist. I will menstruate fury all over you and you will drown in it. You're fucking over, neckbeard.")

@plg.command()
async def manythings(*args):
    deck = ["Balance \n Two of spades \n The character must change to a radically different alignment. If the character fails to act according to the new alignment, she gains a negative level.",
    "Comet \n Two of Diamonds \n The character must single-handedly defeat the next hostile monster or monsters encountered, or the benefit is lost. If successful, the character gains enough XP to attain the next experience level.",
    "Donjon \n Ace of spades \n This card signifies imprisonment— either by the imprisonment spell or by some powerful being. All gear and spells are stripped from the victim in any case. Draw no more cards.",
    "Euryale \n Queen of spades \n The medusalike visage of this card brings a curse that only the fates card or a deity can remove. The –1 penalty on all saving throws is otherwise permanent.",
    "The Fates \n Ace of hearts \n This card enables the character to avoid even an instantaneous occurrence if so desired, for the fabric of reality is unraveled and respun. Note that it does not enable something to happen. It can only stop something from happening or reverse a past occurrence. The reversal is only for the character who drew the card; other party members may have to endure the situation.",
    "Flames \n Queen of clubs \n Hot anger, jealousy, and envy are but a few of the possible motivational forces for the enmity. The enmity of the outsider can’t be ended until one of the parties has been slain. Determine the outsider randomly, and assume that it attacks the character (or plagues her life in some way) within 1d20 days.",
    "Fool \n Joker \n The payment of XP and the redraw are mandatory. This card is always discarded when drawn, unlike all others except the jester.",
    "Gem \n Two of hearts \n This card indicates wealth. The jewelry is all gold set with gems, each piece worth 2,000 gp, the gems 1,000 gp value each.",
    "Idiot \n Two of clubs \n This card causes the drain of 1d4+1 points of Intelligence immediately. The additional draw is optional.",
    "Jester \n Joker \n This card is always discarded when drawn, unlike all others except the fool. The redraws are optional.",
    "Key \n Queen of hearts \n The magic weapon granted must be one usable by the character. It suddenly appears out of nowhere in the character’s hand.",
    "Knight \n Jack of hearts \n The fighter appears out of nowhere and serves loyally until death. He or she is of the same race (or kind) and gender as the character.",
    "Moon \n Queen of diamonds \n This card sometimes bears the image of a moonstone gem with the appropriate number of wishes shown as gleams therein; sometimes it depicts a moon with its phase indicating the number of wishes (full=four; gibbous=three; half=two; quarter=one). These wishes are the same as those granted by the 9th-level wizard spell and must be used within a number of minutes equal to the number received.",
    "Rogue \n Jack of spades \n When this card is drawn, one of the character’s NPC friends (preferably a cohort) is totally alienated and forever after hostile. If the character has no cohorts, the enmity of some powerful personage (or community, or religious order) can be substituted. The hatred is secret until the time is ripe for it to be revealed with devastating effect.",
    "Ruin \n King of spades \n As implied by its name, when this card is drawn, all nonmagical possessions of the drawer are lost.",
    "Skull \n Jack of clubs \n A dread wraith appears. Treat this creature as an unturnable undead. The character must fight it alone—if others help, they get dread wraiths to fight as well. If the character is slain, she is slain forever and cannot be revived, even with a wish or a miracle.",
    "Star \n Jack of diamonds \n The 2 points are added to any ability the character chooses. They cannot be divided among two abilities.",
    "Sun \n King of diamonds \n Roll for a medium wondrous item until a useful item is indicated.",
    "Talons \n Ace of clubs \n When this card is drawn, every magic item owned or possessed by the character is instantly and irrevocably gone.",
    "Throne \n King of hearts \n The character becomes a true leader in people’s eyes. The castle gained appears in any open area she wishes (but the decision where to place it must be made within 1 hour).",
    "Vizier \n Ace of diamonds \n This card empowers the character drawing it with the one-time ability to call upon a source of wisdom to solve any single problem or answer fully any question upon her request. The query or request must be made within one year. Whether the information gained can be successfully acted upon is another question entirely.",
    "The Void \n King of clubs \n This black card spells instant disaster. The character’s body continues to function, as though comatose, but her psyche is trapped in a prison somewhere—in an object on a far plane or planet, possibly in the possession of an outsider. A wish or a miracle does not bring the character back, instead merely revealing the plane of entrapment. Draw no more cards."]

    card = random.randint(0, 21)

    return await plg.send(deck[card])



plg.run(config.token)
