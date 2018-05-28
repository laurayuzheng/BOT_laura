import discord

TOKEN = 'NDUwNDk1NDE2NzU3MTI1MTMx.De0NbA.qfwYZoomqN8TJgSPSxdvp3zmcBs'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!HELLO'):
        if message.author.name == 'Villucian':
            msg = 'love u beeb'.format(message)
        elif message.author.name == 'laura':
            msg = 'hey it me :egg: '.format(message)
        else:
            msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)