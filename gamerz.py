import discord
import asyncio
import os
from discord.ext import commands

bot = commands.Bot(command_prefix = "gz.")

#token reader
def read_token():
    with open("gamerz-token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

#bot start and status
@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    bot.loop.create_task(status_task())

def is_not_pinned(mess):
    return not mess.pinned

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game("gz.help"), status=discord.Status.online)
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game("Official Server Link: https://www.discord.gg/gwkqq7j"), status=discord.Status.online)
        await asyncio.sleep(8)

#ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count = 3):
    await ctx.channel.purge(limit=count, check=is_not_pinned)
    await ctx.channel.send(f'{count} message(s) has been cleared')

@bot.command()
async def cheatcode1(ctx, count = 3):
    await ctx.channel.purge(limit=count)

bot.run(os.environ['Gamerz-Token'])
