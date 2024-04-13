from discord.ext import commands
import shlex
from discord.utils import get
import BotDD.Ferramentas.musica as musica
import BotDD.Ferramentas.lixo as lixo
import BotDD.Ferramentas.Mplayer as Mplayer
import discord
from pytube import Playlist
import asyncio
from BotDD.configs import pega_info
from colorama import init, Fore
import time

init()

robo = pega_info()

prefixo = robo['prefixo']

cor = {
    'amarelo': Fore.YELLOW,
    'vermelho': Fore.RED,
    'verde': Fore.GREEN,
    'reset': Fore.RESET
    }

fila, filap = [], []


class Musica(commands.Cog):
    
    def __init__(self, bot):
        
        self.bot = bot
        self.fila = fila 
        self.filap = filap 

    @commands.command(name= 'p')
    async def entra(self, context,*,arg):
        
        lixo.lixospec()
        pedido = ''.join(arg)

        arg = shlex.split(''.join(arg))
        arg = ' '.join(arg)
        arg = str(arg)
        voice = get(self.bot.voice_clients, guild=context.guild)

        try:
            channel = context.message.author.voice.channel
            voice = await channel.connect(self_deaf = True)
            
        except AttributeError:
            
            return await context.send("Entra na call corno")

        except discord.errors.ClientException:
            
            print('ja estou na CALL')
                
        if arg.__contains__('youtube.com/playlist?list=') or arg.__contains__ ('&list='):

            if arg.__contains__('start_radio'):
                
                await context.send('infelizmente o bot não suporta mix do youtube')
                return
            
            lista = Playlist(arg)
            playlen = len(lista.video_urls)
            print(f'Playlist {lista.title} com {playlen} foi adicionada a pedido de {context.message.author}')
            await context.send(f'adicionando {playlen} faixas da playlist {lista.title}')

            
            for urls in lista.video_urls:
                
                fila.append(urls)
                filap.append(''.join(musica.pegatitle(urls)))
            
        else:
            
            link = musica.url(pedido)
            
            await context.send(f'adicionando {musica.pegatitle(link)}')
            
            fila.append(arg)
            filap.append(musica.pegatitle(link))
            
            time.sleep(1)

            nfila = " \n".join(filap[0:])
            
            print(f'Fila - {cor["amarelo"]}{nfila}{cor["reset"]}')
        
        try:
                
            if voice and voice.is_connected() and not voice.is_playing():
                
                await Mplayer.tocar(context, voice, fila, filap)

                while len(fila) >= 1:

                    await Mplayer.tocar(context, voice, fila, filap)
        
                if len(fila) == 0:

                    await context.send(f'Acabaram as musicas 😟, coloque mais com {prefixo}p')
                    
                    await asyncio.sleep(300)

                    if len(fila) == 0:
                        
                        await voice.disconnect()

                        await context.send('Fiquei triste e quieto, adeus')

        except Exception as e: 
            print('Não consegui tocar') 
            print(e)

    ############ pula ###################

    @commands.command(name= 'pula')
    async def pula(self, context):

        lixo.lixospec()
        voice = get(self.bot.voice_clients, guild= context.guild)
        
        try:

            if voice and voice.is_connected() and voice.is_playing():
                
                voice.stop()
                await asyncio.sleep(1)

                await context.send('Pulando...')

            if not voice.is_playing():

                try:
                    
                    lixo.lixo()     
                    
                except PermissionError:
            
                    print(f'{musica.newest_wav_filename()} esta em uso e não foi apagado.')

        except IndexError:
            
            return await context.send('essa era a  ultima musica 😟')


        except discord.ext.commands.errors.CommandInvokeError:
            
            return context.send('não tem o que pular 😟')

    ############ mostra fila ###################

    @commands.command(name= 'fila')
    async def mfila(self, context):
        
        catalogo = list(enumerate(filap))

        pedidos = []

        for indice, valor in catalogo:
            
            pedidos.append(f'{indice} - {valor}')

        filapedidos ="\n".join(pedidos[1:])
        
        await context.send(f'aqui esta a fila de pedidos, com {len(filap)} faixas:\nTocando - {filap[0]}\n{filapedidos}')
        
        print(f'Tocando - {cor["verde"]}{filap[0]}{cor["reset"]}{cor["amarelo"]}{filapedidos}{cor["reset"]}')

    ############ Sair ###################

    @commands.command(name='sai')
    async def sai(self, context):
        
        try:
        
            voice = get(self.bot.voice_clients, guild=context.guild)
            await voice.disconnect()

        except AttributeError:

            return await context.send("Não to em call corno")

    ############ pause ###################

    @commands.command(name='pause')
    async def pause(self, context):
        
        voice = discord.utils.get(self.bot.voice_clients, guild = context.guild)
        
        if voice.is_playing():
        
            voice.pause()
                
        else:
        
            await context.send('não estou tocando nada')

    ############ volta ###################

    @commands.command(name='volta')
    async def volta(self, context):
        
        voice = discord.utils.get(self.bot.voice_clients, guild = context.guild)

        if voice.is_paused():
          
            voice.resume()
       
        else:
          
            await context.send('não tem nada pausado')

    ############ para ###################

    @commands.command(name='para')
    async def para(self, context):
        
        voice = discord.utils.get(self.bot.voice_clients, guild = context.guild)
        
        if voice.is_playing():
           
            fila.clear()
            filap.clear()
            voice.stop()
            lixo.lixo()
            

        else:
           
            await context.send('não estou tocando nada')
            
async def setup(bot):
    
    await bot.add_cog((Musica(bot)))




