import discord
import asyncio
import requests
import aiohttp
from discord.ext import commands
import os
import logging
from discord import Member
from discord.ext.commands import Bot, has_permissions, CheckFailure, BadArgument

bot = commands.Bot(command_prefix = "gz.")
bot.remove_command("help")
WELCOME_CHANNEL_ID = 724628596676886589
LEAVE_CHANNEL_ID = 724628622236844173
GAMERZ_BOT_ID = 717799015277789275

#token reader
def read_token():
    with open("GamerzBotToken.txt", "r") as f:
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

async def on_disconnect(self):
    print("bot disconnected")

# Discord Bot List Api
#async def apiPost():
    #servers = list(client.servers)
    #numServers = len(client.servers)

    #URL = 'https://discordbotlist.com/api/v1/bots/:id/stats'
    #servdata = {'guilds': int(numServers)}
    #authorization = {'Authorization': 'NzE3Nzk5MDE1Mjc3Nzg5Mjc1.XuO_EA.NmQYK003iw-VzTeV_e7cEaBJ9fM'}

    #x = requests.post(URL, headers=authorization, data="servdata")
    #print(x.text)

#Welcome Command
@bot.event
async def on_member_join(member):
    if not member.bot:
        welcomechannel = discord.utils.get(member.guild.channels, id=WELCOME_CHANNEL_ID)
        await welcomechannel.send(f"{member.mention} has joined the server. Thank you for joining the server. I hope you have a great time in my server!")
        print(f"{member} has joined the server.")
        embed = discord.Embed(
            title="Welcome to The Sticktuber Community Server",
            description="""Hi Member. Welcome to The Sticktuber Community. Don't forget to read the rules before chatting. I hope you have a great time in the server. If you have any complains or suggestion then you can dm me at Gamer Studio 3#6531 and if you got banned by mistake and you want to appeal then email me at channel.gamerstudio3@gmail.com """, color=0x22a7f0)

        if not member.dm_channel:
            await member.create_dm()
            await member.dm_channel.send(embed=embed)

#Leave Command
@bot.event
async def on_member_remove(member):
    leavechannel = discord.utils.get(member.guild.channels, id=LEAVE_CHANNEL_ID)
    await leavechannel.send(f"{str(member)} has left the server. We hope you will come back again :(")
    print(f"{str(member)} has left the server")

#help command
@bot.command()
async def help(ctx):
    await ctx.send("""
    Do you want the help command to be sent in your dm or in this channel? \n
If you want the help command to be sent in your dm then type **gz.helpdm**
If you want the help command to be sent in this channel then type **gz.helpchannel**""")

#help command dm
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

#help command channel
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

#ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

#clear command
@bot.command(name="clear")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count = 3):
    await ctx.channel.purge(limit=count, check=is_not_pinned)
    await ctx.channel.send(f'{count} message(s) has been cleared')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions)

#cheat code (delete or clear message without needing the permission)
@bot.command()
async def cheatcode101(ctx, count = 3):
    await ctx.channel.purge(limit=count)

#ban command

@bot.command(pass_context=True, name="ban", reason=None)
@has_permissions(kick_members=True)
async def ban_command(ctx, *, target: Member):
    if target.server_permissions.administrator:
        await bot.send("Target is an admin")
    else:
        try:
            await bot.ban(target, reason=reason)
            await ctx.send("Banned")
        except Exception:
            await ctx.send("Something went wrong")

#ban error

@ban_command.error
async def ban_error(error, ctx):
    if isinstance(error, CheckFailure):
         await bot.send_message(ctx.message.channel, "You do not have permissions")
    elif isinstance(error, BadArgument):
        await bot.send_message(ctx.message.channel, "Could not identify target")
    else:
        raise error




#token and run
token = read_token()
bot.run(token)