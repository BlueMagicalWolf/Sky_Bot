import discord
from discord.ext import commands
import random
import subprocess
import os
import sys
BadID = 'NONE'
ClusterID = os.getenv('Cluster_ID')
DiscordToken = os.getenv('Discord_Token')
RevoltToken = os.getenv('Revolt_Token')

LOWID = '0'
HIGHID = '16'

print("ClusterID: ",ClusterID)
print("DiscordToken: ",DiscordToken)
print("RevoltToken: ",RevoltToken)

try:
    int(ClusterID)
    print("ID is a number!")
    IsClusterIDNum = 'TRUE'
    if LOWID <= ClusterID <= HIGHID:
        print("Number is Valid!")
        IDVALID = 'TRUE'
    else:
        print("Number isn't Valid!!! ERROR")
        IDVALID = 'FALSE'
except ValueError:
    print("Error! Invalid ID detected,ID is not a number! terminating...")
    IsClusterIDNum = 'FALSE'

D1 = 'ClusterID: ' + ClusterID
D2 = '\nDiscordToken: ' + DiscordToken
D3 = '\nRevoltToken: ' + RevoltToken
D4 = '\nIsClusterIDNum: ' + IsClusterIDNum
D5 = '\nIDVALID: ' + IDVALID
T = [D1, D2, D3, D4, D5]
DATA = '\n'.join(T)
print(DATA)


description = '''UwU'''
activity = discord.Activity(type=discord.ActivityType.listening, name="Hi")
intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='?', description=description, activity=activity, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined in {member.joined_at}')
    
@bot.command()
async def Update(ctx):
    await ctx.send(f'Gonna update now, bye!')
    subprocess.run(["bash", "/usr/src/app/src/update.sh"])
    exit()

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


bot.run(DiscordToken)
