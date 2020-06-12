import discord
import asyncio
import json
from discord.ext import commands

#prefixes change database
def get_prefix(bot, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix)

#token reader
def read_token():
    with open("gamerz-token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

#bot start and status
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("gz.help"))
    print('Logged in as {0.user}'.format(bot))

#ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

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
async def changeprefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f"Prefix has been changed to {prefix}")


#token and run
token = read_token()
bot.run(token)