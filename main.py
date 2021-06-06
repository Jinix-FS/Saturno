#--------------- Imports ---------------#

import discord
import whois
import time
import random
import colorama
import os, sys
import datetime
import inputimeout
import requests
import asyncio
import json
import logging
import base64
import io
import language
import webbrowser

#--------------- Foms ---------------#

from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
import pyPrivnote as pn
from gtts import gTTS
from tqdm import tqdm
from time import sleep
from colorama import Fore as Color
from colorama import Style
from inputimeout import inputimeout, TimeoutOccurred
from discord.ext import commands
from datetime import datetime
from discord import Embed, Member
from discord.ext.commands import Cog, command
from typing import Optional
#--------------- Tela De Entrada ---------------#

os.system('clear')


logo55 = (""" 

  ██████  ▄▄▄     ▄▄▄█████▓ █    ██  ██▀███   ███▄    █  ▒█████  
▒██    ▒ ▒████▄   ▓  ██▒ ▓▒ ██  ▓██▒▓██ ▒ ██▒ ██ ▀█   █ ▒██▒  ██▒
░ ▓██▄   ▒██  ▀█▄ ▒ ▓██░ ▒░▓██  ▒██░▓██ ░▄█ ▒▓██  ▀█ ██▒▒██░  ██▒
  ▒   ██▒░██▄▄▄▄██░ ▓██▓ ░ ▓▓█  ░██░▒██▀▀█▄  ▓██▒  ▐▌██▒▒██   ██░
▒██████▒▒ ▓█   ▓██▒ ▒██▒ ░ ▒▒█████▓ ░██▓ ▒██▒▒██░   ▓██░░ ████▓▒░
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ 
░ ░▒  ░ ░  ▒   ▒▒ ░   ░    ░░▒░ ░ ░   ░▒ ░ ▒░░ ░░   ░ ▒░  ░ ▒ ▒░ 
░  ░  ░    ░   ▒    ░       ░░░ ░ ░   ░░   ░    ░   ░ ░ ░ ░ ░ ▒  
      ░        ░  ░           ░        ░              ░     ░ ░   Neox
                                                                    Jinix

""")
print(f"{Color.CYAN}{logo55}")

print(f"\n")

token = input('Digite seu token: ')
prefix = input('Digite seu prefix: ')

print('')

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

for i in tqdm(range(100), "Carregando dados... "):
    sleep(0.02)
    
print('\n')
print('SELFBOT LIGADO')
print('\n')


#--------------- Comando De Ajuda ---------------#

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    url = 'https://jinix-fs.github.io/SaturnoWeb/'
    r = requests.get(url)
    if r.status_code == 200:
        webbrowser.open(url)
        embed = discord.Embed(
            title=" ",
            description=f"""

        [Help Android](https://jinix-fs.github.io/SaturnoWeb/)

        """)
        await ctx.send(embed=embed)

#--------------- Comando Info do server ---------------#

@bot.command()
async def serverinfo(ctx): #se nao me engano nao precisa de permissao 
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " ",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="👑 | Dono", value=owner, inline=True)
  embed.add_field(name="💻 | ID", value=id, inline=True)
  embed.add_field(name="🌍 | Região", value=region, inline=True)
  embed.add_field(name="👤 | Membros", value=memberCount, inline=True)

  await ctx.send(embed=embed)

#--------------- Cmd De Apagar Todas Mensagens ---------------#

@bot.command()
async def apagar(ctx, amount=5): #precisa de permissão
  await ctx.message.delete()
  contador = 0
  while contador <50:
    await ctx.channel.purge(limit=amount)

#--------------- Comando Say ---------------#

@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)

#--------------- Cmd de ver Info de uma pessoa ---------------#

