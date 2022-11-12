import datetime
import discord
import main


def add_server(server_name):
    main.MyClient.servers.append(server_name)
    main.MyClient.access_all.append("")
    main.MyClient.medium_access.append("")
    main.MyClient.no_access.append("")


def get_server_number(server_name):
    for i in range(len(main.MyClient.servers)):
        if main.MyClient.servers[i] == server_name:
            return i
    return False


def save(server):
    server_num = get_server_number(server)
    with open("./Admin/" + server + "_accessall.txt") as file:
        file.write(main.MyClient.access_all[server_num])
    with open("./Admin/" + server + "_mediumaccess.txt") as file:
        file.write(main.MyClient.medium_access[server_num])
    with open("./Admin/" + server + "_noaccess.txt") as file:
        file.write(main.MyClient.no_access[server_num])


def change_access(access, roles, server):
    print(access, roles, server)
    if not get_server_number(server):
        add_server(server)
    server_num = get_server_number(server)
    if access == "accessall":
        main.MyClient.access_all[server_num] = roles
    elif access == "mediumaccess":
        main.MyClient.medium_access[server_num] = roles
    elif access == "noaccess":
        main.MyClient.no_access[server_num] = roles
    save(server)


async def admin_rights_command(message, content):
    # Admins can configure rights with this command
    if content.startswith("role"):
        info = content.replace("role ", "").split(" ")
        if len(info) < 2:
            embed = discord.Embed(
                title="Sorry. I don't remember if this command could run without at least 2 arguments.",
                description="You should try this: !admin.rights role <right> <role> * n",
                colour=0xff0000,
                url="https://Github.com/Wolkensteine/WolkenBot",
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                             icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                      "WolkensteineIcon.png")

            await message.channel.send(embed=embed)
        else:
            right = info[0]
            roles = [discord.utils.get(message.guild.roles, name=info[1])]
            for i in range(len(info) - 2):
                roles.append(discord.utils.get(message.guild.roles, name=info[i + 2]))

            if right == "accessall" or right == "mediumaccess" or right == "noaccess":
                change_access(right, roles, message.guild.name)
            else:
                embed = discord.Embed(
                    title="Sorry. I don't remember that as a right.",
                    description="You should try this: !admin.rights role <right> <role> * n\n"
                                "There are the following rights:\n"
                                "accessall.json => grant access to all commands for a role\n"
                                "mediumaccess => grant access to most commands for a role\n"
                                "noaccess => deny access to all commands for a role\n",
                    colour=0xff0000,
                    url="https://Github.com/Wolkensteine/WolkenBot",
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                                 icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                          "WolkensteineIcon.png")

                await message.channel.send(embed=embed)


async def admin_help(message):
    embed = discord.Embed(
        title="Some help for you may Admin friend!",
        description="You need to have a role named admin or an other role with privileged access.\n"
                    "!admin.rights role <right> <role> * n\n"
                    "<right>s:\n"
                    "accessall.json => grant access to all commands for a role\n"
                    "mediumaccess => grant access to most commands for a role\n"
                    "noaccess => deny access to all commands for a role\n",
        colour=0xff8c1a,
        url="https://Github.com/Wolkensteine/WolkenBot",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")

    await message.channel.send(embed=embed)


async def admin_commands(message):
    # This switches between different Admin commands
    if message.content.lower().replace("!admin.", "").startswith("rights"):
        await admin_rights_command(message, message.content.lower().replace("!admin.rights ", ""))
    if message.content.lower().replace("!admin.", "").startswith("help"):
        await admin_help(message)
