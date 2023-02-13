import discord

from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix = "?",
            intents = discord.Intents.all()
        )

    async def on_ready(self):
        print(f"[  READY  ]: {self.user}")
        self.load_extension("cogs.docs")

bot = Bot()
bot.run("ODc3NTU5ODQyMDM2OTQwODYx.G7PZVf.VVyUibwf0yGg2IF5ofjdBF8gPHItl071nnV4a0")