import discord
import vote
import CommonCommands
import InformationGivingCommands
import MathCommands
import NewCommands
import admin
import FrogUpdate

intents = discord.Intents.all()
intents.message_content = True
intents.members = True


class MyClient(discord.Client):
    vote_channel = None
    vote_creator = ""
    votes_per_theme = []
    voting_themes = []
    vote_running = False
    vote_duration = 30
    
    # rights that might be granted
    # if a role is not in one of the categories it will default to mediumaccess or a specified access of default_access
    access_all = []
    medium_access = []
    no_access = []
    # Default to what level of access
    default_access = []
    # Array with the server names to see which level must be loaded
    servers = []
    # Arrays for the needed rights for a specific command
    # 0 => access all
    # 1 => medium access
    # 2 => no access
    hello_command = []
    friend_command = []
    vote_command = []
    info_command = []
    pin_command = []
    math_command = []
    bot_command = []
    play_command = []
    g_command = []
    rate_command = []
    random_name_command = []
    dad_joke_command = []
    # Admin roles
    admin_roles = []
    
    
    async def on_ready(self):
        print("Beep bop, Wolkenbot is ready to start!")

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "hallo bot" \
                or message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "hello bot" \
                or message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "hallo wolkenbot" \
                or message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "hello wolkenbot" \
                or message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "moin wolkenbot" \
                or message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "moin bot":
            await message.channel.send("Hello " + str(message.author))
            await message.add_reaction("👋")

        if message.content.startswith("!"):
            if message.content.lower() == "!help":
                await InformationGivingCommands.help_command(message)

            elif message.content.lower().startswith("!friend"):
                if admin.check_permissions(message, "friend"):
                    await CommonCommands.friend_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!vote"):
                if admin.check_permissions(message, "vote"):
                    await vote.start(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower() == "!info":
                if admin.check_permissions(message, "info"):
                    await InformationGivingCommands.info_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!pin"):
                if admin.check_permissions(message, "pin"):
                    await CommonCommands.pin_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!math."):
                if admin.check_permissions(message, "math"):
                    await MathCommands.Math_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!bot"):
                if admin.check_permissions(message, "bot"):
                    await InformationGivingCommands.bot_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!gif"):
                if admin.check_permissions(message, "gif"):
                    await CommonCommands.gif_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!play."):
                if admin.check_permissions(message, "play"):
                    await CommonCommands.play_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower() == "!g":
                if admin.check_permissions(message, "g"):
                    await CommonCommands.g_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!rate"):
                if admin.check_permissions(message, "rate"):
                    await NewCommands.rate_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!randomname"):
                if admin.check_permissions(message, "randomname"):
                    await NewCommands.random_name_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!dadjoke"):
                if admin.check_permissions(message, "dadjokes"):
                    await NewCommands.dad_jokes_by_wald(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!mute"):
                if admin.check_permissions(message, "mute"):
                    await admin.mute_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!unmute"):
                if admin.check_permissions(message, "mute"):
                    await admin.un_mute_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!fishmaster") or \
                    message.content.lower().startswith("!fischmeister"):
                if admin.check_permissions(message, "fishmaster"):
                    await FrogUpdate.fish_master_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!donotannoy") or \
                    message.content.lower().startswith("!nervnicht"):
                if admin.check_permissions(message, "donotannoy"):
                    await FrogUpdate.do_not_annoy_command(message)
                else:
                    await admin.permission_denied(message)

            elif message.content.lower().startswith("!admin"):
                await admin.admin_commands(message)
            else:
                await CommonCommands.command_unknown(message)

        elif vote.check_vote_running():
            await vote.confirm(message)


if __name__ == "__main__":
    # Exclude this when you don't specify your keys in a separate file like I am.
    f = open("keys.txt")
    content = f.read().splitlines()
    discord_secret = content[0]

    client = MyClient(intents=intents)
    client.run(discord_secret)
