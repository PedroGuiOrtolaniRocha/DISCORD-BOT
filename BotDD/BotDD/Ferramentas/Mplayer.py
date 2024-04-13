from discord import FFmpegOpusAudio
import BotDD.Ferramentas.musica as musica
import asyncio
import BotDD.Ferramentas.lixo as lixo
import BotDD.Ferramentas.Cards as Cards
from colorama import init, Fore

init()

cor = {
    'amarelo': Fore.YELLOW,
    'vermelho': Fore.RED,
    'verde': Fore.GREEN,
    'reset': Fore.RESET
    }

async def tocar(context,voice,fila,filap):
    print(f'vou fazer o download de {fila[0]}')                        
                
    musica.main(fila[0])
    music = musica.newest_wav_filename()
    source = FFmpegOpusAudio(music, before_options="-guess_layout_max 0")
    urlemb =  musica.url(fila[0])
    tempos = [musica.pegamin(urlemb), musica.pegaseg(urlemb)]
   
    if tempos[1] < 10:
        
        tempos[1] = f'{tempos[1] :02d}'
                        
    tempo = f'{tempos[0]}:{tempos[1]}'                   
    card = Cards.cardyt(
    link = urlemb, titulo= musica.pegatitle(urlemb),
    desc= musica.pegacan(urlemb) + f'\n            Views: {musica.pegaview(urlemb)}',
    thumb = musica.pegathumb(urlemb), 
    tempo= tempo
    )
    
    player = voice.play(source, after = print(f'Tocando: {cor["verde"]}{musica.pegatitle(urlemb)}{cor["reset"]}, em {str(voice.channel)} a pedido de {cor["amarelo"]}{context.message.author.name}{cor["reset"]}'))

    await context.send(embed = card)

    while voice.is_playing():
    
        await asyncio.sleep(1)
                        
    if not voice.is_playing():
        
        print('acabou o som')
        
        try:
        
            fila.pop(0)
            filap.pop(0)
            lixo.lixo()

        except PermissionError:
        
            print(f'{musica.newest_wav_filename()} esta em uso e não foi apagado.')

        except IndexError:
        
            print('lista vazia')


