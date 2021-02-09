from contextlib import redirect_stdout
import re
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="y/")


class report(commands.Cog, name="report"):
    """```
    report関係
    ```"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="feedback")
    async def feedback(self, ctx, *, content: str):
        """`誰でも`"""

        e = discord.Embed(title='Feedback', color=0x00aaff)
        channel = self.bot.get_channel(411811277724319744)
        if channel is None:
            return

        e.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
        e.description = content
        e.timestamp = ctx.message.created_at

        if ctx.guild is not None:
            e.add_field(name='Server', value=f'{ctx.guild.name} (ID: {ctx.guild.id})', inline=False)

        e.add_field(name='Channel', value=f'{ctx.channel} (ID: {ctx.channel.id})', inline=False)
        e.set_footer(text=f'Author ID: {ctx.author.id}')

        await channel.send(embed=e)
        await ctx.send(f'{ctx.tick(True)} Successfully sent feedback')


    @commands.command(name="request")
    async def request(self,ctx,*, content: str):
        """`誰でも`"""
        e = discord.Embed(title='request', color=0x00aaff)
        channel = self.bot.get_channel(746519843754344560)
        if channel is None:
            return

        e.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
        e.description = content
        e.timestamp = ctx.message.created_at

        if ctx.guild is not None:
            e.add_field(name='Server', value=f'{ctx.guild.name} (ID: {ctx.guild.id})', inline=False)

        e.add_field(name='Channel', value=f'{ctx.channel} (ID: {ctx.channel.id})', inline=False)
        e.set_footer(text=f'Author ID: {ctx.author.id}')

        await channel.send(embed=e)
        await ctx.send(f'{ctx.tick(True)} Successfully sent feedback')

def setup(bot):
    bot.add_cog(report(bot))