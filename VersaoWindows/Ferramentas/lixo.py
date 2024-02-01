import os
import BotDD.Ferramentas.musica as musica

def lixo():
    pasta = '.'
    arquivos = os.listdir(pasta)
    ext = 'wav'
    ext2 = 'mp3'
    ext3 = 'webm'

    for i in arquivos:

        if not ext:
            i = i
        if not ext2:
            i = i
        else:
            extensao = i.split('.')[-1]
            if extensao in ext or extensao in ext2 or extensao in ext3:
                os.remove(i)


def lixospec():
    pasta = '.'
    arquivos = os.listdir(pasta)
    ext = 'wav'
    for i in arquivos:

        if not ext:
            i = i

        else:
            extensao = i.split('.')[-1]
            if extensao in ext and not musica.newest_wav_filename():
                os.remove(i)

