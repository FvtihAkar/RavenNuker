import string,random,requests

allList = string.ascii_letters
cList = "0123456789abcdef"

def randomstr(length: int):
    returnStr = ""
    for i in range(length):
        returnStr += random.choice(allList)
    return returnStr
def randomcolor():
    returnStr = ""
    for i in range(6):
        returnStr += random.choice(cList)
    return int(returnStr,16)
def randomint(min,max):
    return random.randint(min,max)
class APIutils():
    def __init__(self, guid, headers):  
        self.guid = guid  
        self.headers = headers 


    def setServerName(self,name):
        requests.patch(f"https://discord.com/api/v9/guilds/{self.guid}",json={
            "name": name
        },headers=self.headers)

    def sendMessage(self,channel,content):
        requests.post(f"https://discord.com/api/v9/channels/{channel}/messages",headers=self.headers,json={
            "content": content
        })
    def banMember(self,member):
        requests.put(f"https://discord.com/api/v9/guilds/{self.guid}/bans/{member}",headers=self.headers)
    def deleteChannel(self,id):
        return requests.delete(f"https://discord.com/api/v9/channels/{id}",headers=self.headers)
    def createChannel(self,data):
        return requests.post(f"https://discord.com/api/v9/guilds/{self.guid}/channels",headers=self.headers,json=data)
    def getChannels(self):
        return requests.get(f"https://discord.com/api/v9/guilds/{self.guid}/channels",headers=self.headers).json()
    def getUsers(self):
        return requests.get(f"https://discord.com/api/v9/guilds/{self.guid}/members",headers=self.headers).json()
    def getMembers(self):
        return requests.get(f"https://discord.com/api/v9/guilds/{self.guid}/members",headers=self.headers).json()
    def getRoles(self):
        return requests.get(f"https://discord.com/api/v9/guilds/{self.guid}/members",headers=self.headers).json()
    def deleteRole(self,roleID):
        return requests.delete(f"https://discord.com/api/v9/guilds/{self.guid}/roles/{roleID}",headers=self.headers).json()
    def createRole(self,data):
        requests.get(f"https://discord.com/api/v9/guilds/{self.guid}/roles",headers=self.headers,json=data).json()