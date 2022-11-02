import datetime
import discord
import time
import Constants
from main import MyClient


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


async def end_voting(vote_message):
    time.sleep(int(MyClient.vote_duration))

    react_message = await MyClient.vote_channel.fetch_message(vote_message.id)
    reactions = react_message.reactions

    temp_text = ""

    x = 1
    while x < len(MyClient.voting_themes):
        temp_text += str(x) + ". " + MyClient.voting_themes[x] + ": " + str(reactions[x - 1].count - 1) \
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


async def start(message):
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


async def confirm(message):
    if check_vote_creator(message.author):
        if message.content.lower().startswith("confirm"):

            temp_text = ""
            x = 1
            while x < len(MyClient.voting_themes):
                temp_text += MyClient.voting_themes[x] + " :regional_indicator_" + Constants.letter_array[x - 1] \
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
                await vote_message.add_reaction(Constants.emoji_array[x - 1])
                x += 1

            await end_voting(vote_message)

        else:
            add_vote(message.content)
