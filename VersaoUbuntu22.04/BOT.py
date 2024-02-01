import discord
import discord.voice_client
from discord.ext import commands
import os
from BotDD.configs import pega_info, salva_info
import BotDD.Ferramentas.lixo as lixo
from colorama import init, Fore
import sys 

init()

robo = pega_info()

token = robo['senha']

salva_info(robo)


cor = {
    'amarelo': Fore.YELLOW,
    'vermelho': Fore.RED,
    'verde': Fore.GREEN,
    'reset': Fore.RESET
    }

intents = discord.Intents.all()

client = commands.Bot(command_prefix=robo['prefixo'], intents=intents)


async def load_extensions():    
    cogs = os.listdir('BotDD/cogs')
    
    for i in cogs:
        if i != '__pycache__':
            await client.load_extension('BotDD.cogs.'+i[:-3])

        
@client.event
async def on_ready():
    
    lixo.lixo()

    print(f'{cor["verde"]}O bot {str(client.user)[:-5]} ta ON ^_^{cor["reset"]}, usando {cor["amarelo"]}{client.command_prefix}{cor["reset"]} para interagir.')

    print(f'estou nos {cor["vermelho"]}servers{cor["reset"]}:')
    
    for server in client.guilds:
    
        print(f'{cor["vermelho"]}{server}{cor["reset"]} com {cor["amarelo"]}{server.member_count}{cor["reset"]} membros')

    await load_extensions()

def start():    
    client.run(token, log_handler=None)

start()
