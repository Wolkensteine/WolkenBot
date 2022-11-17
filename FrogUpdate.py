async def fish_master_command(message):
    global user
    tmp = message.content.replace("!Fishmaster ", "").replace("!Fischmeister ", "")\
        .replace("!fishmaster ", "").replace("!fischmeister ", "").split(" ")
    name = tmp[0]
    for member in message.guild.members:
        if member.name.lower() == name.lower():
            user = member

    await user.edit(nick="Fischmeister")


async def do_not_annoy_command(message):
    global user
    tmp = message.content.replace("!donotannoy ", "").replace("!Donotannoy ", "") \
        .replace("!DoNotAnnoy ", "").replace("!DoNotannoy ", "").split(" ")
    name = tmp[0]
    for member in message.guild.members:
        if member.name.lower() == name.lower():
            user = member

    await user.edit(voice_channel=None)
