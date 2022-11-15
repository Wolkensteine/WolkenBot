import datetime
import os
import discord
import main


def load_server(server_name):
    main.MyClient.servers.append(server_name)
    file = open("./Admin/" + server_name + "_accessall.txt", 'r')
    main.MyClient.access_all.append(file.read())
    file.close()
    file = open("./Admin/" + server_name + "_mediumaccess.txt", 'r')
    main.MyClient.medium_access.append(file.read())
    file.close()
    file = open("./Admin/" + server_name + "_noaccess.txt", 'r')
    main.MyClient.no_access.append(file.read())
    file.close()
    file = open("./Admin/" + server_name + "_command_access.txt", 'r')

    tmp = file.read().split(" ")

    main.MyClient.hello_command.append(tmp[0])
    main.MyClient.friend_command.append(tmp[1])
    main.MyClient.vote_command.append(tmp[2])
    main.MyClient.info_command.append(tmp[3])
    main.MyClient.pin_command.append(tmp[4])
    main.MyClient.math_command.append(tmp[5])
    main.MyClient.bot_command.append(tmp[6])
    main.MyClient.play_command.append(tmp[7])
    main.MyClient.g_command.append(tmp[8])
    main.MyClient.rate_command.append(tmp[9])
    main.MyClient.random_name_command.append(tmp[10])
    main.MyClient.dad_joke_command.append(tmp[11])

    file.close()
    file = open("./Admin/" + server_name + "_admin_roles.txt", 'r')
    main.MyClient.admin_roles.append(file.read())
    file.close()


def load_settings():
    file_list = os.listdir(path=r"./Admin/")
    for i in range(len(file_list)):
        tmp = file_list[i].replace("_accessall.txt", "").replace("_mediumaccess.txt", "").replace("_noaccess.txt", "").\
            replace("_command_access.txt", "").replace("_admin_roles.txt", "")
        if type(get_server_number(tmp)) != int:
            load_server(tmp)


def add_server(server_name):
    print("Adding server: " + server_name)
    main.MyClient.servers.append(server_name)
    main.MyClient.access_all.append("")
    main.MyClient.medium_access.append("")
    main.MyClient.no_access.append("")
    main.MyClient.admin_roles.append("admin")

    # Setting default rights
    # for everything but the pin command you'll need medium privileges (all roles not on the blacklist)
    # only for the pin command you'll need full rights
    main.MyClient.hello_command.append(1)
    main.MyClient.friend_command.append(1)
    main.MyClient.vote_command.append(1)
    main.MyClient.info_command.append(1)
    main.MyClient.pin_command.append(0)
    main.MyClient.math_command.append(1)
    main.MyClient.bot_command.append(1)
    main.MyClient.play_command.append(1)
    main.MyClient.g_command.append(1)
    main.MyClient.rate_command.append(1)
    main.MyClient.random_name_command.append(1)
    main.MyClient.dad_joke_command.append(1)

    server_num = get_server_number(server_name)

    file = open("./Admin/" + server_name + "_accessall.txt", 'w')
    file.close()
    file = open("./Admin/" + server_name + "_mediumaccess.txt", 'w')
    file.close()
    file = open("./Admin/" + server_name + "_noaccess.txt", 'w')
    file.close()
    file = open("./Admin/" + server_name + "_command_access.txt", 'w')
    file.close()
    file = open("./Admin/" + server_name + "_admin_roles.txt", 'w')
    file.close()
    save(server_name)


def get_server_number(server_name):
    for i in range(len(main.MyClient.servers)):
        if main.MyClient.servers[i] == server_name:
            return i
    return False


def save(server):
    server_num = get_server_number(server)
    with open("./Admin/" + server + "_accessall.txt", 'w') as file:
        file.write(main.MyClient.access_all[server_num])
    with open("./Admin/" + server + "_mediumaccess.txt", 'w') as file:
        file.write(main.MyClient.medium_access[server_num])
    with open("./Admin/" + server + "_noaccess.txt", 'w') as file:
        file.write(main.MyClient.no_access[server_num])
    with open("./Admin/" + server + "_admin_roles.txt", 'w') as file:
        file.write(main.MyClient.admin_roles[server_num])
    with open("./Admin/" + server + "_command_access.txt", 'w') as file:
        file.write(str(main.MyClient.hello_command[server_num]) + " " +
                   str(main.MyClient.friend_command[server_num]) + " " +
                   str(main.MyClient.vote_command[server_num]) + " " +
                   str(main.MyClient.info_command[server_num]) + " " +
                   str(main.MyClient.pin_command[server_num]) + " " +
                   str(main.MyClient.math_command[server_num]) + " " +
                   str(main.MyClient.bot_command[server_num]) + " " +
                   str(main.MyClient.play_command[server_num]) + " " +
                   str(main.MyClient.g_command[server_num]) + " " +
                   str(main.MyClient.rate_command[server_num]) + " " +
                   str(main.MyClient.random_name_command[server_num]) + " " +
                   str(main.MyClient.dad_joke_command[server_num]))


def change_access(access, roles, server):
    if type(get_server_number(server)) != int:
        add_server(server)
    server_num = get_server_number(server)
    if access == "accessall":
        main.MyClient.access_all[server_num] = roles
    elif access == "mediumaccess":
        main.MyClient.medium_access[server_num] = roles
    elif access == "noaccess":
        main.MyClient.no_access[server_num] = roles
    save(server)


def change_command_rights(right, command, server):
    if not get_server_number(server):
        add_server(server)
    server_num = get_server_number(server)

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
            roles = info[1]
            for i in range(len(info) - 2):
                roles += " " + info[i + 2]

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
    if type(get_server_number(message.guild.name)) != int:
        add_server(message.guild.name)

    # This switches between different Admin commands
    for i in range(len(main.MyClient.admin_roles[get_server_number(message.guild.name)].split(" "))):
        if main.MyClient.admin_roles[get_server_number(message.guild.name)].split(" ")[i] in \
                [y.name.lower() for y in message.author.roles]:
            if message.content.lower().replace("!admin.", "").startswith("rights"):
                await admin_rights_command(message, message.content.lower().replace("!admin.rights ", ""))
            if message.content.lower().replace("!admin.", "").startswith("help"):
                await admin_help(message)
            return
        else:
            embed = discord.Embed(
                title="Access denied!",
                colour=0xff0000,
                url="https://Github.com/Wolkensteine/WolkenBot",
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                             icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                      "WolkensteineIcon.png")

            await message.channel.send(embed=embed)
