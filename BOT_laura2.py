import discord
import random
from discord.ext import commands

TOKEN = 'NDUwNDk1NDE2NzU3MTI1MTMx.De0NbA.qfwYZoomqN8TJgSPSxdvp3zmcBs'

bot = commands.Bot(command_prefix='!', description='I am Laura, except a bot.')
bot.remove_command('help')
insults = ['ur mum', 'dumb cunt', 'ill eat ur dog', 'oi fuck u too m8', 
'shut up old hag', 'suck my nonexistent saggy weiner', 'go to school kid',
'u 18 yet kid?', 'https://media.giphy.com/media/l4Fsly71gEOtGvLQA/giphy.gif']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context = True)
async def hello(ctx):
    member = ctx.message.author

    if member.name == 'Villucian':
        string = 'love u beeb'
    elif member.name == 'laura':
        string = 'hey it me :egg: '
    else:
        string = 'hey {0.joined_at} waddup'.format(member)
    await ctx.send(string)

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="BOT laura", description="Timid bot.", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="laura")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    # embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="BOT laura", description="Shy bot. List of commands are:", color=0xeee657)
    embed.add_field(name="!hello", value="Gives a nice greet message", inline=False)
    embed.add_field(name="!cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="!info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="!commands", value="Gives this message", inline=False)
    embed.add_field(name="!joined", value="Gives the time the member joined", inline=False)
    embed.add_field(name="!fucku", value="try me bich", inline=False)

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def joined(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author

    await ctx.send('{0} joined at {0.joined_at}'.format(member))

@bot.command()
async def fucku(ctx):
    comeback = insults[random.randint(0,len(insults) - 1)]
    await ctx.send(comeback)

bot.run(TOKEN)