@bot.command() #nao ta pegando vou arrumar e dps atualizo 
async def userinfo(ctx, target: Optional[Member]):
        x = ctx.guild.members
        if target in x:
             roles = [role for role in target.roles]
             embed = discord.Embed(title=" 🔥 Saturno ", colour=discord.Color.blue(), timestamp=datetime.utcnow())

             embed.set_author(name=target.name, icon_url=target.avatar_url)

             embed.set_thumbnail(url=target.avatar_url)

             embed.set_footer(text="      ", icon_url="https://cdn.discordapp.com/attachments/618434755981213716/718861010223497236/kapi-1.png")

             fields = [("**🔖Tag do Discord**", str(target), False),
                   ("**💻 ID do Discord**", target.id, False),
                   ("**📱 Status**", str(target.status).title(), False),
                   ("**📅 Conta criada em**", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                   ("**🌟 Entrou há**", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]

             for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

             await ctx.send(embed=embed)

#--------------- Comando de expulsar membro ---------------#

@bot.command() #precisa de permissão
async def kick(ctx, member : discord.Member, *, reason=None):
  await ctx.message.delete()
  await member.kick(reason=reason)

#--------------- Comando De banir membro ---------------#

@bot.command() #precisa de permissão
async def ban(ctx, member : discord.Member, *, reason=None):
  await ctx.message.delete()
  await member.ban(reason=reason)
 
#--------------- Comando de excluir todos canais ---------------#

@bot.command()
async def rcanais(ctx): #precisa de permissao
		await ctx.message.delete()

		for channel in ctx.guild.channels:
			try:
				await channel.delete()
				
			except:
				await ctx.send('`[ERRO] Não foi possivel excluir os canais`')

#--------------- Comando de excluir todos cargos ---------------#

@bot.command()
async def rcargos(ctx): #precisa de permissao
		await ctx.message.delete()

		for role in ctx.guild.roles:
			try:
				await role.delete()
			except:
				await ctx.send(f'`[ERRO] Não foi possivel apagar cargos de bot e @everyone!.`')
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def espam(ctx):
	for i in range(100):
		try:
			await ctx.send('@everyone')
		except:
			pass
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def spam(ctx, *, arg=None):
	if arg == None:
		await ctx.send(f"`[ERRO] Digite a mensagem que você quer floodar!.`")
	else:
		for i in range(100):
			try:
				await ctx.send(arg)
			except:
				pass
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def cargos(ctx, *, arg=None):
	if arg == None:
		await ctx.send(f"`[ERRO] Digite o nome do cargo a ser criado!.`")
	else:
		for i in range(250):
			try:
				await ctx.guild.create_role(name=arg)
			except:
				pass
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)

            await ctx.channel.send("'" + args + "' enviando para: " + target.name)

        except:
            await ctx.channel.send("Nao foi possivel  eveiar a dm obs: voce pode ta bloqueado ou nao esta ativa mensagens diretas.")
        

    else:
        await ctx.channel.send("Você não forneceu um ID de usuário / ou uma mensagem.")
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command() 
async def canais(ctx, *, arg=None): #precisa de permissao
	if arg == None:
		await ctx.send("`[ERRO] Informe o nome do canal a ser criado!.`")
	else:
		await ctx.message.delete()
		for i in range(250):
			try:
				await ctx.guild.create_text_channel(arg)
			except:
				pass
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def copy(ctx): #So funciona No pc ou bugo
    await ctx.message.delete()
    await bot.create_guild(f'Servidor de {ctx.author.name}')
    await asyncio.sleep(4)
    for g in bot.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
                    if isinstance(chann, discord.Role):
                    	await x.create_role(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def masskick(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.member):
        try:
            await user.kick()
        except:
            pass    
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def desbantodos(ctx): #precisa de permissão
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def nuke(ctx): # precisa de permissão
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print(f"{Color.WHITE}{ctx.channel.name} {Color.GREEN} Canal excluido em {Color.WHITE}{ctx.guild.name}")
        except:
            pass
    for member in list(ctx.guild.members):
        try:
            await member.kick()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description=f"Hackeado por {ctx.author.name}",
            reason=f"Hackeado por {ctx.author.name}",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name=f"Hackeado por {ctx.author.name}")
    for _i in range(250):
        await ctx.guild.create_role(name=f"Hackeado por {ctx.author.name}")
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def fmsg(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def ipinfo(ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
   
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Tipo de ip', 'value': geo['ipType']}, 
        {'name': 'País', 'value': geo['country']},
        {'name': 'Cidade', 'value': geo['city']},
        {'name': 'Continente', 'value': geo['continent']},
        {'name': 'IPNome', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def abc(ctx): # b'\xfc'
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(1)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(1)
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def cterminal(ctx):
	os.system('clear')
	await ctx.send('`[AVISO] Terminal limpado com sucesso!.`')
	print(f"{Color.GREEN}{logo55}")
	print('\n')
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
    except KeyError:
        print(f"{Color.RED}[ERROR]: {Color.YELLOW}Token invalido"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nPais: `{res['locale']}`\nFoto do user: [Clique aki](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Telefone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verificado?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await bot.change_presence(activity=stream) 

@bot.command()
async def game(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await bot.change_presence(activity=game)

@bot.command()
async def listening(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@bot.command()
async def watching(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@bot.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Color.RED}[ERROR]: {Color.YELLOW}{e}"+Color.RESET)
#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def xvideos(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('https://www.xvideos.com/')

@bot.command()
async def lesbian(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def anal(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


#------------------------------------------------------------------------------------------------------------------------------------#
@bot.command()
async def tokencheck(ctx, *, args):
    await ctx.message.delete()

    headers = {

                'Authorization': f'{args}'
            } 

    request = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

    if request.status_code == 200:
        embes_v = discord.Embed(title='', description=':thumbsup:| **token valido**', color=0x00ff00)
        await ctx.send(embed=embes_v)
    else:
        emded_inv = discord.Embed(title='', description=':thumbsdown:| **token invalido**', color=0x00ff00)
        await ctx.send(embed=emded_inv)
#------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------------------#

headers = {'Authorization': token}
req = requests.get('https://discord.com/api/v6/auth/login', headers=headers)

if req.status_code == 200:

        bot.run(token, bot=False)

else:
        print(Fore.RED+'[ERRO] Token invalido')
        print(Fore.WHITE+'[AVISO] reiniciando o selfbot')
        time.sleep(3)
        os.system('python main.py')
