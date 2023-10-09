from random import choice
from random import randint
from discord.ext import commands
from BotDD.Ferramentas.Cards import cardajuda

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name= 'xinga')
    async def xinga(self, context):


        nome = context.author.nick

        if nome ==  None:

            nome = context.author.name
        
        xingamentos = [
        f'vai sin fude {nome}', 
        f'Ratomanocu {nome}', 
        f'{nome} fede socialmente',
        f'no geral {nome} é noggers',
        f'por acaso {nome} comeu um pacote de cabacitos?', 
        f'Em segredo, {nome} é furry', 
        f'{nome}, sua virilha esta criando teias...'
        ]

        xingo = choice(xingamentos)
        print(f'Xingamento numero {xingamentos.index(xingo)+1}, pedido por {nome}')

        await context.send(xingo)

    @commands.command(name= 'ola')
    async def ola(self, context):
        nome = context.author.nick
        await context.message.channel.send('oieee ' + nome)
    
    @commands.command(name= 'ajuda')
    async def comados(self, context):
        card = cardajuda()
        await context.message.channel.send(embed = card)
    
    @commands.command(name= 'bingo')
    async def bingo(self, context, arg, arg2):
        
        arg = int(arg)
        arg2 = int(arg2)
        bingo = randint(1, 1000)
        bingocont = 1
        await context.send(f'Sorteando {arg} numeros entre 1 e {arg2}')

        while bingocont <= arg:
            bingo = randint(1, arg2)
            bingocont += 1
            await context.send(bingo)
           
        if bingocont == arg:
            await context.send('pronto')
        if bingocont >= arg:
            await context.send('pronto!')
        

    
async def setup(bot):
    await bot.add_cog((Chat(bot)))