import discord
import aiohttp

from discord.ext import commands

class Docs(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.docs_url = "https://hub.spigotmc.org/javadocs/spigot"

    @commands.command(aliases = ["docs", ])
    async def d(self, ctx: commands.Context, path: str = None) -> None:
        if not path:
            await ctx.send("`path` can't be None")
            return

        async with aiohttp.ClientSession() as session:
            if path.split(".")[-1][0].isupper():
                url = f"{self.docs_url}/{path.replace('.', '/')}.html"
                print(url)

            else:
                url = f"{self.docs_url}/{path.replace('.', '/')}/package-summary.html"

            async with session.get(url) as resp:
                if resp.status == 200:
                    await ctx.send(url)

                else:
                    await ctx.send("Please provide a valid path")

def setup(bot: commands.Bot):
    bot.add_cog(Docs(bot))