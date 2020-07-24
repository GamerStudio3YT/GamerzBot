import discord
import asyncio
import requests
import aiohttp
from discord.ext import commands

bot = commands.Bot(command_prefix = "gz.")
bot.remove_command("help")
WELCOME_CHANNEL_ID = 724628596676886589
LEAVE_CHANNEL_ID = 724628622236844173
GAMERZ_BOT_ID = 717799015277789275

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
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count = 3):
    await ctx.channel.purge(limit=count, check=is_not_pinned)
    await ctx.channel.send(f'{count} message(s) has been cleared')

#cheat code (delete or clear message without needing the permission)
@bot.command()
async def cheatcode101(ctx, count = 3):
    await ctx.channel.purge(limit=count)

@bot.command()
async def ruletemp1(ctx):
    await ctx.send("""
@everyone Welcome to The Sticktuber Community Server. Before chatting please read these important rules. You must agree and respect the server rules. You also must agree and respect DISCORD COMMUNITY GUIDELINES and DISCORD TERMS OF SERVICE.

Here is the link to DISCORD COMMUNITY GUIDELINES: https://discordapp.com/guidelines 

Here is the link to DISCORD TERMS OF SERVICE: https://discordapp.com/terms
Server Rules | Created: 12/04/2019 | Updated: Not Updated Yet

Server Rules:
- 1. Any kind of NSFW and +18 content is forbidden in my server. (Strictly Forbidden)
- 2. No fake and alt account in my server. (Strictly Forbidden)
- 3. No spamming or raiding. 
- 4. No dating in this server. 
- 5. This server is private. Only gamers, stickman animators, animators, fan of stickman animation or normal animation are allowed in this server.
- 7. You are not allowed to call me unless you take my permission. 
- 8. You are allowed to dm me if you have complains or problems in my server. You can also dm me if you want to be my friend!
- 9. Don't be toxic, rude, violent, racist, and no bullying, or harassment and no cursing. No bad words. Don't annoy any users or say annoying words to the users. (Strictly Forbidden)
- 10. Respect each other.
- 11. Don't mention or ping anyone pointlessly. 
- 12. No Fighting or arguing in this server. Please dm me for any problems.
- 13. Please don't threat anybody in this server. Even if it's fake. (Strictly Forbidden)
- 14. Do not download pictures in #✩🎨✩artworks. It belongs to the creator of the artwork. You must take the permission from the creator of the artwork before downloading it. (Strictly Forbidden)
+ 15. Please use every channel correctly. For example: Don't advertise on #【💬】main-chat. Use #【📡】advertisements to advertise. 
- 16. No Religious Confidence.
- 17. Don't swear a lot or swear to someone.
- 18. Please don't scream and disturb others in Voice Channels.
- 19. No Irritating.
- 2. Sending Viruses Or Malicious Links Is Strictly Forbidden.
- 3. Don't use middle finger emoji and don't use rude emojis. (Strictly Forbidden)
- 4. No impersonating anyone.
- 5. Moderators and Staffs and Helpers and Friends must follow the rules. Any Members must follow the rules even if they have high role.
- 6. Don't abuse your power (This rule is for Moderator, Staff, Owner Helper, trial staff)
- 7. Don't beg me to give you staff, moderator or owner helper role.
- 8. Don't beg me to accept your staff application.
- 9. No pranking and no fooling. Some users don't like pranks or fools.
- 10. No adult (18+), explicit, inappropriate or controversial messages (Strictly Forbidden)
- 11. Don't send any nitros in this server even if it's not expired or fake. You should dm me before sending nitro in this server.
- 12. If you want to host a giveaway then the giveaway should be real, legit and you should dm me first before hosting a giveaway.
- 12. No inappropriate and nsfw picture profile or name. (For example: Hentai profile picture with the name Fuck#0000)
- 13. Do NOT make fun of anyone in this server.
- 14. Don't send personal information or send other members personal information (Address, Phone Number, IP Address, Birthday, etc.). Sending personal informations can lead to privacy leaking or getting hacked.
- 15. You should agree with my rules. If you don't agree with the rules then leave this server or tell me why.
- 16. Don't ping @ everyone in ☆📡☆advertisements.
- 17. Don't send scam advertisements like fake free nitro server, scam links or etc. (Strictly Forbidden)

I hope you read all the rules and i hope you have fun in this server!
"""
)




#token and run
token = read_token()
bot.run(token)