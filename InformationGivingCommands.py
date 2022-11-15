import discord
import datetime


async def bot_command(message):
    embed = discord.Embed(
        title="Hello it's me a small robot!",
        description="This is a small Bot made by me (@Wolkensteine) just for fun. If you want to know more "
                    "use commands like !info or !help to get some stuff from me :)",
        colour=0xaaffaa,
        url="https://Github.com/Wolkensteine/WolkenBot",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")
    await message.channel.send(embed=embed)


async def help_command(message):
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
            "commands of !math\n"
            "!gif + search term => Sends you a gif found with your search term\n"
            "!play. + term => plays a sound specified by the term. Get help with !play.help\n"
            "!g => Sends you a random Frog death message.\n"
            "!rate + text => Lets you rate sth easily\n"
            "!randomname => returns a random name\n"
            "!dadjoke => sends you a dad joke (feature requested by binMalKurzImWald)",
        colour=0xff8c1a,
        url="https://Github.com/Wolkensteine/WolkenBot",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")
    await message.channel.send(embed=embed)
    await message.delete()


async def info_command(message):
    embed = discord.Embed(
        title="Info",
        description="Version: 2.2.0 (Beta) \nWhen you have any problems either report directly to "
                    "@Wolkensteine or to your server administrator",
        colour=0x00ccff,
        url="https://Github.com/Wolkensteine/WolkenBot",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")
    await message.channel.send(embed=embed)
