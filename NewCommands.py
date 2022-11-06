import discord
import datetime
import random
import Constants


async def rate_command(message):
    temp_text = message.content.lower().replace("!rate ", "")
    embed = discord.Embed(
        title="Rate: " + temp_text,
        colour=0xaaffaa,
        url="https://Github.com/Wolkensteine/WolkenBot",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")
    rate_message = await message.channel.send(embed=embed)
    x = 0
    while x < 11:
        await rate_message.add_reaction(Constants.number_emoji_array[x])
        x += 1


async def random_name_command(message):
    await message.channel.send("A random name for you my friend: " + Constants.player_name_array[
        random.randrange(0, len(Constants.player_name_array))])


async def dad_jokes_by_wald(message):
    await message.channel.send("A random dad joke from Waldi for you (" + str(message.author) + "): " + Constants.random_dad_joke_array[
        random.randrange(0, len(Constants.random_dad_joke_array))])
    await message.delete()
