import discord
from discord.ext import commands
import asyncio
import random

client = commands.Bot(command_prefix=">", case_insensitive=True)

msg_id = None
msg_user = None

@client.event
async def on_ready():
    print(f'Bot {client.user.name} online')

@client.command()
async def ContaSimples(ctx,num1,num2):
  await ctx.send(f'hmm {int(num1) + int(num2)}')

@client.command()
async def clear(ctx, amount = 5):
  await ctx.channel.purge(limit=amount)



@client.command()
async def moeda(ctx):
  moeda = random.randint(1,2)
  if moeda == 1:
    mensagem = await ctx.send("Moeda jogada, o resultado foi: Cara 😄")
    await mensagem.add_reaction("😄")

  if moeda == 2:
    mensagem = await ctx.send("moeda jogada, o resultado foi: coroa 👑")
    await mensagem.add_reaction("👑")
  else:
    await ctx.send("Voce nao esta liberado para usar este comando")



@client.command()
async def enquete(ctx,title,valor1,valor2):
  if ctx.author.id == 498306559017746462:
    embed = discord.Embed(
      title = title,
      color = 0xA549CA,
      description = f"| {valor1} | Ou | {valor2} |"
    )
    embedenviar = await ctx.send(embed=embed)
    await embedenviar.add_reaction("1️⃣")
    await embedenviar.add_reaction("2️⃣")

@client.command()
async def musica(ctx):
  try:
    canal = ctx.message.author.voice.channel
    await canal.connect()
  except:
    await ctx.send("Se conecte a um canal de voz para poder usar")

client.run('ODY0Njg4NzY0NzUxNDQ2MDI3.YO5GKg.MC51dAXapi17cyvMKx0-umtHYIA')