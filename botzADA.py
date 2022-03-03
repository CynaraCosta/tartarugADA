import discord
from discord.ext import commands
import random
from token import *


client = commands.Bot(command_prefix= "!")
client.remove_command('help')

@client.command(name='hello')
async def hello(context):
    author = context.message.author
    await author.send('Hi, i hope your day is going phenomenal!')

@client.command(name="ingridt")
async def ingridt(context):
    
    phrases = {
        '“Dias de luta, dias de derrota”': 'Ingridt, 23/02/2022',
        '“Coachs (...) são essenciais”': 'Ingridt, 20/02/2022',
        '“Vocês são os melhores em serem vcs e estão aqui por isso”': 'Ingridt, 21/02/2022',
    }

    colors = ["#FFA8B8", "#B5DCF9", "#F6ECAB", "#F6ECAB", "#BDF6E3", "#E3D2F4"]

    random_phrase = random.choice(list(phrases.keys()))
    date = phrases[random_phrase]
    embed_color = random.choice(colors)

    myEmbed = discord.Embed(title='Teste 1', description='Teste 2', color=embed_color)
    myEmbed.set_footer(text="teste 3")
    myEmbed.set_author(name="teste 4")

    await context.message.channel.send(embed=myEmbed)

    #embed = discord.Embed(title= date, description= random_phrase, color= embed_color)
    #await context.message.channel.send(embed=embed)

    #await context.channel.send(embed=embed)

client.run(TOKEN)