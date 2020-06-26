import discord
import asyncio
import os
from discord.ext import commands

bot = commands.Bot(command_prefix = "gz.")
bot.remove_command("help")
WELCOME_CHANNEL_ID = 724628596676886589
LEAVE_CHANNEL_ID = 724628622236844173

#bot start and status
@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    bot.loop.create_task(status_task())

def is_not_pinned(mess):
    return not mess.pinned

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Stream("Under Maintenance"), status=discord.Status.online)

#Welcome Command
@bot.event
async def on_member_join(member):
    if not member.bot:
        welcomechannel = bot.get_channel(WELCOME_CHANNEL_ID)
        await welcomechannel.send(f"{member.mention} has joined the server. Thank you for joining the server. I hope you have a great time in my server!")
        print(f"{member} has joined the server.")
        embed = discord.Embed(
            title="Welcome to Gamer Studio 3 Community Server and to Gamer Studio 3 Youtube Channel".format(
                member.name),
            description="""Hi Member. Welcome to The Sticktuber Community. Don't forget to read the rules before chatting. 
            I hope you have a great time in the server. If you have any complains or suggestion then you can dm me at Gamer Studio 3#6531 and 
            if you got banned by mistake and you want to appeal then email me at channel.gamerstudio3@gmail.com """, color=0x22a7f0)

        if not member.dm_channel:
            await member.create_dm()
            await member.dm_channel.send(embed=embed)

#Leave Command
@bot.event
async def on_member_remove(member):
    leavechannel = bot.get_channel(LEAVE_CHANNEL_ID)
    await leavechannel.send(f"{member.mention} has left the server. We hope you will come back again :(")
    print(f"{member} has left the server")

#help command
@bot.command()
async def help(ctx):
    await ctx.send("""Do you want the help command to be sent in your dm or in this channel?
    If you want the help command to be sent in your dm then type gz.helpdm
    If you want the help command to be sent in this channel then type gz.helpchannel""")

#help command dm
@bot.command()
async def helpdm(ctx):
    await ctx.send("Help command has been sent to your dm")

    embed = discord.Embed(
        title="Gamerz Command Lists".format(member.name),
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

    if not member.dm_channel:
        await member.create_dm()
        await member.dm_channel.send(embed=embed)

#help command channel
bot.command()
async def helpchannel(ctx):
    await ctx.send(embed=embed)

    embed = discord.Embed(
        title="Gamerz Command Lists".format(member.name),
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

#ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

#clear command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count = 3):
    await ctx.channel.purge(limit=count, check=is_not_pinned)
    await ctx.channel.send(f'{count} message(s) has been cleared')

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, CheckFailure):
         await bot.send_message(ctx.message.channel, "You do not have manage messages permission")

    if isinstance(error, commands.BadArgument):
        await ctx.send("""Couldn't delete the message. ```Reason: Bad Argument```
        If you still have this issue then contract me (Gamer Studio 3#6531) or send me an email in gamerzbot1@gmail.com""")

    else:
        raise error

#cheat code (delete or clear message without needing the permission)
@bot.command()
async def cheatcode101(ctx, count = 3):
    await ctx.channel.purge(limit=count)

bot.run(os.environ['Gamerz-Token'])
