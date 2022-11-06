import discord
import datetime
import random
import time
import Constants
import requests
import main


async def command_unknown(message):
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


async def g_command(message):
    embed = discord.Embed(
        title=Constants.player_name_array[
                  random.randrange(0, len(Constants.player_name_array) - 4)
              ] + ": " + Constants.random_frog_died_comment[
                  random.randrange(0, len(Constants.random_frog_died_comment))],
        description=Constants.random_frog_death_message[
            random.randrange(0, len(Constants.random_frog_death_message))],
        colour=0x2f3136,
        url="https://Github.com/Wolkensteine/WolkenBot",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")
    await message.channel.send(embed=embed)


async def play_command(message):
    voice_channel = message.author.voice.channel
    channel = await voice_channel.connect()
    if message.content.lower().replace("!play.", "") == "frech":
        channel.play(discord.FFmpegPCMAudio(executable="ffmpeg-5.1.2-essentials_build/bin/ffmpeg.exe",
                                            source="frog.mp3"))
    elif message.content.lower().replace("!play.", "") == "help":
        embed = discord.Embed(
            title="Some audio help for you:",
            description="!play.name => Plays audio in your channel. Make sure you are connected to one!\n"
                        "names:\n"
                        "Frech",
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
            title="What's that?",
            description="Wait what is that? I don't know. When you wanted to play something then do "
                        "!play.help to see what you can actually play!",
            colour=0xff0000,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
        await message.channel.send(embed=embed)
        while channel.is_playing():
            time.sleep(1)
        channel.stop()
        await channel.disconnect()


async def gif_command(message):
    key = "YourKey"  # replace by your key!
    search_term = message.content.lower().replace("!gif ", "")
    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (
            search_term, key, "WolkenBot", 10))

    if r.status_code == 200:
        gif_json = r.json()
        gif = gif_json['results'][random.randrange(0, 9)]["media_formats"]["tinygif"]["url"]
        embed = discord.Embed(
            title=str(message.author) + " searched: " + search_term,
            colour=0xaaffaa,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_image(url=gif)
        embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
        await message.channel.send(embed=embed)

    await message.delete()


async def friend_command(message):
    if message.content.lower().replace("!friend", "") != "":
        temp_text = "Here is a list of answers on the !friend command: \n"
        x = 0
        while x < len(Constants.random_sentence_array):
            temp_text += Constants.random_sentence_array[x] + "\n"
            x += 1
        embed = discord.Embed(
            title="I'll help you out my friend!",
            description=temp_text,
            colour=0xff8c1a,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")

        await message.channel.send(embed=embed)
    else:
        temp_text = Constants.random_sentence_array[
            random.randrange(0, len(Constants.random_sentence_array))]

        if temp_text == "Hey there! You found an easteregg!":

            embed = discord.Embed(
                title="Is it really easteregg time?",
                description=temp_text,
                colour=0xccffff,
                url="https://Github.com/Wolkensteine/WolkenBot",
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                             icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                      "WolkensteineIcon.png")
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(temp_text)


async def pin_command(message):
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
