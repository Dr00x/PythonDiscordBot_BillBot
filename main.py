import discord
from discord.ext import commands
import asyncio
import random

client = commands.Bot(command_prefix=">", case_insensitive=True)

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
    await ctx.send("Moeda jogada, o resultado foi: Cara")
  
  if moeda == 2:
    await ctx.send("moeda jogada, o resultado foi: coroa")


client.run('ODY0Njg4NzY0NzUxNDQ2MDI3.YO5GKg.MC51dAXapi17cyvMKx0-umtHYIA')