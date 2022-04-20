import discord
import asyncio 
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import urllib.parse
from urllib.error import HTTPError
from datetime import datetime, timezone, timedelta
import json
import qrcode
import asyncio 
import os
import requests
import keep_alive
from discord_slash import cog_ext
from core.cog_core import cogcore

class ping(cogcore):
  @cog_ext.cog_slash(name="ping",description="return bot latency")
  async def _ping(self,ctx):
    await ctx.send(f"pong! ({self.bot.latency*1000} ms)")

def setup(bot):
  bot.add_cog(ping(bot))
