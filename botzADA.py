from turtle import color, title
import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN_DISCORD = os.getenv("TOKEN")

client = commands.Bot(command_prefix= "!")
client.remove_command('help')

@client.command(name='hello')
async def hello(context):
    author = context.message.author
    await author.send('Hi, i hope your day is going phenomenal!')

@client.command()
async def join(context):
    if context.author.voice:
        channel = context.author.voice.channel
        await channel.connect()
    else:
        await context.send("Você precisa entrar em um canal antes de me chamar!")

@client.command()
async def leave(context):
    if context.voice_client:
        await context.voice_client.disconnect()
        await context.send("Saindoooo!")
    else:
        await context.send("Eu nem tô em um canal PÔ!")

@client.command()
async def teste(context):
    embed = discord.Embed(title = 'Ingridt diria...', color = 0xFFFFCB)

    embed.add_field(name= '"Dias de luta, dias de derrota"', value="Ingridt, 23/02/2022")
    await context.message.channel.send(embed=embed)

@client.command()
async def novoteste(context):

    phrases = {
        '“Dias de luta, dias de derrota”': 'Ingridt, 23/02/2022',
        '“Coachs (...) são essenciais”': 'Ingridt, 20/02/2022',
        '“Vocês são os melhores em serem vcs e estão aqui por isso”': 'Ingridt, 21/02/2022',
    }

    random_phrase = random.choice(list(phrases.keys()))
    date = phrases[random_phrase]

    embed = discord.Embed(title = 'Ingridt diria...', color = 0xFFFFCB)

    embed.add_field(name = random_phrase, value = date)
    await context.message.channel.send(embed=embed)

@client.command(name="ingridt")
async def ingridt(context):
    
    phrases = {
        '“Dias de luta, dias de derrota”': 'Ingridt, 23/02/2022',
        '“Coachs (...) são essenciais”': 'Ingridt, 20/02/2022',
        '“Vocês são os melhores em serem vcs e estão aqui por isso”': 'Ingridt, 21/02/2022',
    }

    color = "#FFFFCB"
    random_phrase = random.choice(list(phrases.keys()))
    date = phrases[random_phrase]

    myEmbed = discord.Embed(title='Teste 1', description='Teste 2', color=color)
    myEmbed.set_footer(text="teste 3")
    myEmbed.set_author(name="teste 4")

    await context.message.channel.send(embed=myEmbed)

    #embed = discord.Embed(title= date, description= random_phrase, color= embed_color)
    #await context.message.channel.send(embed=embed)

    #await context.channel.send(embed=embed)

client.run(TOKEN_DISCORD)