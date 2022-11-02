import discord
import vote
import CommonCommands
import InformationGivingCommands
import MathCommands
import NewCommands


intents = discord.Intents.default()
intents.message_content = True
class MyClient(discord.Client):
    vote_channel = None
    vote_creator = ""
    votes_per_theme = []
    voting_themes = []
    vote_running = False
    vote_duration = 30
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
                await CommonCommands.friend_command(message)
            elif message.content.lower().startswith("!vote"):
                await vote.start(message)
            elif message.content.lower() == "!info":
                await InformationGivingCommands.info_command(message)
            elif message.content.lower().startswith("!pin"):
                await CommonCommands.pin_command(message)
            elif message.content.lower().startswith("!math."):
                await MathCommands.Math_command(message)
            elif message.content.lower().startswith("!bot"):
                await InformationGivingCommands.bot_command(message)
            elif message.content.lower().startswith("!gif"):
                await CommonCommands.gif_command(message)
            elif message.content.lower().startswith("!play."):
                await CommonCommands.play_command(message)
            elif message.content.lower() == "!g":
                await CommonCommands.g_command(message)
            elif message.content.lower().startswith("!rate"):
                await NewCommands.rate_command(message)
            elif message.content.lower().startswith("!randomname"):
                await NewCommands.random_name_command(message)
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
