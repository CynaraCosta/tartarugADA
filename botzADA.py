import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from config import *
import random
import firebase_admin
from firebase_admin import db
from datetime import date
from firebase_admin import credentials
import random
from dotenv import load_dotenv
import os
load_dotenv()

cred = credentials.Certificate(firebase_config)
databaseApp = firebase_admin.initialize_app(cred, {
    'databaseURL' : DatabaseURL
})

TOKEN_DISCORD = os.getenv("TOKEN")

client = commands.Bot(command_prefix= "!")
client.remove_command('help')

ref = db.reference("/")
ref.set({
    "frasesingridt" : {
        "-Ingridt, 21-02-2022" : '“Vocês são os melhores em serem vcs e estão aqui por isso”',
        "-Ingridt, 20-02-2022" : '“Coachs (...) são essenciais”',
        "-Ingridt, 23-02-2022" : '“Dias de luta, dias de derrota”',
    }
})

@client.command(name="frase")
async def frase(context):
    message = str(context.message.content)
    ref2 = db.reference('frasesingridt')
    emp_ref = ref2.push({context.message.author : {"-Indridt, " + str(date.today().strftime("%d-%m-%Y")) : str(message[6:])}})


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
async def ingridt(context):

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

client.run(TOKEN_DISCORD)