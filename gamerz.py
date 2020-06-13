import discord
import asyncio
import os
import json
from discord.ext import commands

#prefixes change database
def get_prefix(bot, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix)

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


#prefix change

@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "gz."

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def changeprefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f"Prefix has been changed to {prefix}")

bot.run(os.environ['Gamerz-Token'])
