import discord
import asyncio
from discord.ext import commands
import os
import logging
from discord import Member
from discord.ext.commands import Bot, has_permissions, CheckFailure, BadArgument

bot = commands.Bot(command_prefix="gz.")
bot.remove_command("help")
GAMERZ_BOT_ID = 717799015277789275

# bot start and status
@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    bot.loop.create_task(status_task())

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game("gz.help"), status=discord.Status.online)
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game("Official Server Link: https://www.discord.gg/gwkqq7j"), status=discord.Status.online)
        await asyncio.sleep(8)


async def on_disconnect(self):
    print("bot disconnected")


# Discord Bot List Api
# async def apiPost():
# servers = list(client.servers)
# numServers = len(client.servers)

# URL = 'https://discordbotlist.com/api/v1/bots/:id/stats'
# servdata = {'guilds': int(numServers)}
# authorization = {'Authorization': 'NzE3Nzk5MDE1Mjc3Nzg5Mjc1.XuO_EA.NmQYK003iw-VzTeV_e7cEaBJ9fM'}

# x = requests.post(URL, headers=authorization, data="servdata")
# print(x.text)

# help command
@bot.command()
async def help(ctx):
    await ctx.send("""
    Do you want the help command to be sent in your dm or in this channel? \n
If you want the help command to be sent in your dm then type **gz.helpdm**
If you want the help command to be sent in this channel then type **gz.helpchannel**""")


# help command dm
@bot.command()
async def helpdm(ctx):
    await ctx.send("Help command has been sent to your dm")

    embed = discord.Embed(
        title="Gamerz Command Lists",
        description="""
        This bot prefix is gz.
        gz.help
        gz.clear
        gz.ping
        These are the commands. More commands will be added soon. I hope you enjoy this bot

        Links:
        Gamerz Add link: https://discordbotlist.com/bots/gamerz
        Gamerz Bot Offical Server: https://www.discord.gg/gwkqq7j

        This bot is created by Gamer Studio 3#6531""", color=0x22a7f0)

    await ctx.author.send(embed=embed)


# help command channel
@bot.command()
async def helpchannel(ctx):
    embed = discord.Embed(
        title="Gamerz Command Lists",
        description="""
        This bot prefix is gz.
        gz.help
        gz.clear
        gz.ping
        These are the commands. More commands will be added soon. I hope you enjoy this bot

        Links:
        Gamerz Add link: https://discordbotlist.com/bots/gamerz
        Gamerz Bot Offical Server: https://www.discord.gg/gwkqq7j

        This bot is created by Gamer Studio 3#6531""", inline=false, color=0x22a7f0)

    await ctx.send(embed=embed)


# ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


# clear command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count=3):
    await ctx.channel.purge(limit=count, check=is_not_pinned)
    await ctx.channel.send(f'{count} message(s) has been cleared')


# cheat code (delete or clear message without needing the permission)
@bot.command()
async def cheatcode101(ctx, count=3):
    await ctx.channel.purge(limit=count)

#token and run
bot.run(os.environ['Gamerz-Token'])
