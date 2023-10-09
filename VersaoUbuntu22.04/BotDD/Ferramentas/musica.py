import youtube_dl
import yt_dlp as youtube_dl
import os
from pytube import Search
from pytube import YouTube
from glob import glob

list_of_wav = glob('./*.wav')


def download_audio(yt_url):

    ydl_opts = {

        'format': 'bestaudio/best',
        'postprocessors': [{
            
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        
        }],
        }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        
        ydl.download([yt_url])

def main(arg):

    arg = ''.join(arg)
        
    
    if not arg.startswith('https://www.youtube.com/watch?v='):
        
        arg = ''.join(arg)
        arg = arg.removeprefix("['") and arg.removesuffix("']")
        pesq = Search(arg)
        idcru = (str(pesq.results[0])).split()
        idtrat = idcru[2].removeprefix('videoId=').removesuffix('>')
        yt_url = ('https://www.youtube.com/watch?v=' + idtrat)
        download_audio(yt_url)
    
    
    else:
        
        yt_url = arg
        download_audio(yt_url)

def url(arg):

    if not arg.startswith('https://www.youtube.com/watch?v='):
        
        pesq = Search(arg)
        idcru = (str(pesq.results[0])).split()
        idtrat = idcru[2].removeprefix('videoId=').removesuffix('>')
        yt_url = ('https://www.youtube.com/watch?v=' + idtrat)
    
    else: yt_url = arg
    return yt_url



def newest_wav_filename():
    arquivos = os.listdir('.')
    musicas = []
    
    for arquivo in arquivos:
        if arquivo.endswith('.wav'):
            musicas.append(arquivo)

    return max(musicas, key=os.path.getctime)


def pegatitle(arg):
    
    url(arg)
    yt = YouTube(arg)
    return yt.title

def pegathumb(arg):
    
    yt = YouTube(arg)
    return yt.thumbnail_url

def pegamin(arg):
    
    yt = YouTube(arg)
    temp = (yt.length // 60)
    return temp

def pegatempo(arg):
    
    yt = YouTube(arg)
    temp = yt.length
    return temp

def pegaseg(arg):
    
    yt = YouTube(arg)
    temp = (yt.length % 60)
    return temp

def pegacan(arg):
    
    yt = YouTube(arg)
    can = yt.author
    return can
    
def pegaview(arg):
    
    yt = YouTube(arg)
    view = yt.views
    return view

