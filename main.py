import datetime
import math
import time
import random

import discord

intents = discord.Intents.default()
intents.message_content = True
def start_vote(author, channel, duration):
    MyClient.vote_running = True
    MyClient.vote_creator = author
    MyClient.vote_channel = channel
    if int(duration) <= 600:
        MyClient.vote_duration = int(duration)
    else:
        MyClient.vote_duration = 600
def check_vote_creator(author):
    if MyClient.vote_creator == str(author):
        return True
    else:
        return False
def check_vote_running():
    if MyClient.vote_running:
        return True
    else:
        return False
def vote_confirm():
    MyClient.vote_running = False
def add_vote(theme):
    MyClient.voting_themes = MyClient.voting_themes + [theme]


class MyClient(discord.Client):
    vote_channel = None
    vote_creator = ""
    votes_per_theme = []
    voting_themes = []
    vote_running = False
    vote_duration = 30
    letter_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    emoji_array = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹',
                   '🇺',
                   '🇻', '🇼', '🇽', '🇾', '🇿']

    random_sentence_array = ["Hello my new friend!",
                             "Hey, how are you doing?",
                             "Is something going on?",
                             "Maybe another time ;)",
                             "Sadly I am busy maybe later.",
                             "Would you like to have some chocolate? I would.",
                             "Did you know I was written in python?",
                             "Python is a language. Did you know that?",
                             "Hey cool to have a new friend!",
                             "What's your favorite book?",
                             "Do you have a favorite film?",
                             "What about some deep talk?",
                             "Hey there!",
                             "This is just random, so good luck!",
                             "Have you a gambling addiction?",
                             "Do you like playing games?",
                             "How about going out and take some photos?",
                             "Maybe you should find some real friends.",
                             "If you ever need advice, ask someone else.",
                             "!help lets you know some stuff!",
                             "Move your lazy ass and go outside!",
                             "Do some physics my guy!",
                             "Ok!",
                             "Get some help!",
                             "**. . .** > . . .",
                             "Assembly > C > C# > C++ > Java > Kotlin > Python > PHP > JavaScript > CSS > HTML > "
                             "Scratch > Other languages"]

    async def on_ready(self):
        print("Beep bop, Wolkenbot is ready to start!")

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.lower() == "hallo bot" or message.content.lower() == "hello bot" or message.content.lower() \
                == "hallo wolkenbot" or message.content.lower() == "hello wolkenbot" or message.content.lower() == \
                "moin wolkenbot":
            await message.channel.send("Hello " + str(message.author))
            await message.add_reaction("👋")

        if message.content.startswith("!"):
            if message.content.lower() == "!help":
                embed = discord.Embed(
                    title="You need Help?",
                    description="!help => help\n"
                                "!friend => Answer with a random sentence - good luck :)\n"
                                "!vote + vote duration in seconds => You can create a voting system (example: '!vote 60"
                                "' to make in vote with a duration of one minute) [default duration: 60 seconds - "
                                "maximal duration is 600 seconds]\n"
                                "!info => informations about the bot\n"
                                "!pin + (message content) => Will pin a custom Message [!Attention!: This will resend "
                                "the Message as an embed, which might corrupt files attached to the message!]\n"
                                "!math => Has some cool math functions implemented. Run !math.help to see all the "
                                "commands of !math",
                    colour=0xff8c1a,
                    url="https://Github.com/Wolkensteine/WolkenBot",
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                 icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                          "WolkensteineIcon.png")
                await message.channel.send(embed=embed)
                await message.delete()
            elif message.content.lower() == "!friend":
                await message.channel.send(MyClient.random_sentence_array[
                                              random.randrange(0, len(MyClient.random_sentence_array) - 1)])
            elif message.content.lower().startswith("!vote"):
                if check_vote_running():
                    embed = discord.Embed(
                        title="There is a voting already running. Please try later again!",
                        colour=0xff0000,
                        url="https://Github.com/Wolkensteine/WolkenBot",
                        timestamp=datetime.datetime.utcnow()
                    )
                    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                              "WolkensteineIcon.png")
                    await message.channel.send(embed=embed)
                else:
                    if message.content.replace("!vote", "") == "":
                        start_vote(str(message.author), message.channel, "60")
                    else:
                        start_vote(str(message.author), message.channel, message.content.replace("!vote", ""))
                    embed = discord.Embed(
                        title="Start a vote",
                        description="Tell me the things to vote for in separate messages (The first message "
                                    "will be the theme listed above the voting). Write confirm at "
                                    "the end to start the voting!\nBut pay attention! The number of votable"
                                    "things is limited by the amount of letters! If you put more in query it"
                                    "won't work!\nYou specified a duration of " + str(MyClient.vote_duration) +
                                    " seconds.",
                        colour=0xccffff,
                        url="https://Github.com/Wolkensteine/WolkenBot",
                        timestamp=datetime.datetime.utcnow()
                    )
                    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                              "WolkensteineIcon.png")
                    await message.author.send(embed=embed)
                    await message.delete()
            elif message.content.lower() == "!info":
                embed = discord.Embed(
                    title="Info",
                    description="Version: 0.0.2 (Development version of WolkenBot)\nThis version of the bot may have "
                                "bugs or inefficiencies. When you have any problems either report directly to "
                                "@Wolkensteine or to your server administrator",
                    colour=0x00ccff,
                    url="https://Github.com/Wolkensteine/WolkenBot",
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                 icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                          "WolkensteineIcon.png")
                await message.channel.send(embed=embed)
            elif message.content.lower().startswith("!pin"):
                temp_text = message.content.replace("!pin ", "")

                embed = discord.Embed(
                    title="Message from: " + str(message.author),
                    description=temp_text,
                    colour=0xaaffaa,
                    url="https://Github.com/Wolkensteine/WolkenBot",
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                 icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                          "WolkensteineIcon.png")

                pin = await message.channel.send(embed=embed)
                await pin.pin()
                await message.delete()
            elif message.content.lower().startswith("!math."):
                if message.content.lower().replace("!math.", "").startswith("root"):
                    inputs = message.content.lower().replace("!math.square ", "").split(" ")
                    temp_text = "The " + inputs[1] + ". root of " + inputs[2] + " is: " + \
                                str(float(inputs[2]) ** 1/float(inputs[1]))
                    embed = discord.Embed(
                        title="Math.Root",
                        description=temp_text,
                        colour=0xcc33ff,
                        url="https://Github.com/Wolkensteine/WolkenBot",
                        timestamp=datetime.datetime.utcnow()
                    )
                    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                              "WolkensteineIcon.png")
                    await message.channel.send(embed=embed)
                elif message.content.lower().replace("!math.", "").startswith("square"):
                    inputs = message.content.lower().replace("!math.square ", "").split("^")
                    temp_text = inputs[0] + "^" + inputs[1] + " = " + str(float(inputs[0]) ** float(inputs[1]))
                    embed = discord.Embed(
                        title="Math.Square",
                        description=temp_text,
                        color=0xcc33ff,
                        url="https://Github.com/Wolkensteine/WolkenBot",
                        timestamp=datetime.datetime.utcnow()
                    )
                    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                              "WolkensteineIcon.png")
                    await message.channel.send(embed=embed)
                elif message.content.lower() == "!math.help":
                    embed = discord.Embed(
                        title="Math.Help",
                        description="Use '.' instead of ',' in case you are not used to the english version\n!math.root"
                                    " n number => nth root of number\n!math.square number^number => number^number = ?",
                        colour=0xff8c1a,
                        url="https://Github.com/Wolkensteine/WolkenBot",
                        timestamp=datetime.datetime.utcnow()
                    )
                    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                              "WolkensteineIcon.png")
                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(
                        title="Unknown Command",
                        description="I can't remember this command :frowning: type !math.help to get some help if "
                                    "you need it.",
                        colour=0xff0000,
                        url="https://Github.com/Wolkensteine/WolkenBot",
                        timestamp=datetime.datetime.utcnow()
                    )
                    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                              "WolkensteineIcon.png")
                    await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="Unknown Command",
                    description="I can't remember this command :frowning: type !help to get some help if "
                                "you need it.",
                    colour=0xff0000,
                    url="https://Github.com/Wolkensteine/WolkenBot",
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                 icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                          "WolkensteineIcon.png")

                await message.channel.send(embed=embed)

        elif check_vote_running():
            if check_vote_creator(message.author):
                if message.content.lower().startswith("confirm"):

                    temp_text = ""
                    x = 1
                    while x < len(MyClient.voting_themes):
                        temp_text += MyClient.voting_themes[x] + " :regional_indicator_" + MyClient.letter_array[x - 1] \
                                     + ":" + "\n"
                        x += 1
                    embed = discord.Embed(
                        title="Vote for: " + MyClient.voting_themes[0],
                        description=temp_text,
                        colour=0xccffff,
                        url="https://Github.com/Wolkensteine/WolkenBot",
                        timestamp=datetime.datetime.utcnow()
                    )
                    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                              "WolkensteineIcon.png")

                    vote_message = await MyClient.vote_channel.send(embed=embed)

                    x = 1
                    while x < len(MyClient.voting_themes):
                        await vote_message.add_reaction(MyClient.emoji_array[x - 1])
                        x += 1
                    time.sleep(int(MyClient.vote_duration))

                    reactions = []
                    react_message = await MyClient.vote_channel.fetch_message(vote_message.id)
                    reactions = react_message.reactions

                    temp_text = ""
                    x = 1
                    while x < len(MyClient.voting_themes):
                        temp_text += str(x) + ". " + MyClient.voting_themes[x] + ": " + str(reactions[x - 1].count - 1)\
                                     + "\n"
                        x += 1
                    embed = discord.Embed(
                        title="Voting results",
                        description=temp_text,
                        colour=0xccffff,
                        url="https://Github.com/Wolkensteine/WolkenBot",
                        timestamp=datetime.datetime.utcnow()
                    )
                    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                              "WolkensteineIcon.png")

                    await MyClient.vote_channel.send(embed=embed)

                    vote_confirm()

                else:
                    add_vote(message.content)


if __name__ == "__main__":
    client = MyClient(intents=intents)
    client.run("Secret")
