import datetime
import os
import discord
import main


async def permission_denied(message):
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


def get_role_access(message, rights):
    tmp = ""

    if rights == 0:
        tmp = "_accessall.txt"
    elif rights == 1:
        tmp = "_mediumaccess.txt"
    elif rights == 2:
        tmp = "_noaccess.txt"

    with open(message.guild.name + tmp) as file:
        tmp = file.read()

    tmp = tmp.split(" ")

    for i in range(len(tmp)):
        if tmp[i] in [y.name.lower() for y in message.author.roles]:
            return True

    for i in range(len(main.MyClient.admin_roles[get_server_number(message.guild.name)].split(" "))):
        if main.MyClient.admin_roles[get_server_number(message.guild.name)].split(" ")[i] in \
                [y.name.lower() for y in message.author.roles]:
            return True
        else:
            return False


def check_permissions(message, command):
    server_num = get_server_number(message.guild.name)
    req_rights = 0
    if command == "hello":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "friend":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "vote":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "info":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "pin":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "math":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "bot":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "play":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "g":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "rate":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "randomname":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "dadjokes":
        req_rights = main.MyClient.hello_command[server_num]

    return get_role_access(message, req_rights)


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
    # 0 => It'll require all rights
    # 1 => It'll require medium rights
    # 2 => It'll require no rights
    main.MyClient.hello_command.append(2)
    main.MyClient.friend_command.append(2)
    main.MyClient.vote_command.append(1)
    main.MyClient.info_command.append(2)
    main.MyClient.pin_command.append(0)
    main.MyClient.math_command.append(2)
    main.MyClient.bot_command.append(2)
    main.MyClient.play_command.append(1)
    main.MyClient.g_command.append(2)
    main.MyClient.rate_command.append(1)
    main.MyClient.random_name_command.append(2)
    main.MyClient.dad_joke_command.append(2)

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
        main.MyClient.access_all[server_num] = roles.lower()
    elif access == "mediumaccess":
        main.MyClient.medium_access[server_num] = roles.lower()
    elif access == "noaccess":
        main.MyClient.no_access[server_num] = roles.lower()
    save(server)


def change_command_rights(right, command, server):
    if not get_server_number(server):
        add_server(server)
    server_num = get_server_number(server)
    right_num = 2
    if right == "accessall":
        right_num = 0
    elif right == "mediumaccess":
        right_num = 1
    if command == "hello":
        main.MyClient.hello_command[server_num] = right_num
    elif command == "friend":
        main.MyClient.friend_command[server_num] = right_num
    elif command == "vote":
        main.MyClient.vote_command[server_num] = right_num
    elif command == "info":
        main.MyClient.info_command[server_num] = right_num
    elif command == "pin":
        main.MyClient.pin_command[server_num] = right_num
    elif command == "math":
        main.MyClient.math_command[server_num] = right_num
    elif command == "bot":
        main.MyClient.bot_command[server_num] = right_num
    elif command == "play":
        main.MyClient.play_command[server_num] = right_num
    elif command == "g":
        main.MyClient.g_command[server_num] = right_num
    elif command == "rate":
        main.MyClient.rate_command[server_num] = right_num
    elif command == "randomname":
        main.MyClient.random_name_command[server_num] = right_num
    elif command == "dadjokes":
        main.MyClient.dad_joke_command[server_num] = right_num
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
    elif content.startswith("command"):
        info = content.replace("command ", "").split(" ")
        if len(info) != 2:
            embed = discord.Embed(
                title="Sorry. I don't remember if this command could run without 2 arguments.",
                description="You should try this: !admin.rights command <right> <command>",
                colour=0xff0000,
                url="https://Github.com/Wolkensteine/WolkenBot",
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                             icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                      "WolkensteineIcon.png")

            await message.channel.send(embed=embed)
        else:
            change_command_rights(info[0], info[1], server=message.guild.name)


async def admin_help(message):
    embed = discord.Embed(
        title="Some help for you may Admin friend!",
        description="You need to have a role named admin or an other role with privileged access.\n"
                    "!admin.rights role <right> <role> * n\n"
                    "<right>s:\n"
                    "accessall => grant access to all commands for a role\n"
                    "mediumaccess => grant access to most commands for a role\n"
                    "noaccess => deny access to all commands for a role\n"
                    "!admin.rights command <right> <command>\n"
                    "<command>'s: !<command>\n"
                    "The rights are the same as above.\n"
                    "This will set a required permission level for a command.",
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
