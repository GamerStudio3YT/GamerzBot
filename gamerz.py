import discord
import asyncio
from discord.ext import commands
import os
import logging
from discord import Member
from discord.ext.commands import Bot, has_permissions, CheckFailure, BadArgument

bot = commands.Bot(command_prefix = "sb.")
bot.remove_command("help")
WELCOME_CHANNEL_ID = 724628596676886589
LEAVE_CHANNEL_ID = 724628622236844173

#bot start and status
@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

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
    await ctx.send("""This Bot is Under Development""")

#ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

#token and run
bot.run(os.environ['Gamerz-Token'])
