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
  if ctx.author.id == 498306559017746462:
    moeda = random.randint(1,2)
    if moeda == 1:
      mensagem = await ctx.send("Moeda jogada, o resultado foi: Cara 😄")
      await mensagem.add_reaction("😄")

    if moeda == 2:
      mensagem = await ctx.send("moeda jogada, o resultado foi: coroa 👑")
      await mensagem.add_reaction("👑")
  else:
    await ctx.send("Voce nao esta liberado para usar este comando")

# @client.command()
# async def CargoCores(ctx):
#    if ctx.author.id == 498306559017746462:
#     embed = discord.Embed(
#       title = "Escolha sua cor!",
#       color = 0xA549CA,
#       description = "-Vermelho\n"
#                     "-Azul\n"
#                     "-Amarelo\n"
#                     "-Verde\n"
#                     "-Roxo\n"
#     )
#     botmsg = await ctx.send(embed=embed)

#     await botmsg.add_reaction("🔴")
#     await botmsg.add_reaction("🔵")
#     await botmsg.add_reaction("🟡") #amarelo
#     await botmsg.add_reaction("🟢") #verde
#     await botmsg.add_reaction("🟣") #roxo

#     global msg_id
#     msg_id = botmsg.id
#     global msg_user
#     msg_user = ctx.author

# @client.event
# async def on_reaction_add(reaction, user):
#   msg = reaction.message

#   if reaction.emoji == "🔴" and msg.id == msg.id:
#     await user.add_roles(discord.utils.get(user.guild.roles, name="vermelho"))
  
# @client.event
# async def on_reaction_remove(reaction, user):
#   msg = reaction.message

#   if reaction.emoji == "🔴" and msg.id == msg.id:
#     await user.remove_roles(discord.utils.get(user.guild.roles, name="vermelho"))


client.run('ODY0Njg4NzY0NzUxNDQ2MDI3.YO5GKg.MC51dAXapi17cyvMKx0-umtHYIA')