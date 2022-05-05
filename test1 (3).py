import requests,time,os,re,sys,string,subprocess,asyncio
from telethon import TelegramClient

r=requests.get("https://justpaste.it/active77")
e=(r.status_code)
if e==200 :
 y=subprocess.getoutput("pip install requests")
 y
 os.system("clear")
 #name = input ("\033[0;33m Enter your Name: ")
 #os.system("clear")
 print("\033[1;30m Hello,")
 print("")
 logo="""
                      x 500MB ORANGE FREE x     
 
                       x Youssef  Bassem x    
 
 \033[0;94m     ____
 \033[0;94m    / __ \ _____ ____ _ ____   ____ _ ___          
 \033[0;94m   / / / // ___// __ `// __ \ / __ `// _ \ 
 \033[0;94m  / /_/ // /   / /_/ // / / // /_/ //  __/ 
 \033[0;94m  \____//_/    \__,_//_/ /_/ \__, / \___/
 \033[0;94m                            /____/
 """
 for o in logo:
     sys.stdout.write(o)
     sys.stdout.flush()
     time.sleep(0.01)
 print("")
else:
 	print("\033[0;31m Script Was Closed !")
 	sys.exit()
class main():
    #def __init__(self):
    ####################################################################
                                ############Add Number##############
    def token(self):
        file_variable = open('myfile.txt','r+')
        all_lines= file_variable.readlines()
        ctv=all_lines[0].replace('ctv : ','').replace(" \n","").replace('''
        ''','')
        htv=all_lines[1].replace('htv : ','').replace(" \n","").replace('''
        ''','')
        url2 = 'https://backend.orange.eg/api/HybridFamily/ManageFamily'

        headers2 ={'Host': 'backend.orange.eg',
                   '_ctv': ctv,
                   '_htv': htv,
                   'Content-Type': 'application/json; charset=UTF-8',
                   'Content-Length':'235',
                   'Accept-Encoding': 'gzip, deflate',
                   'User-Agent': 'okhttp/3.12.1',
                   'Connection': 'close'}
        
        data2 = '{"ActionType":"2","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"FamilyMemberDial":"01228221780","FamilyOwnerDial":"01273004463","lang":"ar","dial":"01273004463","IsEasyLogin":false,"password":"emr25dyp"}'

        r=requests.post(url2,data=data2,headers=headers2)
        m=(r.status_code)
        if m ==200:
          print("\033[0;32m Success !")
        else:
            print(r.text)
    #####################################################################
                                ############Manage Units##############
    def delta(self):
        file_variable = open('myfile.txt','r+')
        all_lines= file_variable.readlines()
        ctv=all_lines[0].replace('ctv : ','').replace(" \n","").replace('''
        ''','')
        htv=all_lines[1].replace('htv : ','').replace(" \n","").replace('''
        ''','')
        url3 = 'https://backend.orange.eg/api/HybridFamily/ManageSharing'             
        headers3 ={'Host': 'backend.orange.eg',
                   '_ctv': ctv,
                   '_htv': htv,
                   'Content-Type': 'application/json; charset=UTF-8',
                   'Content-Length':'254',
                   'Accept-Encoding': 'gzip, deflate',
                   'User-Agent': 'okhttp/3.12.1',
                   'Connection': 'close'}
        data3='{"ActionType":"2","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"FamilyMemberDial":"01228221780","lang":"ar","Sharing":[{"SharedAmount":"10","SharingType":5}],"dial":"01273004463","IsEasyLogin":false,"password":"emr25dyp"}'     
        req=requests.post(url3,data=data3,headers=headers3)
        m=(req.status_code)
        if m ==200:
          print("\033[0;32m Success,Added!")
    ###############################################################################
                             ############Delete##############
    def india(self):
        file_variable = open('myfile.txt','r+')
        all_lines= file_variable.readlines()
        ctv=all_lines[0].replace('ctv : ','').replace(" \n","").replace('''
        ''','')
        htv=all_lines[1].replace('htv : ','').replace(" \n","").replace('''
        ''','')
        url4='https://backend.orange.eg/api/HybridFamily/ManageFamily'          
        headers4 ={'Host': 'backend.orange.eg',
                   '_ctv': ctv,
                   '_htv': htv,
                   'Content-Type': 'application/json; charset=UTF-8',
                   'Content-Length':'254',
                   'Accept-Encoding': 'gzip, deflate',
                   'User-Agent': 'okhttp/3.12.1',
                   'Connection': 'close'}
        data4='{"ActionType":"3","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"FamilyMemberDial":"01228221780","FamilyOwnerDial":"01273004463","lang":"ar","dial":"01273004463","IsEasyLogin":false,"password":"emr25dyp"}'
        req=requests.post(url4,data=data4,headers=headers4)
        m=(req.status_code)
        if m ==200:
          print("\033[0;32m Done !")
    ##############################################################################
                                ############Accept##############
    def accept(self):
        file_variable = open('myfile.txt','r+')
        all_lines= file_variable.readlines()
        ctv=all_lines[0].replace('ctv : ','').replace(" \n","").replace('''
        ''','')
        htv=all_lines[1].replace('htv : ','').replace(" \n","").replace('''
        ''','')
        url5="https://backend.orange.eg/api/HybridFamily/ManageFamily"
        headers5={
        "Host": "backend.orange.eg",
        "_ctv": ctv,
        "_htv": htv,
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "235",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "okhttp/3.12.1",
        "Connection": "close"}
        data5='{"ActionType":"4","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"FamilyMemberDial":"01228221780","FamilyOwnerDial":"01273004463","lang":"ar","dial":"01228221780","IsEasyLogin":false,"password":"z4jx3vw2"}'
        req=requests.post(url5,data=data5,headers=headers5)
        m=(req.status_code)
        if m ==200:
          print("\033[0;32m Done !")
       ##############################################################################
print("welcome bro "+"\n")
fox=main()
print("{\033[0;33m 1}"+" To Add MBS"+" \n"+"{\033[0;33m 2}"+" To Delete&Renew")
delta= input(("put your choice :"))
client = TelegramClient("session", 18962752, "439407f036d83e4e4003fbf6a987a081")
client.start()
async def main():
    message = await client.get_messages("@ctv_htv_bot")
    await message[0].click()
    messages = await client.get_messages("@ctv_htv_bot",limit=1)
    for message in messages:
        mm= message.message
        file1 = open("myfile.txt", "w")
        L = [mm]
        file1.writelines(L)
asyncio.get_event_loop().run_until_complete(main())
if delta =="1":
    x=fox.token()
    time.sleep(1)
    asyncio.get_event_loop().run_until_complete(main())
    x=fox.delta()
    time.sleep(1)
    asyncio.get_event_loop().run_until_complete(main())
    x=fox.accept()
elif  delta =="2":
    x=fox.india()
    time.sleep(1)
    asyncio.get_event_loop().run_until_complete(main())
    x=fox.token()
    time.sleep(1)
    asyncio.get_event_loop().run_until_complete(main())
    x=fox.delta()
    time.sleep(1)
    asyncio.get_event_loop().run_until_complete(main())
    x=fox.accept()
else:
    print("\033[0;31m Uncorrect Choice ,Try Again.")
