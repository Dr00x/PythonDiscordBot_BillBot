import discord
from discord.ext import commands
import asyncio

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


client.run('ODY0Njg4NzY0NzUxNDQ2MDI3.YO5GKg.MC51dAXapi17cyvMKx0-umtHYIA')