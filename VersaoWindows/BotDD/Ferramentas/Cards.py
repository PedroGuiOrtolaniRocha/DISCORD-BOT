import discord


def cardyt(link, titulo, desc, thumb, tempo):
    card = discord.Embed(type = 'image', url = link, description= desc, title=titulo,color=discord.Color.brand_red() ) 
    card.set_image(url = thumb)
    card.set_footer(text=f'Tempo de musica: {tempo}')
    return card
    
    
def cardajuda():
    link = 'https://github.com/Pedrones999/BotDD'
    card = discord.Embed(url = link, 
                         description= 'ZéPorva é um bot multifunfional de discord focado em tocar musica\nAinda estou em desenvolvimento e possuo limitações\n**!ajuda** para ajuda',
                         title='Obrigado por usar o bot ^^',
                         color=discord.Color.dark_purple()) 
   
    card.add_field(name = '**Comandos para musica:**',
                    value = "**!p <nome ou link>**: Toca a música escolhida, se ja estiver tocando adiciona na fila.\n"
                    "**!sai**: Faz o bot sair do canal de voz.\n"
                    "**!pause**: Pausa a música.\n"
                    "**!volta**: Volta a música.\n"
                    "**!para**: Para a música e reseta a fila.\n"
                    "**!fila**: Mostra a fila.\n", 
                    inline = False)
  
    card.set_footer(text=f'Para ajudar a desenvolver o projeto entre em {link}')
    return card


