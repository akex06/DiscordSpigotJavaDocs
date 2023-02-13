import discord
import aiohttp

from discord.ext import commands

class Docs(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.docs = {
            "spigot": "https://hub.spigotmc.org/javadocs/spigot",
            "bungeecord": "https://ci.md-5.net/job/BungeeCord/ws/api/target/apidocs/",
            "bungeecord-chat": "https://javadoc.io/doc/net.md-5/bungeecord-chat/latest/"
        }



    async def get_docs(self, javadocs: str, path: str) -> str:
        async with aiohttp.ClientSession() as session:
            if path.split(".")[-1][0].isupper():
                url = f"{self.docs[javadocs]}/{path.replace('.', '/')}.html"

            else:
                url = f"{self.docs[javadocs]}/{path.replace('.', '/')}/package-summary.html"

            async with session.get(url) as resp:
                if resp.status == 200:
                    return url

                else:
                    return "Please provide a valid path"

    @commands.command(aliases = ["jd-s", ])
    async def jds(self, ctx: commands.Context, path: str = None) -> None:
        if not path:
            await ctx.send(self.docs["spigot"])
            return
            
        await ctx.send(await self.get_docs("spigot", path))

    @commands.command(aliases = ["jd-bc", ])
    async def jdbc(self, ctx: commands.Context, path: str = None) -> None:
        if not path:
            await ctx.send(self.docs["bungeecord"] + "index.html")
            return

        await ctx.send(await self.get_docs("bungeecord", path))

    @commands.command(aliases = ["jd-bcc", ])
    async def jdbcc(self, ctx: commands.Context, path: str = None) -> None:
        if not path:
            await ctx.send(self.docs["bungeecord-chat"] + "index.html")
            return

        await ctx.send(await self.get_docs("bungeecord-chat", path))

def setup(bot: commands.Bot):
    bot.add_cog(Docs(bot))