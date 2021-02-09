import textwrap
from discord import Intents
import typing
import aiohttp
from datetime import datetime, timedelta
from typing import Optional

from typing import Union
import time

import platform
from discord.ext import commands
from platform import python_version
from discord import __version__ as discord_version
from asyncio import sleep
import json
from discord.utils import get

from collections import OrderedDict, deque, Counter
import datetime
import os

import asyncio, discord
import random
import secrets
from io import BytesIO
import ast
import psutil
import functools
import inspect
from discord.ext.commands import clean_content
from discord import Embed
from discord.ext.commands import Cog
import sys
import json
import traceback
import wikipedia
import io
from contextlib import redirect_stdout
import re

import tracemalloc


class everyone(commands.Cog):
    """
    誰でも使えるコマンドです
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def timer(self, ctx, seconds):
        try:
            secondint = int(seconds)
            if secondint > 300:
                await ctx.send("300秒まで可能です")
                raise BaseException
            if secondint < 0 or secondint == 0:
                await ctx.send("I dont think im allowed to do negatives")
                raise BaseException
            message = await ctx.send("Timer: " + seconds)
            while True:
                secondint = secondint - 1
                if secondint == 0:
                    await message.edit(new_content=("Ended!"))
                    break
                await message.edit(new_content=("Timer: {0}".format(secondint)))
                await asyncio.sleep(1)
            await ctx.send(ctx.message.author.mention + " カウントダウン")
        except ValueError:
            await ctx.send("Must be a number!")

    @commands.command(name="say", aliases=["echo"], description="```任意の文章を送信します。```")
    async def say(self, ctx, *, arg):
        """`豆腐がしゃべります`"""
        await ctx.message.delete()

        if "<@" in arg or "@everyone" in arg or "@here" in arg:
            await ctx.send("```メンションはしないでください。```")
        else:
            await ctx.send(arg)




    @commands.command(description="お豆腐サーバー")
    async def official(self, ctx):
        """`誰でも`"""
        embed = discord.Embed(title="Zosuserver", url="https://discord.gg/589NpX9",description="豆腐のサーバー", color=0x00aaff)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/803281008703176706/9327faa387255c25d6cb69d70a839f51.png?size=1024")
        embed.add_field(name="何かあればこちらへ", value="by creater", inline=True)
        embed.set_footer(text="豆腐")
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        """`誰でも`"""
        msg = await ctx.send("`Pinging bot latency...`")
        times = []
        counter = 0
        embed = discord.Embed(title="More information:", description="Pinged 4 times and calculated the average.",
                              colour=discord.Colour(value=0x36393e))
        for _ in range(3):
            counter += 1
            start = time.perf_counter()
            await msg.edit(content=f"Pinging... {counter}/3")
            end = time.perf_counter()
            speed = round((end - start) * 1000)
            times.append(speed)
            embed.add_field(name=f"Ping {counter}:", value=f"{speed}ms", inline=True)

        embed.set_author(name="Pong!")
        embed.add_field(name="Bot latency", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="Average speed",
                        value=f"{round((round(sum(times)) + round(self.bot.latency * 1000)) / 4)}ms")
        embed.set_footer(text=f"Estimated total time elapsed: {round(sum(times))}ms")
        await msg.edit(content=f":ping_pong: **{round((round(sum(times)) + round(self.bot.latency * 1000)) / 4)}ms**",
                       embed=embed)


def setup(bot):
    bot.add_cog(everyone(bot))