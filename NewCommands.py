import discord
import datetime
import random
import Constants


async def rate_command(message):
    temp_text = message.content.lower().replace("!rate", "")
    embed = discord.Embed(
        title="Rate: ",
        colour=0xaaffaa,
        url="https://Github.com/Wolkensteine/WolkenBot",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")


async def random_name_command(message):
    await message.channel.send("A random name for you my friend: " + Constants.player_name_array[
        random.randrange(0, len(Constants.player_name_array))])
