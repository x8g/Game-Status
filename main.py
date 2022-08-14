import discord
import os

client = discord.Client()

token = input('\033[0;33mToken: ')
os.system('clear')

name = input('\033[0;33mGame Name: ')
os.system('clear')
  
  
@client.event
async def on_ready():
    print('''\033[1;33m 
░██████╗████████╗░█████╗░████████╗██╗░░░██╗░██████╗
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║░░░██║██╔════╝
╚█████╗░░░░██║░░░███████║░░░██║░░░██║░░░██║╚█████╗░
░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░██║░░░██║░╚═══██╗
██████╔╝░░░██║░░░██║░░██║░░░██║░░░╚██████╔╝██████╔╝
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═════╝░\033[0m
   ''')
    print("\033[0;32mONLINE\nLogged In As {0.user}".format(client))
    print(f'Game: {name}\033[0m')
    await client.change_presence(activity=discord.Game(name=f"{name}"))
client.run(token, bot=False)
client.run(f'{token}')
