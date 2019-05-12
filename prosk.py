'''
© 2019SelfBot ProtectV3.1
'''

from DHENZA import *
from akad.ttypes import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from important import *
from random import randint
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
Bot_startTime = time.strftime("%H:%M:%S", time.localtime())
# Login line
print("""
\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Start Bot ]\033[0m    
"""%(Bot_startTime))
#==============================================================
cl = LINE("EEpR3Hwkz0HDzVssOUy3.FYu04akrWgYZ3QYlgLYHyW.TW8xKhycjRrzFiN9MvgRy4Q1VVE1U5ChGCJE+WTcKUc= ")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Selfbot Login ]\033[0m"""%(Bot_startTime))

k1 = LINE("EEGch55E6mLo1qnC7Cyd.H05bMcL8jvsvLLDFqxOzdq.AToHkkBWqC9wcZ0le27UQWF1+BUEsWA5/IdBG6oqif0=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist1 Login ]\033[0m"""%(Bot_startTime))

k2 = LINE("EDWbTbqC8PYiRz5rO5x8.zCDUP/z706O6bNt58ukv/a.RsWvduLPA4SburylX9NpqfiaCGUdoD9arWfXYalAkl4=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist2 Login ]\033[0m"""%(Bot_startTime))

k3 = LINE("EDTkA1tG7pcBl5wvxZVc.tn+6fwyxhvF5WM5t+TiPVa.PkiRYp45cqEHtZczpmURoo7vhjqyX1ESikgL5vCrFS8=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist3 Login ]\033[0m"""%(Bot_startTime))

k4 = LINE("EDtcM4XxGYBeXXyDorC4.6Uwi6B/cCTTBHPYfgSU+9a.ukSNl+c7ADevMllh1ebwvi+hgNOVdsAWVxfdQp5jBfo=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist4 Login ]\033[0m"""%(Bot_startTime))

k5 = LINE("EEZEoJAUa6R8AuoVA8R0.fXgtlnRBczSaU8u558m/ma.Eo1xOY1OlbDKddi2uIZA3EBCnyqGU22/wynxEOxu/xc=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist5 Login ]\033[0m"""%(Bot_startTime))

k6 = LINE("ED0cN7MhdEGnBb02xmmb.xtJLMlkBDgzM2QRYmmKMIW.0XUwU/kP5MptnYN6IfSXA2mREydF5FYowPuQk6TIKAw=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist6 Login ]\033[0m"""%(Bot_startTime))

k7 = LINE("EDbtMc6rxokiuMSRYpWd.0LmaH9CHq+TxBTfg2vfOpq.paNtHVVH1OpvJAJ+SEka6GMYEY5skODRH+AhqV7Pots=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist7 Login ]\033[0m"""%(Bot_startTime))

k8 = LINE("EEfXNyFoFfjHMBclO0r0.PoLEdyMCQJfPB5K56fOzia.p6jUdGVZc1odvTVUHVudnKXzRByzFz+HFhHTzCYOfVI=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist8 Login ]\033[0m"""%(Bot_startTime))

k9 = LINE("EE4x75ikHUah1Irr76d8.nKfeSlinHnaqKXwivAk22a.V+0IkUA21Erszs1zB/7ZGFiQ/J5iYjqctnBhh8tANjs=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist9 Login ]\033[0m"""%(Bot_startTime))

k10 = LINE("EESAk2TtLFmxiaYV0OHe.wzy3HFe4gpMpjOnrRHz0hG.8umjfyNH1JRtlRGpyABxxrI/TY5k5QSSeF1gFh/bK7M=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Asist10 Login ]\033[0m"""%(Bot_startTime))

g1 = LINE("EEXk1gKbHo9zhT8jx3j8.VBXOFAqRym29GqjwALneca.ZgX5mgk91yyI8rfEehihUuwEfoklXIywqAFObQ2giFc=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Kicker1 Login ]\033[0m"""%(Bot_startTime))

g2 = LINE("EEZq1tw1XlDQOKuuMzga.i4VcIshESshIzoDF6YMuIG.24SFc02i5llDS+D3XDSrjN3f4yci7nRPCJOf4/oRmps=")
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Kicker2 Login ]\033[0m"""%(Bot_startTime))
#==========================[[PAKE TOKEN CHROMEOS 2.1.5]]=========================
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m

	    Welcome To Self Bot Protect  By Dhenza15

            
Login Time %s \033[0m\n\n"""%(Bot_startTime))
#==============================================================================
oepoll = OEPoll(cl)
call = cl
creator = ["ub1c5a71f27b863896e9d44bea857d35b","ufdc20b3a00b5e8f31e4f91017eb361b0"]
owner = ["ub1c5a71f27b863896e9d44bea857d35b","ufdc20b3a00b5e8f31e4f91017eb361b0"]
admin = ["ub1c5a71f27b863896e9d44bea857d35b","ufdc20b3a00b5e8f31e4f91017eb361b0"]
staff = ["ufdc20b3a00b5e8f31e4f91017eb361b0"]
#==============================================================================
lineProfile = cl.getProfile()
mid = cl.getProfile().mid
mid = cl.getProfile().mid
Amid = k1.getProfile().mid
Bmid = k2.getProfile().mid
Cmid = k3.getProfile().mid
Dmid = k4.getProfile().mid
Emid = k5.getProfile().mid
Fmid = k6.getProfile().mid
Gmid = k7.getProfile().mid
Hmid = k8.getProfile().mid
Imid = k9.getProfile().mid
Jmid = k10.getProfile().mid   
g1MID = g1.getProfile().mid
g2MID = g2.getProfile().mid                 
KAC = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10]
ABC = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10]
KICKER = [g1,g2]           
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,g1MID,g2MID]
Saint = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)
#===============================================================================
welcome = []
targets = []
lower = []
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
protectname = []
botStart = time.time()
msgditerima = {}
unsendchat = {}
msgdikirim = {}
userTemp = {}
userKicked = []
dict = []
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
dhenzaqr = []
offbot = []
msg_image={}
msg_video={}
msg_sticker={}
detectUnsend = []
simisimi = []
tagmeOpen = codecs.open("tag.json","r","utf-8")
tagme = json.load(tagmeOpen)
#===============================================================================
responsename1 = k1.getProfile().displayName
responsename2 = k2.getProfile().displayName
responsename3 = k3.getProfile().displayName
responsename4 = k4.getProfile().displayName
responsename5 = k5.getProfile().displayName
responsename6 = k6.getProfile().displayName
responsename7 = k7.getProfile().displayName
responsename8 = k8.getProfile().displayName
responsename9 = k9.getProfile().displayName
responsename10 = k10.getProfile().displayName
#===============================================================================
settings = {
    "autoBlock": False,
    "autoRead": False,
    "welcome": False,
    "leave": False,
    "mid": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": True,
    "checkPost": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",    
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":False,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 100,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "dhenza":{},
    "likeOn": True,
    "Timeline": True,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoCancel':{"on":True, "members":20},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "unsend":True,
    "selfbot":True,
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
            "displayName": "",
            "coverId": "",
            "pictureStatus": "",
            "statusMessage": ""
            },
    "mention":"Masuk say ngitip bacok",
    "Respontag":"Cuy ngrtag mele..",
    "welcome":"Wellcome to my Fams",
    "comment":"ᴀᴜᴛᴏʟɪᴋᴇ ʙʏ: \n\n\n\n™S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ\n\n\n\nᴄʀᴇᴀᴛᴏʀ:\nhttp://line.me/ti/p/~teambotprotect\nɢɪᴛhᴜʙ:\ngithub.com/dhenza1415\nchanel ʏᴏᴜᴛᴜʙᴇ:\nhttps://youtu.be/CRqXKcTl6IY\n\nnew ᴄʜᴀɴᴇʟ:\nhttps://youtu.be/6UGH_4gG9qk",
    "message":"ᴄɪᴇᴇ ᴋᴇᴛᴀʜᴜᴀɴ ɴɢᴇ ᴀᴅᴅ\nᴍᴀᴋᴀsɪʜ ʏᴀ sᴜᴅᴀʜ ᴀᴅᴅ..\n\n\n\n\n™S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ\n\n\n\nᴄʀᴇᴀᴛᴏʀ:\nhttp://line.me/ti/p/~teambotprotect\nɢɪᴛhᴜʙ:\ngithub.com/dhenza1415\nchanel ʏᴏᴜᴛᴜʙᴇ:\nhttps://youtu.be/CRqXKcTl6IY\n\nnew ᴄʜᴀɴᴇʟ:\nhttps://youtu.be/6UGH_4gG9qk",
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

bl = {
    'blacklist':{}
    }

with open('bl.json', 'r') as fp:
    bl = json.load(fp)

rname = {
    "rname":"s"
}

sname = {
    "sname":"k"
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
dzProfile = cl.getProfile()
myProfile["displayName"] = dzProfile.displayName
myProfile["statusMessage"] = dzProfile.statusMessage
myProfile["pictureStatus"] = dzProfile.pictureStatus

    
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
        
        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]                   
       
            
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
                        
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
                        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
    
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def backupProfile():
    profile = cl.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = cl.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
    
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "✏DAFTAR JONES「{}」\n\n╔━━━━[ SILENT KILLER ]━━━\n╠❂➣✏1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠❂➣✏%i.  " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
        
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@dhenza "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0) 

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\nJam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nGroup : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nxpired : In "+hari+"\nVersion : Sempak Bot\nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd

def help():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭━━━━━━━━━━━━━━━\n"
    helpMessage += "│┃ " + "╭──⍟ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ⍟─\n"
    helpMessage += "│┃" + " ├───༼ᴍᴇɴᴜ ʙᴏᴛ sɪʟᴇɴᴛ༽────────────────\n"
    helpMessage += "│┃" + " ├──────────────\n"
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴘ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴋᴇᴘᴏ @\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴍʏʙᴏᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɴᴀᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴍᴀsᴜᴋ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴘᴜʟᴀɴɢ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴜᴘʙᴏᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɢᴇᴛᴍɪᴅ @\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀʙᴏᴜᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴛɪᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄʀᴇᴀᴛᴏʀ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɢʟɪsᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴏᴘᴇɴ\n"
    num = (num+1)    
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴏᴜʀʟ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i ." % num + key + "ᴄᴜʀʟ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɢʀᴜᴘɪɴғᴏ ɴᴏ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴛᴀғғʟɪsᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʙᴏᴛʟɪsᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʜᴀᴘᴜsᴄʜᴀᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sɪᴅᴇʀ ᴏɴ[ᴏғғ]\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴛᴇs\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴜᴘɢʀᴜᴘ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʙᴄᴀsᴛ:「ᴛᴇxᴛ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴇᴛɴᴀᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɴᴀᴍᴇ: ɴᴀᴍᴀ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɴᴀᴍᴇ1/10: ɴᴀᴍᴀ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʀᴇsᴇᴛɴᴀᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "s:sɪᴅᴇʀ: ᴛᴇxᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴘᴇsᴀɴ: ᴛᴇxᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴡᴇʟᴄᴏᴍᴇ: ᴛᴇxᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sʀᴇsᴘᴏɴ: ᴛᴇxᴛ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴜᴘʙᴏᴛ 「ubah foto」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "1/10ᴜᴘ 「ubah foto」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄsɪᴅᴇʀ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄᴘᴇsᴀɴ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄʀᴇsᴘᴏɴ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄᴡᴇʟᴄᴏᴍᴇ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴛɪᴄᴋᴇʀ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʀᴇsᴘᴏɴ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴜɴsᴇɴᴅ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀᴜᴛᴏʙʟᴏᴄᴋ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴡᴇʟᴄᴏᴍᴇ「ᴏɴ/ᴏғғ」\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʟᴀɢᴜ ᴊᴜᴅᴜʟ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "sᴍᴜʟᴇ:「ʟɪɴᴋ」 \n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "!ɢᴏᴏɢʟᴇ ᴄᴀʀɪ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʏᴛᴍᴘ4: ᴄᴀʀɪ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄʜᴀɴɢᴇᴅᴜᴀʟ \n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴄʜᴀɴɢᴇᴅᴜᴀʟʟɪɴᴋ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ɪᴍɢ ғᴏᴏᴅ: ᴄᴀʀɪ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴘʀᴏғɪʟᴇsᴍᴜʟᴇ: ɪᴅ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + " ᴘʀᴏғɪʟᴇɪɢ: ɪᴅ\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴍᴇᴍᴇ@1@2@3\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴛᴀғsɪʀǫᴜʀᴀɴ ɴᴏ|ɴᴏ\n"
    num = (num+1)    
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀᴅᴅɪᴍɢ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴅᴇʟʟɪᴍɢ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʟɪsᴛɪᴍɢ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀᴅᴅᴠɪᴅᴇᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴅᴇʟʟᴠɪᴅᴇᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʟɪsᴛᴠɪᴅᴇᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀᴅᴅsᴛɪᴄᴋᴇʀ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴅᴇʟʟsᴛɪᴄᴋᴇʀ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʟɪsᴛsᴛɪᴄᴋᴇʀ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴀᴅᴅᴀᴜᴅɪᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ᴅᴇʟʟᴀᴜᴅɪᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)
    helpMessage += "│╠❂➣ %i. " % num + key + "ʟɪsᴛᴀᴜᴅɪᴏ •ᴋᴀᴛᴀ•\n"
    num = (num+1)    
    helpMessage += "│┃ " + "├──────────────\n"
    helpMessage += "│┃ " + "╰──⍟ ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ⍟─────────\n"
    helpMessage += "╰━━━━━━━━━━━━━━━━"
    helpMessage += " Creator: https://line.me/ti/p/~teambotprotect \n"
    return helpMessage

def helpbot():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╭━━━━━━━━━━━━━━━━\n"
    helpMessage2 += "│┃ " + "╭───⍟ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ⍟─\n"
    helpMessage2 += "│┃" + " ├───༼ᴄᴏᴍᴍᴀɴᴅ ᴋɪᴄᴋᴇʀ༽────────────\n"
    helpMessage2 += "│┃" + " ├──────────────\n"
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴋɪᴄᴋᴇʀ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴠᴄ @ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴍᴀɪɴᴋᴀɴ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ɪɴᴠɪᴛᴇ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙʟ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴʟɪsᴛ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ғʀᴇsʜ/ʀᴇғʀᴇsʜ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ɢᴀs \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴋɪʟʟʙᴀɴ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "sᴘᴀᴍɪɴᴠɪᴛᴇ ᴏɴ/ᴏғғ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴅᴅʙᴏᴛ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴᴀʟʟ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴄʟᴇᴀʀʙᴀɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴅᴍɪɴ ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴅᴍɪɴ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴅᴍɪɴᴅᴇʟʟ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴅᴍɪɴ ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + " ᴏᴡɴᴇʀ ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "sᴛᴀғғ ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "sᴛᴀғғᴅᴇʟʟ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "sᴛᴀғғ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "sᴛᴀғғᴅᴇʟʟ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴏᴛ ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴏᴛᴅᴇʟʟ \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴏᴛ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴏᴛᴅᴇʟʟ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴᴅᴇʟʟ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴ ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴀɴᴅᴇʟʟ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴛᴀʟᴋʙᴀɴ ᴏɴ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "s bl\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "s dbn\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i ." % num + key + "ᴛᴀʟᴋʙᴀɴᴅᴇʟʟ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴛᴀᴋʙᴀɴ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + " ᴛᴀʟᴋʙᴀɴᴅᴇʟʟ @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴛᴀʟᴋʙᴀɴʟɪsᴛ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀʟʟᴘʀᴏ ᴏɴ/ᴏғғ\n"
    num = (num+1)    
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛǫʀ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛᴜʀʟ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛɪɴᴠɪᴛᴇ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴊs ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙʏᴇ1/10\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʟᴇᴀᴠᴇɢʀᴜᴘ「ɴᴏ」\n"
    num = (num+1)    
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴋɪᴄᴋᴇʀ「ɪɴ」\n"
    num = (num+1)  
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴋɪᴄᴋᴇʀ「ʟᴠ」\n"
    num = (num+1)    
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ɪɴғᴏɢʀᴜᴘ「ɴᴏ」\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ɪɴғᴏᴍᴇᴍʙᴇʀ「ɴᴏ」\n"
    num = (num+1)     
    helpMessage2 += "│╠❂➣ %i. " % num + key + "sɪʟᴇɴᴛᴋɪʟʟᴇʀ [ᴋɪᴄᴋᴀʟʟ]\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ʙᴜʙᴀʀ [ᴋɪᴄᴋᴀʟʟ]\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "sɪʟᴇɴᴛ1/2 \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴜᴛᴏᴊᴏɪɴ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴀᴜᴛᴏʙʟᴏᴋ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴏɴ/ᴏғғ\n"
    num = (num+1)
    helpMessage2 += "│┃ " + "├──────────────\n"
    helpMessage2 += "│┃ " + "╰──⍟ ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ⍟────────\n"
    helpMessage2 += "╰━━━━━━━━━━━━━━━━"
    helpMessage2 += " My ID LINE : 〘 https://line.me/ti/p/~teambotprotect 〙\n"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if aditya.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if k1.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                k1.reissueGroupTicket(op.param1)
                                X = k1.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                k1.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if k2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    k2.reissueGroupTicket(op.param1)
                                    X = k2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    k2.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if k3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        k3.reissueGroupTicket(op.param1)
                                        X = k3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        k3.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if k4.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            k4.reissueGroupTicket(op.param1)
                                            X = k4.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            k4.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if k5.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                k5.reissueGroupTicket(op.param1)
                                                X = k5.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                k5.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if k6.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    k6.reissueGroupTicket(op.param1)
                                                    X = k6.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    k6.updateGroup(X)
                                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                        except:
                                            try:
                                                if k7.getGroup(op.param1).preventedJoinByTicket == False:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        k7.reissueGroupTicket(op.param1)
                                                        X = k7.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        k7.updateGroup(X)
                                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                            except:
                                                try:
                                                    if k8.getGroup(op.param1).preventedJoinByTicket == False:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            k8.reissueGroupTicket(op.param1)
                                                            X = k8.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            k8.updateGroup(X)
                                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                except:
                                                    try:
                                                        if k9.getGroup(op.param1).preventedJoinByTicket == False:
                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                k9.reissueGroupTicket(op.param1)
                                                                X = k9.getGroup(op.param1)
                                                                X.preventedJoinByTicket = True
                                                                k9.updateGroup(X)
                                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                    except:
                                                        try:
                                                            if k10.getGroup(op.param1).preventedJoinByTicket == False:
                                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                    k10.reissueGroupTicket(op.param1)
                                                                    X = k10.getGroup(op.param1)
                                                                    X.preventedJoinByTicket = True
                                                                    k10.updateGroup(X)
                                                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                        except:
                                                            pass                                                                   
#====================================================================                            
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)      
#====================================================================                          
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        cl.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            cl.cancelGroupInvitation(op.param1,[taged])                           
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Amid in op.param3:
                G = k1.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k1.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k1.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k1.cancelGroupInvitation(op.param1,[taged])
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Bmid in op.param3:
                G = k2.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k2.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k2.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k2.cancelGroupInvitation(op.param1,[taged])
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Cmid in op.param3:
                G = k3.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k3.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k3.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k3.cancelGroupInvitation(op.param1,[taged])
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Dmid in op.param3:
                G = k4.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k4.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k4.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k4.cancelGroupInvitation(op.param1,[taged])
                            k4.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Emid in op.param3:
                G = k5.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k5.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        ke.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k5.cancelGroupInvitation(op.param1,[taged])
                            k5.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Fmid in op.param3:
                G = k6.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k6.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k6.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k6.cancelGroupInvitation(op.param1,[taged])
                            k6.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Gmid in op.param3:
                G = k7.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k7.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k7.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k7.cancelGroupInvitation(op.param1,[taged])
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Hmid in op.param3:
                G = k8.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k8.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k8.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k8.cancelGroupInvitation(op.param1,[taged])
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Imid in op.param3:
                G = k9.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k9.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k9.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k9.cancelGroupInvitation(op.param1,[taged])
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if Jmid in op.param3:
                G = k10.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k10.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k10.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in bl['blacklist']:
                        try:
                            k10.cancelGroupInvitation(op.param1,[taged])
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            bl['blacklist'][op.param2] = True
                            with open('bl.json', 'w') as fp:
                                json.dump(bl, fp, sort_keys=True, indent=4)
                        except:
                            pass
        if op.type == 13:
            if op.param3 in bl['blacklist'] and op.param2 in bl['blacklist'] and op.param2 not in Bots and op.param2 not in Saint and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                bl['blacklist'][op.param2] = True
                with open('bl.json', 'w') as fp:
                    json.dump(bl, fp, sort_keys=True, indent=4)
                try:
                    k1.cancelGroupInvitation(op.param1,[op.param3])
                    k1.kickoutFromGroup(op.param1, [op.param2])
                except:
                        try:
                            if op.param3 not in bl["blacklist"]:
                                k2.cancelGroupInvitation(op.param1,[op.param3])
                                k2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    k3.cancelGroupInvitation(op.param1,[op.param3])
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        k4.cancelGroupInvitation(op.param1,[op.param3])
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            k5.cancelGroupInvitation(op.param1,[op.param3])
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in bl["blacklist"]:
                                                k6.cancelGroupInvitation(op.param1,[op.param3])
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in bl["blacklist"]:
                                                    k7.cancelGroupInvitation(op.param1,[op.param3])
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in bl["blacklist"]:
                                                        k8.cancelGroupInvitation(op.param1,[op.param3])
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in bl["blacklist"]:
                                                            k9.cancelGroupInvitation(op.param1,[op.param3])
                                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in bl["blacklist"]:
                                                                k10.cancelGroupInvitation(op.param1,[op.param3])
                                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
                return                     
#====================================================================       
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        group = k1.getGroup(op.param1)
                        inv1 = op.param3.replace('\x1e',',')
                        inv2 = inv1.split(',')
                        for target in inv2:
                            k1.cancelGroupInvitation(op.param1, [target])
                            k1.kickoutFromGroup(op.param1, [op.param2])
                            bl["blacklist"][op.param2] = True
                    except:
                        try:
                            group = k2.getGroup(op.param1)
                            inv1 = op.param3.replace('\x1e',',')
                            inv2 = inv1.split(',')
                            for target in inv2:
                                k2.cancelGroupInvitation(op.param1, [target])
                                k2.kickoutFromGroup(op.param1, [op.param2])
                                bl["blacklist"][op.param2] = True
                        except:
                            try:
                                group = k3.getGroup(op.param1)
                                inv1 = op.param3.replace('\x1e',',')
                                inv2 = inv1.split(',')
                                for target in inv2:
                                    k3.cancelGroupInvitation(op.param1, [target])
                                    k3.kickoutFromGroup(op.param1, [op.param2])
                                    bl["blacklist"][op.param2] = True
                            except:
                                try:
                                    group = k4.getGroup(op.param1)
                                    inv1 = op.param3.replace('\x1e',',')
                                    inv2 = inv1.split(',')
                                    for target in inv2:
                                        k4.cancelGroupInvitation(op.param1, [target])
                                        k4.kickoutFromGroup(op.param1, [op.param2])
                                        bl["blacklist"][op.param2] = True
                                except:
                                    try:
                                        group = k5.getGroup(op.param1)
                                        inv1 = op.param3.replace('\x1e',',')
                                        inv2 = inv1.split(',')
                                        for target in inv2:
                                            k5.cancelGroupInvitation(op.param1, [target])
                                            k5.kickoutFromGroup(op.param1, [op.param2])
                                            bl["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            group = k6.getGroup(op.param1)
                                            inv1 = op.param3.replace('\x1e',',')
                                            inv2 = inv1.split(',')
                                            for target in inv2:
                                                k6.cancelGroupInvitation(op.param1, [target])
                                                k6.kickoutFromGroup(op.param1, [op.param2])
                                                bl["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                group = k7.getGroup(op.param1)
                                                inv1 = op.param3.replace('\x1e',',')
                                                inv2 = inv1.split(',')
                                                for target in inv2:
                                                    k7.cancelGroupInvitation(op.param1, [target])
                                                    k7.kickoutFromGroup(op.param1, [op.param2])
                                                    bl["blacklist"][op.param2] = True    
                                            except:
                                                try:
                                                   group = k8.getGroup(op.param1)
                                                   inv1 = op.param3.replace('\x1e',',')
                                                   inv2 = inv1.split(',')
                                                   for target in inv2:
                                                       k8.cancelGroupInvitation(op.param1, [target])
                                                       k8.kickoutFromGroup(op.param1, [op.param2])
                                                       bl["blacklist"][op.param2] = True
                                                except:
                                                	pass       
       
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    bl["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in bl["blacklist"]:
                        	k1.kickoutFromGroup(op.param1,[op.param2])
                    except: 
                        try:
                            if op.param3 not in bl["blacklist"]:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                except: 
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in bl["blacklist"]:
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in bl["blacklist"]:
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in bl["blacklist"]:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in bl["blacklist"]:
                                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in bl["blacklist"]:
                                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
                                                                
                return
                                        
        if op.type == 17:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    bl["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in bl["blacklist"]:
                        	k1.kickoutFromGroup(op.param1,[op.param2])
                    except: 
                        try:
                            if op.param3 not in bl["blacklist"]:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                except: 
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in bl["blacklist"]:
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in bl["blacklist"]:
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in bl["blacklist"]:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in bl["blacklist"]:
                                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in bl["blacklist"]:
                                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
                                                                
                return                                                                         
#====================================================================  
        if op.type == 11:
            if op.param2 in bl['blacklist']:
                    try:
                        k1.reissueGroupTicket(op.param1) 
                    except:
                        try:
                            if op.param3 not in bl["blacklist"]:
                                k2.reissueGroupTicket(op.param1) 
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    k3.reissueGroupTicket(op.param1) 
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        k4.reissueGroupTicket(op.param1) 
                                except:
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            k5.reissueGroupTicket(op.param1) 
                                    except:
                                        try:
                                            if op.param3 not in bl["blacklist"]:
                                                k6.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                if op.param3 not in bl["blacklist"]:
                                                    k7.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    if op.param3 not in bl["blacklist"]:
                                                        k8.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        if op.param3 not in bl["blacklist"]:
                                                            k9.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            if op.param3 not in bl["blacklist"]:
                                                                k10.reissueGroupTicket(op.param1)
                                                        except:
                                                            pass
                 
#====================================================================                                                                                                                 
#====================================================================                            
        if op.type == 17:
            if op.param2 in bl['blacklist']:                
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2]) 
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
                                                                
                
#====================================================================     
        if op.type == 19:
            if op.param2 in bl['blacklist']:            
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2]) 
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
                                                                
#====================================================================                                            
        if op.type == 19:
            if op.param1 in ghost:
            	try:
            	    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
            	        G = cl.getGroup(op.param1)
            	        G.preventedJoinByTicket = False
            	        cl.updateGroup(G)
            	        invsend = 0
            	        Ticket = cl.reissueGroupTicket(op.param1)
            	        g1.acceptGroupInvitationByTicket(op.param1,Ticket)
            	        g2.acceptGroupInvitationByTicket(op.param1,Ticket)
            	        try:
            	            g1.kickoutFromGroup(op.param1,[op.param2])
            	        except:
            	            try:
            	                g2.kickoutFromGroup(op.param1,[op.param2])
            	            except:
            	                pass
            	        bl["blacklist"][op.param2] = True
            	        try:
            	            g1.findAndAddContactsByMid(op.param3)
            	            g1.inviteIntoGroup(op.param1,[op.param3])
            	        except:
            	            try:
            	                g2.findAndAddContactsByMid(op.param3)
            	                g2.inviteIntoGroup(op.param1,[op.param3])
            	            except:
            	                g1.sendMessage(op.param1,"Bl succes")
            	                g1.leaveGroup(op.param1)
            	                g2.leaveGroup(op.param1)
            	        g1.leaveGroup(op.param1)
            	        g2.leaveGroup(op.param1)
            	        X = cl.getGroup(op.param1)
            	        X.preventedJoinByTicket = True
            	        cl.updateGroup(X)
            	except:
            	    pass              	
#============================[[[ Anti Kicker ]]]========================================                                                              
        if op.type == 19:
            if op.param1 in protectantijs:
                if mid in op.param3:
                    if op.param2 not in Bots and op.param2 not in Saint and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        try:
                            g1.acceptGroupInvitation(op.param1)   
                            g2.acceptGroupInvitation(op.param1)                                                                              
                            G = g1.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            g1.updateGroup(G)
                            Ticket = g1.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                            bl["blacklist"][op.param2] = True
                            g1.leaveGroup(op.param1)
                            g2.leaveGroup(op.param1)                           
                            cl.inviteIntoGroup(op.param1,[g1MID,g2MID])                                                  
                        except:
                            pass
                            
                            
            if op.param3 in g1MID:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[g1MID])
                        cl.sendMessage(op.param1,"ANTI KICKER STAY")
                else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[g1MID])
                        cl.sendMessage(op.param1,"ANTI KICKER STAY")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            bl["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.sendMessage(op.param1,"SUCSESS INVITE ADMIN")
                else:
                    pass
            
            if op.param1 in protectantijs:
                if g2MID in op.param3:
                    if op.param2 not in Bots and op.param2 not in Saint and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        bl["blacklist"][op.param2] = True
                        try:
                            g1.inviteIntoGroup(op.param1,[g2MID])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.inviteIntoGroup(op.param1,[g2MID])
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                               
            try:
                if op.param3 in owner:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            bl["blacklist"][op.param2] = True

                if op.param3 in admin:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            bl["blacklist"][op.param2] = True

                if op.param3 in staff:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in staff:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            bl["blacklist"][op.param2] = True              
            except:
                pass
#====================================================================                                 
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
             
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])        

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    bl["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in bl["blacklist"]:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.inviteIntoGroup(op.param1,[g1MID,g2MID])
                            k1.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                            k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)									
                    except:
                        try:
                            if op.param3 not in bl["blacklist"]:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.inviteIntoGroup(op.param1,[g1MID,g2MID])
                                k2.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                k2.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)										
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k3.inviteIntoGroup(op.param1,[g1MID,g2MID])
                                    k3.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                    k3.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)										
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[g1MID,g2MID])
                                        k4.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                        k4.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)											
                                except:
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[g1MID,g2MID])
                                            k5.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                            k5.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if op.param3 not in bl["blacklist"]:
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                                k6.inviteIntoGroup(op.param1,[g1MID,g2MID])
                                                k6.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                                k6.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)			
                                        except:
                                            try:
                                                if op.param3 not in bl["blacklist"]:
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                                    k7.inviteIntoGroup(op.param1,[g1MID,g2MID])
                                                    k7.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                                    k7.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)														
                                            except:
                                                try:
                                                    if op.param3 not in bl["blacklist"]:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                        k8.nviteIntoGroup(op.param1,[g1MID,g2MID])
                                                        k8.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                                        k8.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)													
                                                except:
                                                    pass
                return        
#====================================================================                  
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:                  	
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                    k4.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                            k6.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                                k7.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                                        k9.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(KICKER).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except: 
                                                            try:
                                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                                k10.inviteIntoGroup(op.param1,[op.param3])
                                                                cl.acceptGroupInvitation(op.param1)
                                                            except:
                                                                pass
                return
                                                                                                                    
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        k6.acceptGroupInvitation(op.param1)
                        k7.acceptGroupInvitation(op.param1)
                        k8.acceptGroupInvitation(op.param1)
                        k9.acceptGroupInvitation(op.param1)
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            cl.acceptGroupInvitation(op.param1)
                            k1.acceptGroupInvitation(op.param1)
                            k3.acceptGroupInvitation(op.param1)
                            k4.acceptGroupInvitation(op.param1)
                            k5.acceptGroupInvitation(op.param1)
                            k6.acceptGroupInvitation(op.param1)
                            k7.acceptGroupInvitation(op.param1)
                            k8.acceptGroupInvitation(op.param1)
                            k9.acceptGroupInvitation(op.param1)
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                cl.acceptGroupInvitation(op.param1)
                                k1.acceptGroupInvitation(op.param1)
                                k2.acceptGroupInvitation(op.param1)
                                k3.acceptGroupInvitation(op.param1)
                                k4.acceptGroupInvitation(op.param1)
                                k5.acceptGroupInvitation(op.param1)
                                k6.acceptGroupInvitation(op.param1)
                                k7.acceptGroupInvitation(op.param1)
                                k8.acceptGroupInvitation(op.param1)
                                k9.acceptGroupInvitation(op.param1)
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    k6.acceptGroupInvitation(op.param1)
                                    k7.acceptGroupInvitation(op.param1)
                                    k8.acceptGroupInvitation(op.param1)
                                    k9.acceptGroupInvitation(op.param1)
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k6.kickoutFromGroup(op.param1,[op.param2])
                                        k6.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.acceptGroupInvitation(op.param1)
                                        k1.acceptGroupInvitation(op.param1)
                                        k2.acceptGroupInvitation(op.param1)
                                        k3.acceptGroupInvitation(op.param1)
                                        k4.acceptGroupInvitation(op.param1)
                                        k5.acceptGroupInvitation(op.param1)
                                        k6.acceptGroupInvitation(op.param1)
                                        k7.acceptGroupInvitation(op.param1)
                                        k8.acceptGroupInvitation(op.param1)
                                        k9.acceptGroupInvitation(op.param1)
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k7.kickoutFromGroup(op.param1,[op.param2])
                                            k7.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                            cl.acceptGroupInvitation(op.param1)
                                            k1.acceptGroupInvitation(op.param1)
                                            k2.acceptGroupInvitation(op.param1)
                                            k3.acceptGroupInvitation(op.param1)
                                            k4.acceptGroupInvitation(op.param1)
                                            k5.acceptGroupInvitation(op.param1)
                                            k6.acceptGroupInvitation(op.param1)
                                            k7.acceptGroupInvitation(op.param1)
                                            k8.acceptGroupInvitation(op.param1)
                                            k9.acceptGroupInvitation(op.param1)
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k8.kickoutFromGroup(op.param1,[op.param2])
                                                k8.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                cl.acceptGroupInvitation(op.param1)
                                                k1.acceptGroupInvitation(op.param1)
                                                k2.acceptGroupInvitation(op.param1)
                                                k3.acceptGroupInvitation(op.param1)
                                                k4.acceptGroupInvitation(op.param1)
                                                k5.acceptGroupInvitation(op.param1)
                                                k6.acceptGroupInvitation(op.param1)
                                                k7.acceptGroupInvitation(op.param1)
                                                k8.acceptGroupInvitation(op.param1)
                                                k9.acceptGroupInvitation(op.param1)
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                                    k9.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    k1.acceptGroupInvitation(op.param1)
                                                    k2.acceptGroupInvitation(op.param1)
                                                    k3.acceptGroupInvitation(op.param1)
                                                    k4.acceptGroupInvitation(op.param1)
                                                    k5.acceptGroupInvitation(op.param1)
                                                    k6.acceptGroupInvitation(op.param1)
                                                    k7.acceptGroupInvitation(op.param1)
                                                    k8.acceptGroupInvitation(op.param1)
                                                    k9.acceptGroupInvitation(op.param1)
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                                        k10.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        k1.acceptGroupInvitation(op.param1)
                                                        k2.acceptGroupInvitation(op.param1)
                                                        k3.acceptGroupInvitation(op.param1)
                                                        k4.acceptGroupInvitation(op.param1)
                                                        k5.acceptGroupInvitation(op.param1)
                                                        k6.acceptGroupInvitation(op.param1)
                                                        k7.acceptGroupInvitation(op.param1)
                                                        k8.acceptGroupInvitation(op.param1)
                                                        k9.acceptGroupInvitation(op.param1)
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(KICKER).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k1.kickoutFromGroup(op.param1,[op.param2])
                                                                k1.inviteIntoGroup(op.param1,[op.param3])
                                                                k1.acceptGroupInvitation(op.param1)
                                                            except:
                                                                pass 
                                                                                                                      
                                        
                return        
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        k6.acceptGroupInvitation(op.param1)
                        k7.acceptGroupInvitation(op.param1)
                        k8.acceptGroupInvitation(op.param1)
                        k9.acceptGroupInvitation(op.param1)
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k4.kickoutFromGroup(op.param1,[op.param2])
                            k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            cl.acceptGroupInvitation(op.param1)
                            k1.acceptGroupInvitation(op.param1)
                            k2.acceptGroupInvitation(op.param1)
                            k3.acceptGroupInvitation(op.param1)
                            k4.acceptGroupInvitation(op.param1)
                            k5.acceptGroupInvitation(op.param1)
                            k6.acceptGroupInvitation(op.param1)
                            k7.acceptGroupInvitation(op.param1)
                            k8.acceptGroupInvitation(op.param1)
                            k9.acceptGroupInvitation(op.param1)
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k5.kickoutFromGroup(op.param1,[op.param2])
                                k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                cl.acceptGroupInvitation(op.param1)
                                k1.acceptGroupInvitation(op.param1)
                                k2.acceptGroupInvitation(op.param1)
                                k3.acceptGroupInvitation(op.param1)
                                k4.acceptGroupInvitation(op.param1)
                                k5.acceptGroupInvitation(op.param1)
                                k6.acceptGroupInvitation(op.param1)
                                k7.acceptGroupInvitation(op.param1)
                                k8.acceptGroupInvitation(op.param1)
                                k9.acceptGroupInvitation(op.param1)
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                    k6.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    k6.acceptGroupInvitation(op.param1)
                                    k7.acceptGroupInvitation(op.param1)
                                    k8.acceptGroupInvitation(op.param1)
                                    k9.acceptGroupInvitation(op.param1)
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                        k7.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.acceptGroupInvitation(op.param1)
                                        k1.acceptGroupInvitation(op.param1)
                                        k2.acceptGroupInvitation(op.param1)
                                        k3.acceptGroupInvitation(op.param1)
                                        k4.acceptGroupInvitation(op.param1)
                                        k5.acceptGroupInvitation(op.param1)
                                        k6.acceptGroupInvitation(op.param1)
                                        k7.acceptGroupInvitation(op.param1)
                                        k8.acceptGroupInvitation(op.param1)
                                        k9.acceptGroupInvitation(op.param1)
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k8.kickoutFromGroup(op.param1,[op.param2])
                                            k8.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                            cl.acceptGroupInvitation(op.param1)
                                            k1.acceptGroupInvitation(op.param1)
                                            k2.acceptGroupInvitation(op.param1)
                                            k3.acceptGroupInvitation(op.param1)
                                            k4.acceptGroupInvitation(op.param1)
                                            k5.acceptGroupInvitation(op.param1)
                                            k6.acceptGroupInvitation(op.param1)
                                            k7.acceptGroupInvitation(op.param1)
                                            k8.acceptGroupInvitation(op.param1)
                                            k9.acceptGroupInvitation(op.param1)
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k9.kickoutFromGroup(op.param1,[op.param2])
                                                k9.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                cl.acceptGroupInvitation(op.param1)
                                                k1.acceptGroupInvitation(op.param1)
                                                k2.acceptGroupInvitation(op.param1)
                                                k3.acceptGroupInvitation(op.param1)
                                                k4.acceptGroupInvitation(op.param1)
                                                k5.acceptGroupInvitation(op.param1)
                                                k6.acceptGroupInvitation(op.param1)
                                                k7.acceptGroupInvitation(op.param1)
                                                k8.acceptGroupInvitation(op.param1)
                                                k9.acceptGroupInvitation(op.param1)
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                                    k10.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    k1.acceptGroupInvitation(op.param1)
                                                    k2.acceptGroupInvitation(op.param1)
                                                    k3.acceptGroupInvitation(op.param1)
                                                    k4.acceptGroupInvitation(op.param1)
                                                    k5.acceptGroupInvitation(op.param1)
                                                    k6.acceptGroupInvitation(op.param1)
                                                    k7.acceptGroupInvitation(op.param1)
                                                    k8.acceptGroupInvitation(op.param1)
                                                    k9.acceptGroupInvitation(op.param1)
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                                        k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        k1.acceptGroupInvitation(op.param1)
                                                        k2.acceptGroupInvitation(op.param1)
                                                        k3.acceptGroupInvitation(op.param1)
                                                        k4.acceptGroupInvitation(op.param1)
                                                        k5.acceptGroupInvitation(op.param1)
                                                        k6.acceptGroupInvitation(op.param1)
                                                        k7.acceptGroupInvitation(op.param1)
                                                        k8.acceptGroupInvitation(op.param1)
                                                        k9.acceptGroupInvitation(op.param1)
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(KICKER).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                                k3.acceptGroupInvitation(op.param1)
                                                            except:
                                                                pass
                                                               
                return
              
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k4.kickoutFromGroup(op.param1,[op.param2])
                        k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        k6.acceptGroupInvitation(op.param1)
                        k7.acceptGroupInvitation(op.param1)
                        k8.acceptGroupInvitation(op.param1)
                        k9.acceptGroupInvitation(op.param1)
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                            k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            cl.acceptGroupInvitation(op.param1)
                            k1.acceptGroupInvitation(op.param1)
                            k2.acceptGroupInvitation(op.param1)
                            k3.acceptGroupInvitation(op.param1)
                            k4.acceptGroupInvitation(op.param1)
                            k5.acceptGroupInvitation(op.param1)
                            k6.acceptGroupInvitation(op.param1)
                            k7.acceptGroupInvitation(op.param1)
                            k8.acceptGroupInvitation(op.param1)
                            k9.acceptGroupInvitation(op.param1)
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k6.kickoutFromGroup(op.param1,[op.param2])
                                k6.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                cl.acceptGroupInvitation(op.param1)
                                k1.acceptGroupInvitation(op.param1)
                                k2.acceptGroupInvitation(op.param1)
                                k3.acceptGroupInvitation(op.param1)
                                k4.acceptGroupInvitation(op.param1)
                                k5.acceptGroupInvitation(op.param1)
                                k6.acceptGroupInvitation(op.param1)
                                k7.acceptGroupInvitation(op.param1)
                                k8.acceptGroupInvitation(op.param1)
                                k9.acceptGroupInvitation(op.param1)
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                    k7.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    k6.acceptGroupInvitation(op.param1)
                                    k7.acceptGroupInvitation(op.param1)
                                    k8.acceptGroupInvitation(op.param1)
                                    k9.acceptGroupInvitation(op.param1)
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.acceptGroupInvitation(op.param1)
                                        k1.acceptGroupInvitation(op.param1)
                                        k2.acceptGroupInvitation(op.param1)
                                        k3.acceptGroupInvitation(op.param1)
                                        k4.acceptGroupInvitation(op.param1)
                                        k5.acceptGroupInvitation(op.param1)
                                        k6.acceptGroupInvitation(op.param1)
                                        k7.acceptGroupInvitation(op.param1)
                                        k8.acceptGroupInvitation(op.param1)
                                        k9.acceptGroupInvitation(op.param1)
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k7.kickoutFromGroup(op.param1,[op.param2])
                                            k7.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                            cl.acceptGroupInvitation(op.param1)
                                            k1.acceptGroupInvitation(op.param1)
                                            k2.acceptGroupInvitation(op.param1)
                                            k3.acceptGroupInvitation(op.param1)
                                            k4.acceptGroupInvitation(op.param1)
                                            k5.acceptGroupInvitation(op.param1)
                                            k6.acceptGroupInvitation(op.param1)
                                            k7.acceptGroupInvitation(op.param1)
                                            k8.acceptGroupInvitation(op.param1)
                                            k9.acceptGroupInvitation(op.param1)
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            try:                                                
                                                k8.kickoutFromGroup(op.param1,[op.param2])
                                                k8.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                cl.acceptGroupInvitation(op.param1)
                                                k1.acceptGroupInvitation(op.param1)
                                                k2.acceptGroupInvitation(op.param1)
                                                k3.acceptGroupInvitation(op.param1)
                                                k4.acceptGroupInvitation(op.param1)
                                                k5.acceptGroupInvitation(op.param1)
                                                k6.acceptGroupInvitation(op.param1)
                                                k7.acceptGroupInvitation(op.param1)
                                                k8.acceptGroupInvitation(op.param1)
                                                k9.acceptGroupInvitation(op.param1)
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                                    k9.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    k1.acceptGroupInvitation(op.param1)
                                                    k2.acceptGroupInvitation(op.param1)
                                                    k3.acceptGroupInvitation(op.param1)
                                                    k4.acceptGroupInvitation(op.param1)
                                                    k5.acceptGroupInvitation(op.param1)
                                                    k6.acceptGroupInvitation(op.param1)
                                                    k7.acceptGroupInvitation(op.param1)
                                                    k8.acceptGroupInvitation(op.param1)
                                                    k9.acceptGroupInvitation(op.param1)
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                                        k10.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        k1.acceptGroupInvitation(op.param1)
                                                        k2.acceptGroupInvitation(op.param1)
                                                        k3.acceptGroupInvitation(op.param1)
                                                        k4.acceptGroupInvitation(op.param1)
                                                        k5.acceptGroupInvitation(op.param1)
                                                        k6.acceptGroupInvitation(op.param1)
                                                        k7.acceptGroupInvitation(op.param1)
                                                        k8.acceptGroupInvitation(op.param1)
                                                        k9.acceptGroupInvitation(op.param1)
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(KICKER).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k4.kickoutFromGroup(op.param1,[op.param2])
                                                                k4.inviteIntoGroup(op.param1,[op.param3])
                                                                k5.acceptGroupInvitation(op.param1)
                                                            except:
                                                                pass
                                                                                         
                return
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k5.kickoutFromGroup(op.param1,[op.param2])
                        k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        k6.acceptGroupInvitation(op.param1)
                        k7.acceptGroupInvitation(op.param1)
                        k8.acceptGroupInvitation(op.param1)
                        k9.acceptGroupInvitation(op.param1)
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k6.kickoutFromGroup(op.param1,[op.param2])
                            k6.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            cl.acceptGroupInvitation(op.param1)
                            k1.acceptGroupInvitation(op.param1)
                            k2.acceptGroupInvitation(op.param1)
                            k3.acceptGroupInvitation(op.param1)
                            k4.acceptGroupInvitation(op.param1)
                            k5.acceptGroupInvitation(op.param1)
                            k6.acceptGroupInvitation(op.param1)
                            k7.acceptGroupInvitation(op.param1)
                            k8.acceptGroupInvitation(op.param1)
                            k9.acceptGroupInvitation(op.param1)
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k7.kickoutFromGroup(op.param1,[op.param2])
                                k7.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                cl.acceptGroupInvitation(op.param1)
                                k1.acceptGroupInvitation(op.param1)
                                k2.acceptGroupInvitation(op.param1)
                                k3.acceptGroupInvitation(op.param1)
                                k4.acceptGroupInvitation(op.param1)
                                k5.acceptGroupInvitation(op.param1)
                                k6.acceptGroupInvitation(op.param1)
                                k7.acceptGroupInvitation(op.param1)
                                k8.acceptGroupInvitation(op.param1)
                                k9.acceptGroupInvitation(op.param1)
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    k8.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    k6.acceptGroupInvitation(op.param1)
                                    k7.acceptGroupInvitation(op.param1)
                                    k8.acceptGroupInvitation(op.param1)
                                    k9.acceptGroupInvitation(op.param1)
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                        k9.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.acceptGroupInvitation(op.param1)
                                        k1.acceptGroupInvitation(op.param1)
                                        k2.acceptGroupInvitation(op.param1)
                                        k3.acceptGroupInvitation(op.param1)
                                        k4.acceptGroupInvitation(op.param1)
                                        k5.acceptGroupInvitation(op.param1)
                                        k6.acceptGroupInvitation(op.param1)
                                        k7.acceptGroupInvitation(op.param1)
                                        k8.acceptGroupInvitation(op.param1)
                                        k9.acceptGroupInvitation(op.param1)
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                            k10.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                            cl.acceptGroupInvitation(op.param1)
                                            k1.acceptGroupInvitation(op.param1)
                                            k2.acceptGroupInvitation(op.param1)
                                            k3.acceptGroupInvitation(op.param1)
                                            k4.acceptGroupInvitation(op.param1)
                                            k5.acceptGroupInvitation(op.param1)
                                            k6.acceptGroupInvitation(op.param1)
                                            k7.acceptGroupInvitation(op.param1)
                                            k8.acceptGroupInvitation(op.param1)
                                            k9.acceptGroupInvitation(op.param1)
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k4.kickoutFromGroup(op.param1,[op.param2])
                                                k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                cl.acceptGroupInvitation(op.param1)
                                                k1.acceptGroupInvitation(op.param1)
                                                k2.acceptGroupInvitation(op.param1)
                                                k3.acceptGroupInvitation(op.param1)
                                                k4.acceptGroupInvitation(op.param1)
                                                k5.acceptGroupInvitation(op.param1)
                                                k6.acceptGroupInvitation(op.param1)
                                                k7.acceptGroupInvitation(op.param1)
                                                k8.acceptGroupInvitation(op.param1)
                                                k9.acceptGroupInvitation(op.param1)
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                                    k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    k1.acceptGroupInvitation(op.param1)
                                                    k2.acceptGroupInvitation(op.param1)
                                                    k3.acceptGroupInvitation(op.param1)
                                                    k4.acceptGroupInvitation(op.param1)
                                                    k5.acceptGroupInvitation(op.param1)
                                                    k6.acceptGroupInvitation(op.param1)
                                                    k7.acceptGroupInvitation(op.param1)
                                                    k8.acceptGroupInvitation(op.param1)
                                                    k9.acceptGroupInvitation(op.param1)
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                                        k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        k1.acceptGroupInvitation(op.param1)
                                                        k2.acceptGroupInvitation(op.param1)
                                                        k3.acceptGroupInvitation(op.param1)
                                                        k4.acceptGroupInvitation(op.param1)
                                                        k5.acceptGroupInvitation(op.param1)
                                                        k6.acceptGroupInvitation(op.param1)
                                                        k7.acceptGroupInvitation(op.param1)
                                                        k8.acceptGroupInvitation(op.param1)
                                                        k9.acceptGroupInvitation(op.param1)
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(KICKER).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                                k4.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    k4.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass
                                                            
                return
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k6.kickoutFromGroup(op.param1,[op.param2])
                        k6.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        k6.acceptGroupInvitation(op.param1)
                        k7.acceptGroupInvitation(op.param1)
                        k8.acceptGroupInvitation(op.param1)
                        k9.acceptGroupInvitation(op.param1)
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            cl.acceptGroupInvitation(op.param1)
                            k1.acceptGroupInvitation(op.param1)
                            k2.acceptGroupInvitation(op.param1)
                            k3.acceptGroupInvitation(op.param1)
                            k4.acceptGroupInvitation(op.param1)
                            k5.acceptGroupInvitation(op.param1)
                            k6.acceptGroupInvitation(op.param1)
                            k7.acceptGroupInvitation(op.param1)
                            k8.acceptGroupInvitation(op.param1)
                            k9.acceptGroupInvitation(op.param1)
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                cl.acceptGroupInvitation(op.param1)
                                k1.acceptGroupInvitation(op.param1)
                                k2.acceptGroupInvitation(op.param1)
                                k3.acceptGroupInvitation(op.param1)
                                k4.acceptGroupInvitation(op.param1)
                                k5.acceptGroupInvitation(op.param1)
                                k6.acceptGroupInvitation(op.param1)
                                k7.acceptGroupInvitation(op.param1)
                                k8.acceptGroupInvitation(op.param1)
                                k9.acceptGroupInvitation(op.param1)
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                    k9.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    k6.acceptGroupInvitation(op.param1)
                                    k7.acceptGroupInvitation(op.param1)
                                    k8.acceptGroupInvitation(op.param1)
                                    k9.acceptGroupInvitation(op.param1)
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                        k10.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.acceptGroupInvitation(op.param1)
                                        k1.acceptGroupInvitation(op.param1)
                                        k2.acceptGroupInvitation(op.param1)
                                        k3.acceptGroupInvitation(op.param1)
                                        k4.acceptGroupInvitation(op.param1)
                                        k5.acceptGroupInvitation(op.param1)
                                        k6.acceptGroupInvitation(op.param1)
                                        k7.acceptGroupInvitation(op.param1)
                                        k8.acceptGroupInvitation(op.param1)
                                        k9.acceptGroupInvitation(op.param1)
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                            cl.acceptGroupInvitation(op.param1)
                                            k1.acceptGroupInvitation(op.param1)
                                            k2.acceptGroupInvitation(op.param1)
                                            k3.acceptGroupInvitation(op.param1)
                                            k4.acceptGroupInvitation(op.param1)
                                            k5.acceptGroupInvitation(op.param1)
                                            k6.acceptGroupInvitation(op.param1)
                                            k7.acceptGroupInvitation(op.param1)
                                            k8.acceptGroupInvitation(op.param1)
                                            k9.acceptGroupInvitation(op.param1)
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k1.kickoutFromGroup(op.param1,[op.param2])
                                                k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                cl.acceptGroupInvitation(op.param1)
                                                k1.acceptGroupInvitation(op.param1)
                                                k2.acceptGroupInvitation(op.param1)
                                                k3.acceptGroupInvitation(op.param1)
                                                k4.acceptGroupInvitation(op.param1)
                                                k5.acceptGroupInvitation(op.param1)
                                                k6.acceptGroupInvitation(op.param1)
                                                k7.acceptGroupInvitation(op.param1)
                                                k8.acceptGroupInvitation(op.param1)
                                                k9.acceptGroupInvitation(op.param1)
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                    k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    k1.acceptGroupInvitation(op.param1)
                                                    k2.acceptGroupInvitation(op.param1)
                                                    k3.acceptGroupInvitation(op.param1)
                                                    k4.acceptGroupInvitation(op.param1)
                                                    k5.acceptGroupInvitation(op.param1)
                                                    k6.acceptGroupInvitation(op.param1)
                                                    k7.acceptGroupInvitation(op.param1)
                                                    k8.acceptGroupInvitation(op.param1)
                                                    k9.acceptGroupInvitation(op.param1)
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                        k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        k1.acceptGroupInvitation(op.param1)
                                                        k2.acceptGroupInvitation(op.param1)
                                                        k3.acceptGroupInvitation(op.param1)
                                                        k4.acceptGroupInvitation(op.param1)
                                                        k5.acceptGroupInvitation(op.param1)
                                                        k6.acceptGroupInvitation(op.param1)
                                                        k7.acceptGroupInvitation(op.param1)
                                                        k8.acceptGroupInvitation(op.param1)
                                                        k9.acceptGroupInvitation(op.param1)
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(KICKER).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                                k4.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    k4.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass
                                                            
                return
            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k7.kickoutFromGroup(op.param1,[op.param2])
                        k7.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        k6.acceptGroupInvitation(op.param1)
                        k7.acceptGroupInvitation(op.param1)
                        k8.acceptGroupInvitation(op.param1)
                        k9.acceptGroupInvitation(op.param1)
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            k8.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            cl.acceptGroupInvitation(op.param1)
                            k1.acceptGroupInvitation(op.param1)
                            k2.acceptGroupInvitation(op.param1)
                            k3.acceptGroupInvitation(op.param1)
                            k4.acceptGroupInvitation(op.param1)
                            k5.acceptGroupInvitation(op.param1)
                            k6.acceptGroupInvitation(op.param1)
                            k7.acceptGroupInvitation(op.param1)
                            k8.acceptGroupInvitation(op.param1)
                            k9.acceptGroupInvitation(op.param1)
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k9.kickoutFromGroup(op.param1,[op.param2])
                                k9.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                cl.acceptGroupInvitation(op.param1)
                                k1.acceptGroupInvitation(op.param1)
                                k2.acceptGroupInvitation(op.param1)
                                k3.acceptGroupInvitation(op.param1)
                                k4.acceptGroupInvitation(op.param1)
                                k5.acceptGroupInvitation(op.param1)
                                k6.acceptGroupInvitation(op.param1)
                                k7.acceptGroupInvitation(op.param1)
                                k8.acceptGroupInvitation(op.param1)
                                k9.acceptGroupInvitation(op.param1)
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                    k10.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    k6.acceptGroupInvitation(op.param1)
                                    k7.acceptGroupInvitation(op.param1)
                                    k8.acceptGroupInvitation(op.param1)
                                    k9.acceptGroupInvitation(op.param1)
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k6.kickoutFromGroup(op.param1,[op.param2])
                                        k6.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.acceptGroupInvitation(op.param1)
                                        k1.acceptGroupInvitation(op.param1)
                                        k2.acceptGroupInvitation(op.param1)
                                        k3.acceptGroupInvitation(op.param1)
                                        k4.acceptGroupInvitation(op.param1)
                                        k5.acceptGroupInvitation(op.param1)
                                        k6.acceptGroupInvitation(op.param1)
                                        k7.acceptGroupInvitation(op.param1)
                                        k8.acceptGroupInvitation(op.param1)
                                        k9.acceptGroupInvitation(op.param1)
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                            k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                            cl.acceptGroupInvitation(op.param1)
                                            k1.acceptGroupInvitation(op.param1)
                                            k2.acceptGroupInvitation(op.param1)
                                            k3.acceptGroupInvitation(op.param1)
                                            k4.acceptGroupInvitation(op.param1)
                                            k5.acceptGroupInvitation(op.param1)
                                            k6.acceptGroupInvitation(op.param1)
                                            k7.acceptGroupInvitation(op.param1)
                                            k8.acceptGroupInvitation(op.param1)
                                            k9.acceptGroupInvitation(op.param1)
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                cl.acceptGroupInvitation(op.param1)
                                                k1.acceptGroupInvitation(op.param1)
                                                k2.acceptGroupInvitation(op.param1)
                                                k3.acceptGroupInvitation(op.param1)
                                                k4.acceptGroupInvitation(op.param1)
                                                k5.acceptGroupInvitation(op.param1)
                                                k6.acceptGroupInvitation(op.param1)
                                                k7.acceptGroupInvitation(op.param1)
                                                k8.acceptGroupInvitation(op.param1)
                                                k9.acceptGroupInvitation(op.param1)
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                                    k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    k1.acceptGroupInvitation(op.param1)
                                                    k2.acceptGroupInvitation(op.param1)
                                                    k3.acceptGroupInvitation(op.param1)
                                                    k4.acceptGroupInvitation(op.param1)
                                                    k5.acceptGroupInvitation(op.param1)
                                                    k6.acceptGroupInvitation(op.param1)
                                                    k7.acceptGroupInvitation(op.param1)
                                                    k8.acceptGroupInvitation(op.param1)
                                                    k9.acceptGroupInvitation(op.param1)
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                                        k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        k1.acceptGroupInvitation(op.param1)
                                                        k2.acceptGroupInvitation(op.param1)
                                                        k3.acceptGroupInvitation(op.param1)
                                                        k4.acceptGroupInvitation(op.param1)
                                                        k5.acceptGroupInvitation(op.param1)
                                                        k6.acceptGroupInvitation(op.param1)
                                                        k7.acceptGroupInvitation(op.param1)
                                                        k8.acceptGroupInvitation(op.param1)
                                                        k9.acceptGroupInvitation(op.param1)
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(KICKER).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                                k4.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    k4.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass                                                                        
                return
            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k8.kickoutFromGroup(op.param1,[op.param2])
                        k8.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        k6.acceptGroupInvitation(op.param1)
                        k7.acceptGroupInvitation(op.param1)
                        k8.acceptGroupInvitation(op.param1)
                        k9.acceptGroupInvitation(op.param1)
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            cl.acceptGroupInvitation(op.param1)
                            k1.acceptGroupInvitation(op.param1)
                            k2.acceptGroupInvitation(op.param1)
                            k3.acceptGroupInvitation(op.param1)
                            k4.acceptGroupInvitation(op.param1)
                            k5.acceptGroupInvitation(op.param1)
                            k6.acceptGroupInvitation(op.param1)
                            k7.acceptGroupInvitation(op.param1)
                            k8.acceptGroupInvitation(op.param1)
                            k9.acceptGroupInvitation(op.param1)
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k10.kickoutFromGroup(op.param1,[op.param2])
                                k10.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                cl.acceptGroupInvitation(op.param1)
                                k1.acceptGroupInvitation(op.param1)
                                k2.acceptGroupInvitation(op.param1)
                                k3.acceptGroupInvitation(op.param1)
                                k4.acceptGroupInvitation(op.param1)
                                k5.acceptGroupInvitation(op.param1)
                                k6.acceptGroupInvitation(op.param1)
                                k7.acceptGroupInvitation(op.param1)
                                k8.acceptGroupInvitation(op.param1)
                                k9.acceptGroupInvitation(op.param1)
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                    k7.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    k6.acceptGroupInvitation(op.param1)
                                    k7.acceptGroupInvitation(op.param1)
                                    k8.acceptGroupInvitation(op.param1)
                                    k9.acceptGroupInvitation(op.param1)
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.acceptGroupInvitation(op.param1)
                                        k1.acceptGroupInvitation(op.param1)
                                        k2.acceptGroupInvitation(op.param1)
                                        k3.acceptGroupInvitation(op.param1)
                                        k4.acceptGroupInvitation(op.param1)
                                        k5.acceptGroupInvitation(op.param1)
                                        k6.acceptGroupInvitation(op.param1)
                                        k7.acceptGroupInvitation(op.param1)
                                        k8.acceptGroupInvitation(op.param1)
                                        k9.acceptGroupInvitation(op.param1)
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                            cl.acceptGroupInvitation(op.param1)
                                            k1.acceptGroupInvitation(op.param1)
                                            k2.acceptGroupInvitation(op.param1)
                                            k3.acceptGroupInvitation(op.param1)
                                            k4.acceptGroupInvitation(op.param1)
                                            k5.acceptGroupInvitation(op.param1)
                                            k6.acceptGroupInvitation(op.param1)
                                            k7.acceptGroupInvitation(op.param1)
                                            k8.acceptGroupInvitation(op.param1)
                                            k9.acceptGroupInvitation(op.param1)
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                cl.acceptGroupInvitation(op.param1)
                                                k1.acceptGroupInvitation(op.param1)
                                                k2.acceptGroupInvitation(op.param1)
                                                k3.acceptGroupInvitation(op.param1)
                                                k4.acceptGroupInvitation(op.param1)
                                                k5.acceptGroupInvitation(op.param1)
                                                k6.acceptGroupInvitation(op.param1)
                                                k7.acceptGroupInvitation(op.param1)
                                                k8.acceptGroupInvitation(op.param1)
                                                k9.acceptGroupInvitation(op.param1)
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                                    k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    k1.acceptGroupInvitation(op.param1)
                                                    k2.acceptGroupInvitation(op.param1)
                                                    k3.acceptGroupInvitation(op.param1)
                                                    k4.acceptGroupInvitation(op.param1)
                                                    k5.acceptGroupInvitation(op.param1)
                                                    k6.acceptGroupInvitation(op.param1)
                                                    k7.acceptGroupInvitation(op.param1)
                                                    k8.acceptGroupInvitation(op.param1)
                                                    k9.acceptGroupInvitation(op.param1)
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                                        k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        k1.acceptGroupInvitation(op.param1)
                                                        k2.acceptGroupInvitation(op.param1)
                                                        k3.acceptGroupInvitation(op.param1)
                                                        k4.acceptGroupInvitation(op.param1)
                                                        k5.acceptGroupInvitation(op.param1)
                                                        k6.acceptGroupInvitation(op.param1)
                                                        k7.acceptGroupInvitation(op.param1)
                                                        k8.acceptGroupInvitation(op.param1)
                                                        k9.acceptGroupInvitation(op.param1)
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(KICKER).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                                k4.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    k4.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass
                return
            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k9.kickoutFromGroup(op.param1,[op.param2])
                        k9.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        k6.acceptGroupInvitation(op.param1)
                        k7.acceptGroupInvitation(op.param1)
                        k8.acceptGroupInvitation(op.param1)
                        k9.acceptGroupInvitation(op.param1)
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            k10.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            cl.acceptGroupInvitation(op.param1)
                            k1.acceptGroupInvitation(op.param1)
                            k2.acceptGroupInvitation(op.param1)
                            k3.acceptGroupInvitation(op.param1)
                            k4.acceptGroupInvitation(op.param1)
                            k5.acceptGroupInvitation(op.param1)
                            k6.acceptGroupInvitation(op.param1)
                            k7.acceptGroupInvitation(op.param1)
                            k8.acceptGroupInvitation(op.param1)
                            k9.acceptGroupInvitation(op.param1)
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                cl.acceptGroupInvitation(op.param1)
                                k1.acceptGroupInvitation(op.param1)
                                k2.acceptGroupInvitation(op.param1)
                                k3.acceptGroupInvitation(op.param1)
                                k4.acceptGroupInvitation(op.param1)
                                k5.acceptGroupInvitation(op.param1)
                                k6.acceptGroupInvitation(op.param1)
                                k7.acceptGroupInvitation(op.param1)
                                k8.acceptGroupInvitation(op.param1)
                                k9.acceptGroupInvitation(op.param1)
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    k6.acceptGroupInvitation(op.param1)
                                    k7.acceptGroupInvitation(op.param1)
                                    k8.acceptGroupInvitation(op.param1)
                                    k9.acceptGroupInvitation(op.param1)
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.acceptGroupInvitation(op.param1)
                                        k1.acceptGroupInvitation(op.param1)
                                        k2.acceptGroupInvitation(op.param1)
                                        k3.acceptGroupInvitation(op.param1)
                                        k4.acceptGroupInvitation(op.param1)
                                        k5.acceptGroupInvitation(op.param1)
                                        k6.acceptGroupInvitation(op.param1)
                                        k7.acceptGroupInvitation(op.param1)
                                        k8.acceptGroupInvitation(op.param1)
                                        k9.acceptGroupInvitation(op.param1)
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                            cl.acceptGroupInvitation(op.param1)
                                            k1.acceptGroupInvitation(op.param1)
                                            k2.acceptGroupInvitation(op.param1)
                                            k3.acceptGroupInvitation(op.param1)
                                            k4.acceptGroupInvitation(op.param1)
                                            k5.acceptGroupInvitation(op.param1)
                                            k6.acceptGroupInvitation(op.param1)
                                            k7.acceptGroupInvitation(op.param1)
                                            k8.acceptGroupInvitation(op.param1)
                                            k9.acceptGroupInvitation(op.param1)
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k4.kickoutFromGroup(op.param1,[op.param2])
                                                k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                cl.acceptGroupInvitation(op.param1)
                                                k1.acceptGroupInvitation(op.param1)
                                                k2.acceptGroupInvitation(op.param1)
                                                k3.acceptGroupInvitation(op.param1)
                                                k4.acceptGroupInvitation(op.param1)
                                                k5.acceptGroupInvitation(op.param1)
                                                k6.acceptGroupInvitation(op.param1)
                                                k7.acceptGroupInvitation(op.param1)
                                                k8.acceptGroupInvitation(op.param1)
                                                k9.acceptGroupInvitation(op.param1)
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                                    k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    k1.acceptGroupInvitation(op.param1)
                                                    k2.acceptGroupInvitation(op.param1)
                                                    k3.acceptGroupInvitation(op.param1)
                                                    k4.acceptGroupInvitation(op.param1)
                                                    k5.acceptGroupInvitation(op.param1)
                                                    k6.acceptGroupInvitation(op.param1)
                                                    k7.acceptGroupInvitation(op.param1)
                                                    k8.acceptGroupInvitation(op.param1)
                                                    k9.acceptGroupInvitation(op.param1)
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k6.kickoutFromGroup(op.param1,[op.param2])
                                                        k6.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        k1.acceptGroupInvitation(op.param1)
                                                        k2.acceptGroupInvitation(op.param1)
                                                        k3.acceptGroupInvitation(op.param1)
                                                        k4.acceptGroupInvitation(op.param1)
                                                        k5.acceptGroupInvitation(op.param1)
                                                        k6.acceptGroupInvitation(op.param1)
                                                        k7.acceptGroupInvitation(op.param1)
                                                        k8.acceptGroupInvitation(op.param1)
                                                        k9.acceptGroupInvitation(op.param1)
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(KICKER).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                                k4.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    k4.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass
                                                            
                return
            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        k6.acceptGroupInvitation(op.param1)
                        k7.acceptGroupInvitation(op.param1)
                        k8.acceptGroupInvitation(op.param1)
                        k9.acceptGroupInvitation(op.param1)
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            cl.acceptGroupInvitation(op.param1)
                            k1.acceptGroupInvitation(op.param1)
                            k2.acceptGroupInvitation(op.param1)
                            k3.acceptGroupInvitation(op.param1)
                            k4.acceptGroupInvitation(op.param1)
                            k5.acceptGroupInvitation(op.param1)
                            k6.acceptGroupInvitation(op.param1)
                            k7.acceptGroupInvitation(op.param1)
                            k8.acceptGroupInvitation(op.param1)
                            k9.acceptGroupInvitation(op.param1)
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                cl.acceptGroupInvitation(op.param1)
                                k1.acceptGroupInvitation(op.param1)
                                k2.acceptGroupInvitation(op.param1)
                                k3.acceptGroupInvitation(op.param1)
                                k4.acceptGroupInvitation(op.param1)
                                k5.acceptGroupInvitation(op.param1)
                                k6.acceptGroupInvitation(op.param1)
                                k7.acceptGroupInvitation(op.param1)
                                k8.acceptGroupInvitation(op.param1)
                                k9.acceptGroupInvitation(op.param1)
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                    k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    k6.acceptGroupInvitation(op.param1)
                                    k7.acceptGroupInvitation(op.param1)
                                    k8.acceptGroupInvitation(op.param1)
                                    k9.acceptGroupInvitation(op.param1)
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.acceptGroupInvitation(op.param1)
                                        k1.acceptGroupInvitation(op.param1)
                                        k2.acceptGroupInvitation(op.param1)
                                        k3.acceptGroupInvitation(op.param1)
                                        k4.acceptGroupInvitation(op.param1)
                                        k5.acceptGroupInvitation(op.param1)
                                        k6.acceptGroupInvitation(op.param1)
                                        k7.acceptGroupInvitation(op.param1)
                                        k8.acceptGroupInvitation(op.param1)
                                        k9.acceptGroupInvitation(op.param1)
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                            k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                            cl.acceptGroupInvitation(op.param1)
                                            k1.acceptGroupInvitation(op.param1)
                                            k2.acceptGroupInvitation(op.param1)
                                            k3.acceptGroupInvitation(op.param1)
                                            k4.acceptGroupInvitation(op.param1)
                                            k5.acceptGroupInvitation(op.param1)
                                            k6.acceptGroupInvitation(op.param1)
                                            k7.acceptGroupInvitation(op.param1)
                                            k8.acceptGroupInvitation(op.param1)
                                            k9.acceptGroupInvitation(op.param1)
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                cl.acceptGroupInvitation(op.param1)
                                                k1.acceptGroupInvitation(op.param1)
                                                k2.acceptGroupInvitation(op.param1)
                                                k3.acceptGroupInvitation(op.param1)
                                                k4.acceptGroupInvitation(op.param1)
                                                k5.acceptGroupInvitation(op.param1)
                                                k6.acceptGroupInvitation(op.param1)
                                                k7.acceptGroupInvitation(op.param1)
                                                k8.acceptGroupInvitation(op.param1)
                                                k9.acceptGroupInvitation(op.param1)
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                    k6.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    k1.acceptGroupInvitation(op.param1)
                                                    k2.acceptGroupInvitation(op.param1)
                                                    k3.acceptGroupInvitation(op.param1)
                                                    k4.acceptGroupInvitation(op.param1)
                                                    k5.acceptGroupInvitation(op.param1)
                                                    k6.acceptGroupInvitation(op.param1)
                                                    k7.acceptGroupInvitation(op.param1)
                                                    k8.acceptGroupInvitation(op.param1)
                                                    k9.acceptGroupInvitation(op.param1)
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                        k7.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        k1.acceptGroupInvitation(op.param1)
                                                        k2.acceptGroupInvitation(op.param1)
                                                        k3.acceptGroupInvitation(op.param1)
                                                        k4.acceptGroupInvitation(op.param1)
                                                        k5.acceptGroupInvitation(op.param1)
                                                        k6.acceptGroupInvitation(op.param1)
                                                        k7.acceptGroupInvitation(op.param1)
                                                        k8.acceptGroupInvitation(op.param1)
                                                        k9.acceptGroupInvitation(op.param1)
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(KICKER).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                                k4.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    k4.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass
                                                                                                                                               
                return
            if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        k6.acceptGroupInvitation(op.param1)
                        k7.acceptGroupInvitation(op.param1)
                        k8.acceptGroupInvitation(op.param1)
                        k9.acceptGroupInvitation(op.param1)
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            cl.acceptGroupInvitation(op.param1)
                            k1.acceptGroupInvitation(op.param1)
                            k2.acceptGroupInvitation(op.param1)
                            k3.acceptGroupInvitation(op.param1)
                            k4.acceptGroupInvitation(op.param1)
                            k5.acceptGroupInvitation(op.param1)
                            k6.acceptGroupInvitation(op.param1)
                            k7.acceptGroupInvitation(op.param1)
                            k8.acceptGroupInvitation(op.param1)
                            k9.acceptGroupInvitation(op.param1)
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                cl.acceptGroupInvitation(op.param1)
                                k1.acceptGroupInvitation(op.param1)
                                k2.acceptGroupInvitation(op.param1)
                                k3.acceptGroupInvitation(op.param1)
                                k4.acceptGroupInvitation(op.param1)
                                k5.acceptGroupInvitation(op.param1)
                                k6.acceptGroupInvitation(op.param1)
                                k7.acceptGroupInvitation(op.param1)
                                k8.acceptGroupInvitation(op.param1)
                                k9.acceptGroupInvitation(op.param1)
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    k6.acceptGroupInvitation(op.param1)
                                    k7.acceptGroupInvitation(op.param1)
                                    k8.acceptGroupInvitation(op.param1)
                                    k9.acceptGroupInvitation(op.param1)
                                    k10.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.acceptGroupInvitation(op.param1)
                                        k1.acceptGroupInvitation(op.param1)
                                        k2.acceptGroupInvitation(op.param1)
                                        k3.acceptGroupInvitation(op.param1)
                                        k4.acceptGroupInvitation(op.param1)
                                        k5.acceptGroupInvitation(op.param1)
                                        k6.acceptGroupInvitation(op.param1)
                                        k7.acceptGroupInvitation(op.param1)
                                        k8.acceptGroupInvitation(op.param1)
                                        k9.acceptGroupInvitation(op.param1)
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                            cl.acceptGroupInvitation(op.param1)
                                            k1.acceptGroupInvitation(op.param1)
                                            k2.acceptGroupInvitation(op.param1)
                                            k3.acceptGroupInvitation(op.param1)
                                            k4.acceptGroupInvitation(op.param1)
                                            k5.acceptGroupInvitation(op.param1)
                                            k6.acceptGroupInvitation(op.param1)
                                            k7.acceptGroupInvitation(op.param1)
                                            k8.acceptGroupInvitation(op.param1)
                                            k9.acceptGroupInvitation(op.param1)
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                                k6.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                cl.acceptGroupInvitation(op.param1)
                                                k1.acceptGroupInvitation(op.param1)
                                                k2.acceptGroupInvitation(op.param1)
                                                k3.acceptGroupInvitation(op.param1)
                                                k4.acceptGroupInvitation(op.param1)
                                                k5.acceptGroupInvitation(op.param1)
                                                k6.acceptGroupInvitation(op.param1)
                                                k7.acceptGroupInvitation(op.param1)
                                                k8.acceptGroupInvitation(op.param1)
                                                k9.acceptGroupInvitation(op.param1)
                                                k10.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                                    k7.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    k1.acceptGroupInvitation(op.param1)
                                                    k2.acceptGroupInvitation(op.param1)
                                                    k3.acceptGroupInvitation(op.param1)
                                                    k4.acceptGroupInvitation(op.param1)
                                                    k5.acceptGroupInvitation(op.param1)
                                                    k6.acceptGroupInvitation(op.param1)
                                                    k7.acceptGroupInvitation(op.param1)
                                                    k8.acceptGroupInvitation(op.param1)
                                                    k9.acceptGroupInvitation(op.param1)
                                                    k10.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                        k8.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        k1.acceptGroupInvitation(op.param1)
                                                        k2.acceptGroupInvitation(op.param1)
                                                        k3.acceptGroupInvitation(op.param1)
                                                        k4.acceptGroupInvitation(op.param1)
                                                        k5.acceptGroupInvitation(op.param1)
                                                        k6.acceptGroupInvitation(op.param1)
                                                        k7.acceptGroupInvitation(op.param1)
                                                        k8.acceptGroupInvitation(op.param1)
                                                        k9.acceptGroupInvitation(op.param1)
                                                        k10.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(KICKER).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                                k4.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    k4.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass
                                                            
                return
                
        if op.type == 55:
            if op.param3 in bl['blacklist'] and op.param2 in bl['blacklist'] and op.param2 not in Bots and op.param2 not in admin:
                try:
                    k1.cancelGroupInvitation(op.param1,[op.param3])
                    k1.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        k2.cancelGroupInvitation(op.param1,[op.param3])
                        k2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k3.cancelGroupInvitation(op.param1,[op.param3])
                            k3.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                k4.cancelGroupInvitation(op.param1,[op.param3])
                                k4.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                     k5.cancelGroupInvitation(op.param1,[op.param3])
                                     k5.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
#====================================================================                                                                
#===================================================================================================              
        if op.type == 25 or op.type == 26:
          if settings['SpamInvite'] == True:
            msg = op.message
            sender = msg._from
            receiver = msg.to
            if msg.contentType == 13:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            cl.sendMessage(msg.to, korban + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)                                
                                cl.createGroup("TES BOT PUBLIK",[target]) 
                                cl.createGroup("TES BOT PUBLIK",[target])            
                                cl.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                settings['SpamInvite'] = False
                            except:             
                                 cl.sendMessage(msg.to, 'Contact error')
                                 settings['SpamInvite'] = False
                                 break
                                 
        if op.type == 26:           
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 16:
                  if msg.toType in (2,1,0):
                     try:
                         mat = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                         cl.likePost(mat[0], mat[1], 1003)
                         cl.createComment(mat[0], mat[1], "ᴀᴜᴛᴏʟɪᴋᴇ ʙʏ: \n\n\n\n™S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ\n\n\n\nᴄʀᴇᴀᴛᴏʀ:\nhttp://line.me/ti/p/~teambotprotect\nɢɪᴛhᴜʙ:\ngithub.com/dhenza1415\nchanel ʏᴏᴜᴛᴜʙᴇ:\nhttps://youtu.be/CRqXKcTl6IY\n\nnew ᴄʜᴀɴᴇʟ:\nhttps://youtu.be/6UGH_4gG9qk")
                         cl.sendReplyMessage(msg.id, to, "➥[TEAM BOT PROTECT LIKE]\nSucsess..👍\nCek Timeline👌\n\nᴄʀᴇᴀᴛᴏʀ:\nhttp://line.me/ti/p/~teambotprotect\nɢɪᴛhᴜʙ:\ngithub.com/dhenza1415\nchanel ʏᴏᴜᴛᴜʙᴇ:\nhttps://youtu.be/CRqXKcTl6IY\n\nnew ᴄʜᴀɴᴇʟ:\nhttps://youtu.be/6UGH_4gG9qk")
                     except Exception as e:
                         cl.sendMessage(msg.to, str(e))               
#===================================================================================================           
#===================================================================================================                      
        if op.type == 55:
            if op.param2 in bl["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
                
        if op.type == 55:
            if op.param2 in bl["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                G = cl.getGroup(op.param1)	
                G.preventedJoinByTicket = True		
                random.choice(ABC).updateGroup(G)	
                random.choice(ABC).sendMessage(op.param1,"mamam tu")					
                random.choice(ABC).sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)														
            else:
                pass

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)
                        cl.sendMessage(op.param1, None, contentMetadata={"STKID":"13162615","STKPKGID":"1326453","STKVER":"1"}, contentType=7)
                        
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  " Gambar Dihapus \n Pengirim : "
                                ret_ = " Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  " Pesan Dihapus \n"
                                ret_ += " Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  " Sticker Dihapus \n"
                                ret_ += " Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e) 
                    
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\nSticker Info"
                   ret_ += "\nSticker ID : {}".format(stk_id)
                   ret_ += "\nSticker Version : {}".format(stk_ver)
                   ret_ += "\nSticker Package : {}".format(pkg_id)
                   ret_ += "\nSticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\nSticker Info"
                   ret_ += "\nSticker ID : {}".format(stk_id)
                   ret_ += "\nSticker Version : {}".format(stk_ver)
                   ret_ += "\nSticker Package : {}".format(pkg_id)
                   ret_ += "\nSticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime};
            
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                   if msg._from in wait["blacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           saints = cl.getContact(msg._from)
                           sendMention(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"25628787","STKPKGID":"1818607","STKVER":"1"}, contentType=7)
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendImageWithURL(msg.to,image)
                           rnd = ["yg nge tag semoga masuk surga amin"]
                           p = random.choice(rnd)
                           lang = 'id'
                           tts = gTTS(text=p, lang=lang)
                           tts.save("hasil.mp3")
                           cl.sendAudio(msg.to,"hasil.mp3")
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"25628787","STKPKGID":"1818607","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "No tag me....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
                           
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nãLink Stickerã" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
                        
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "「 ᴅᴇᴛᴀɪʟ ᴘᴏsᴛɪɴɢᴀɴ 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\n• ˢᵏℹ༓ᴘᴇɴᴜʟɪs : {}".format(str(contact.displayName))
                            else:
                                auth = "\n• ˢᵏℹ ༓ᴘᴇɴᴜʟɪs : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n• ˢᵏℹ༓sᴛɪᴄᴋᴇʀ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• ˢᵏℹ༓ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n• ˢᵏℹ༓Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• ˢᵏℹ༓Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n• ˢᵏℹ༓Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• ˢᵏℹ༓Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• ˢᵏℹ༓Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• ˢᵏℹ༓Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• ˢᵏℹ༓Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                                url = msg.contentMetadata['postEndUrl']
                            cl.sendMessage(to, str(ret_))
                            cl.likePost(url[25:58], url[66:], likeType=1005)
                            cl.createComment(url[25:58], url[66:], wait["comment"])                           
#=======================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nãLink Stickerã" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots&media         	   
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["AddstickerTag"]["status"] == True:
                         settings["AddstickerTag"]["sid"] = msg.contentMetadata["STKID"]
                         settings["AddstickerTag"]["spkg"] = msg.contentMetadata["STKPKGID"]
                         cl.sendMessage(msg.to, "Sticker respon hasben changed")
                         settings["AddstickerTag"]["status"] = False
                         
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            cl.sendMessage(msg.to,"Send gambarnya...")
                            
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            cl.sendMessage(msg.to,"Change Video Profile Success!!!")
                            
               if msg.contentType == 1:
                  if msg._from in mid:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
                         
               if msg.contentType == 2:
                  if msg._from in mid:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
                         
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
                         
               if msg.contentType == 3:
                  if msg._from in mid:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
                         
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                      print ("Read")
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                          if msg._from in mid:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in mid:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in mid:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in mid:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
                               
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Nothing in bot")
#SC ADD STAFF
                 if msg._from in owner or msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Already in stafflist")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Succes add to staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes expel to staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Nothing in staff")
#SC ADD ADMIN
                 if msg._from in owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Already in Admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Succes Add to Admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes to expel admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#SC ADD BLACKLIST
                 if msg._from in owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Already in blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to blacklist")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete blacklist")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in blacklist")
#SC TALKBAN
                 if msg._from in owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Already in Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to Talkban")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete Talkban")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in Talkban")
#SC UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Succes change pict group")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["SKfoto"]:
                            path = k1.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Amid]
                            k1.updateProfilePicture(path)
                            k1.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["SKfoto"]:
                            path = k2.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Bmid]
                            k2.updateProfilePicture(path)
                            k2.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["SKfoto"]:
                            path = k3.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Cmid]
                            k3.updateProfilePicture(path)
                            k3.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["SKfoto"]:
                            path = k4.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Dmid]
                            k4.updateProfilePicture(path)
                            k4.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["SKfoto"]:
                            path = k5.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Emid]
                            k5.updateProfilePicture(path)
                            k5.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Fmid in Setmain["SKfoto"]:
                            path = k6.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Fmid]
                            k6.updateProfilePicture(path)
                            k6.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Gmid in Setmain["SKfoto"]:
                            path = k7.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Gmid]
                            k7.updateProfilePicture(path)
                            k7.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Hmid in Setmain["SKfoto"]:
                            path = k8.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Hmid]
                            k8.updateProfilePicture(path)
                            k8.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Imid in Setmain["SKfoto"]:
                            path = k9.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Imid]
                            k9.updateProfilePicture(path)
                            k9.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Jmid in Setmain["SKfoto"]:
                            path = k10.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Jmid]
                            k10.updateProfilePicture(path)
                            k10.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif g1MID in Setmain["SKfoto"]:
                            path = g1.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][g1MID]
                            g1.updateProfilePicture(path)
                            g1.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif g2MID in Setmain["SKfoto"]:
                            path = g2.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][g2MID]
                            g2.updateProfilePicture(path)
                            g2.sendMessage(msg.to,"Foto berhasil dirubah")
                            
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = k1.downloadObjectMsg(msg_id)
                     path2 = k2.downloadObjectMsg(msg_id)
                     path3 = k3.downloadObjectMsg(msg_id)
                     path4 = k4.downloadObjectMsg(msg_id)
                     path5 = k5.downloadObjectMsg(msg_id)
                     path6 = k6.downloadObjectMsg(msg_id)
                     path7 = k7.downloadObjectMsg(msg_id)
                     path8 = k8.downloadObjectMsg(msg_id)
                     path9 = k9.downloadObjectMsg(msg_id)
                     path10 = k10.downloadObjectMsg(msg_id)
                     path11 = g1.downloadObjectMsg(msg_id)
                     path12 = g2.downloadObjectMsg(msg_id)             
                     settings["changePicture"] = False
                     k1.updateProfilePicture(path1)
                     k1.sendMessage(msg.to, "ᴀsɪsᴛ 1 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғᴏᴛᴏ")
                     k2.updateProfilePicture(path2)
                     k2.sendMessage(msg.to, "ᴀsɪsᴛ 2 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғʜᴏᴛᴏ")
                     k3.updateProfilePicture(path3)
                     k3.sendMessage(msg.to, "ᴀsɪsᴛ 3 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғᴏᴛᴏ")
                     k4.updateProfilePicture(path4)
                     k4.sendMessage(msg.to, "ᴀsɪsᴛ 4 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғᴏᴛᴏ")
                     k5.updateProfilePicture(path5)
                     k5.sendMessage(msg.to, "ᴀsɪsᴛ 5 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғᴏᴛᴏ")
                     k6.updateProfilePicture(path6)
                     k6.sendMessage(msg.to, "ᴀsɪsᴛ 6 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғᴏᴛᴏ")
                     k7.updateProfilePicture(path7)
                     k7.sendMessage(msg.to, "ᴀsɪsᴛ 7 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғᴏᴛᴏ")
                     k8.updateProfilePicture(path8)
                     k8.sendMessage(msg.to, "ᴀsɪsᴛ 8 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғᴏᴛᴏ")
                     k9.updateProfilePicture(path9)
                     k9.sendMessage(msg.to, "ᴀsɪsᴛ 9 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғᴏᴛᴏ")
                     k10.updateProfilePicture(path10)
                     k10.sendMessage(msg.to, "ᴀsɪsᴛ 10 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғᴏᴛᴏ")
                     g1.updateProfilePicture(path11)
                     g1.sendMessage(msg.to, "ʜᴀɴᴛᴜ 1 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғᴏᴛᴏ")
                     g2.updateProfilePicture(path12)
                     g2.sendMessage(msg.to, "ʜᴀɴᴛᴜ 2 ʙᴇʀʜᴀsɪʟ ᴜᴘᴅᴀᴛᴇ ғᴏᴛᴏ")
                     

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "on":
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "Bot telah di aktifkan")
                                
                        elif cmd == "off":
                            if msg._from in owner or msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "Bot off smentara waktu")
                                
                        elif cmd == 'vp':
                        	if msg._from in owner or msg._from in admin:
                                 me = cl.getContact(mid)
                                 cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage2 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage2))

                        elif cmd == "protect":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)                                
                                md = "│╔══[ TΣΔM βΩT PRΩTΣCTsᴋ ] \n"                                
                                if wait["sticker"] == True: md+="│╠══[  ON  ] sᴛɪᴄᴋᴇʀ✔️\n"
                                else: md+="│╠══[ OFF ] sᴛɪᴄᴋᴇʀ❌\n"
                                if wait["contact"] == True: md+="│╠══[  ON  ] ᴄᴏɴᴛᴀᴄᴛ✔️\n"
                                else: md+="│╠══[ OFF ] ᴄᴏɴᴛᴀᴄᴛ❌\n"
                                if wait["detectMention"] == True: md+="│╠══[  ON  ] ʀᴇsᴘᴏɴ✔️\n"
                                else: md+="│╠══[ OFF ] ʀᴇsᴘᴏɴ❌\n"
                                if wait["autoJoin"] == True: md+="│╠══[  ON  ] ᴀᴜᴛᴏᴊᴏɪɴ✔️\n"
                                else: md+="│╠══[ OFF ] ᴀᴜᴛᴏᴊᴏɪɴ❌\n"
                                if settings["autoJoinTicket"] == True: md+="│╠══[  ON  ] ᴊᴏɪɴᴛɪᴄᴋᴇᴛ✔️\n"
                                else: md+="│╠══[ OFF ] ᴊᴏɪɴᴛɪᴄᴋᴇᴛ❌\n"
                                if settings["unsendMessage"] == True: md+="│╠══[  ON  ] ᴜɴsᴇɴᴅ✔️\n"
                                else: md+="│╠══[ OFF ] ᴜɴsᴇɴᴅ❌\n"
                                if wait["autoAdd"] == True: md+="│╠══[  ON  ] ᴀᴜᴛᴏᴀᴅᴅ✔️\n"
                                else: md+="│╠══[ OFF ] ᴀᴜᴛᴏᴀᴅᴅ❌\n"
                                if msg.to in welcome: md+="│╠══[  ON  ] ᴡᴇʟᴄᴏᴍᴇ✔️\n"
                                else: md+="│╠══[ OFF ] ᴡᴇʟᴄᴏᴍᴇ❌\n"
                                if wait["autoLeave"] == True: md+="│╠══[  ON  ] ᴀᴜᴛᴏʟᴇᴀᴠᴇ✔️\n"
                                else: md+="│╠══[ OFF ] ᴀᴜᴛᴏʟᴇᴀᴠᴇ❌\n"
                                if msg.to in ghost: md+="│╠══[  ON  ] ɢʜᴏsᴛ✔️\n"
                                else: md+="│╠══[ OFF ] ɢʜᴏsᴛ❌\n"
                                if msg.to in protectqr: md+="│╠══[  ON  ] ᴘʀᴏᴛᴇᴄᴛǫʀ✔️\n"
                                else: md+="│╠══[ OFF ] ᴘʀᴏᴛᴇᴄᴛǫʀ❌\n"
                                if msg.to in protectjoin: md+="│╠══[  ON  ] ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ✔️\n"
                                else: md+="│╠══[ OFF ] ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ❌\n"
                                if msg.to in protectkick: md+="│╠══[  ON  ] ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ✔️\n"
                                else: md+="│╠══[ OFF ] ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ❌\n"
                                if msg.to in protectinvite: md+="│╠══[  ON  ] ᴘʀᴏᴛᴇᴄᴛɪɴᴠɪᴛᴇ✔️\n"
                                else: md+="│╠══[ OFF ] ᴘʀᴏᴛᴇᴄᴛɪɴᴠɪᴛᴇ❌\n"
                                if msg.to in protectantijs: md+="│╠══[  ON  ] ᴊs✔️\n"
                                else: md+="│╠══[ OFF ] ᴊs❌\n"                                
                                if msg.to in protectcancel: md+="│╠══[  ON  ] ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ✔️\n"
                                else: md+="│╠══[ OFF ] ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ❌\n"
                                md+= "│╚══[ TΣΔM βΩT PRΩTΣCTsᴋ ]"
                                cl.sendMessage(msg.to, md+"\n│ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│ᴊᴀᴍ  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")   
                                                                 
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                cl.sendMessage(msg.to,"Creator Kami")
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendMention(msg.to, sender, "ᴍʏ ᴄʀᴇᴀᴛᴏʀ\n\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:                                           
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': msg._from}
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)
                                path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                                image = 'http://dl.profile.line.naver.jp'+path
                                cl.sendImageWithURL(msg.to, image)
                                
                        elif cmd == "gue":                       	
                    	    if msg._from in owner or msg._from in admin or msg._from in staff: 
                              contact = cl.getContact(sender)
                              image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                              cl.sendMessage(msg.to, "Nama : "+str(contact.displayName))
                              cl.sendMessage(msg.to, None,contentMetadata={'mid': sender}, contentType=13)
                                                                                                     
                        elif text.lower() == "midku":
                               cl.sendMessage(msg.to, msg._from)
                        elif text.lower() == 'ass':
                               cl.sendMessage(msg.to, "Assalamu'alaikum Wr. Wb")
                               cl.sendMessage(msg.to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                        elif text.lower() == 'wss':
                               cl.sendMessage(msg.to, "Wa'alaikumsallam.Wr,Wb")
                               cl.sendMessage(msg.to, "ُوَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")
                        elif text.lower() == 'bot':
                               cl.sendMessage(msg.to, "вoтѕ ѕιap ѕтay proтecт мaхιмal😡")

                        elif ("Get id " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Kepo " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                                                       
                        elif cmd == "addbot":
                          if msg._from in admin:
                            try:
                                cl.findAndAddContactsByMid(Amid)
                                cl.findAndAddContactsByMid(Bmid)
                                cl.findAndAddContactsByMid(Cmid)
                                cl.findAndAddContactsByMid(Dmid)
                                cl.findAndAddContactsByMid(Emid)
                                cl.findAndAddContactsByMid(Fmid) 
                                cl.findAndAddContactsByMid(Gmid)
                                cl.findAndAddContactsByMid(Hmid)
                                cl.findAndAddContactsByMid(Imid)
                                cl.findAndAddContactsByMid(Jmid)
                                cl.findAndAddContactsByMid(g1MID)
                                cl.findAndAddContactsByMid(g2MID)                                                          
                                k1.findAndAddContactsByMid(mid)                                                               
                                k1.findAndAddContactsByMid(Cmid)
                                k1.findAndAddContactsByMid(Dmid)
                                k1.findAndAddContactsByMid(Emid)
                                k1.findAndAddContactsByMid(Fmid)                                                              
                                k1.findAndAddContactsByMid(Gmid)
                                k1.findAndAddContactsByMid(Hmid)                                
                                k1.findAndAddContactsByMid(Imid)
                                k1.findAndAddContactsByMid(Jmid)
                                k1.findAndAddContactsByMid(g1MID)
                                k1.findAndAddContactsByMid(g2MID) 
                                k2.findAndAddContactsByMid(mid)                                                             
                                k2.findAndAddContactsByMid(Bmid)
                                k2.findAndAddContactsByMid(Dmid)
                                k2.findAndAddContactsByMid(Emid)
                                k2.findAndAddContactsByMid(Fmid)                                                              
                                k2.findAndAddContactsByMid(Gmid)
                                k2.findAndAddContactsByMid(Hmid)                                
                                k2.findAndAddContactsByMid(Imid)
                                k2.findAndAddContactsByMid(Jmid)
                                k2.findAndAddContactsByMid(g1MID)
                                k2.findAndAddContactsByMid(g2MID)
                                k3.findAndAddContactsByMid(mid)                                
                                k3.findAndAddContactsByMid(Bmid)                              
                                k3.findAndAddContactsByMid(Dmid)
                                k3.findAndAddContactsByMid(Emid)
                                k3.findAndAddContactsByMid(Fmid)                                                              
                                k3.findAndAddContactsByMid(Gmid)
                                k3.findAndAddContactsByMid(Hmid)                                
                                k3.findAndAddContactsByMid(Imid)
                                k3.findAndAddContactsByMid(Jmid)
                                k3.findAndAddContactsByMid(g1MID)
                                k3.findAndAddContactsByMid(g2MID) 
                                k4.findAndAddContactsByMid(mid)                                
                                k4.findAndAddContactsByMid(Bmid)
                                k4.findAndAddContactsByMid(Cmid)                                
                                k4.findAndAddContactsByMid(Emid)
                                k4.findAndAddContactsByMid(Fmid)                                                              
                                k4.findAndAddContactsByMid(Gmid)
                                k4.findAndAddContactsByMid(Hmid)                                
                                k4.findAndAddContactsByMid(Imid)
                                k4.findAndAddContactsByMid(Jmid)
                                k4.findAndAddContactsByMid(g1MID)
                                k4.findAndAddContactsByMid(g2MID) 
                                k5.findAndAddContactsByMid(mid)                                
                                k5.findAndAddContactsByMid(Bmid)
                                k5.findAndAddContactsByMid(Cmid)
                                k5.findAndAddContactsByMid(Dmid)                                
                                k5.findAndAddContactsByMid(Fmid)                                                              
                                k5.findAndAddContactsByMid(Gmid)
                                k5.findAndAddContactsByMid(Hmid)                                
                                k5.findAndAddContactsByMid(Imid)
                                k5.findAndAddContactsByMid(Jmid)
                                k5.findAndAddContactsByMid(g1MID)
                                k5.findAndAddContactsByMid(g2MID) 
                                k6.findAndAddContactsByMid(mid)                                
                                k6.findAndAddContactsByMid(Bmid)
                                k6.findAndAddContactsByMid(Cmid)
                                k6.findAndAddContactsByMid(Dmid)
                                k6.findAndAddContactsByMid(Emid)
                                k6.findAndAddContactsByMid(Fmid)                                                              
                                k6.findAndAddContactsByMid(Gmid)
                                k6.findAndAddContactsByMid(Hmid)                                
                                k6.findAndAddContactsByMid(Imid)
                                k6.findAndAddContactsByMid(Jmid)
                                k6.findAndAddContactsByMid(g1MID)
                                k6.findAndAddContactsByMid(g2MID)
                                k7.findAndAddContactsByMid(mid)                                
                                k7.findAndAddContactsByMid(Bmid)
                                k7.findAndAddContactsByMid(Cmid)
                                k7.findAndAddContactsByMid(Dmid)
                                k7.findAndAddContactsByMid(Emid)
                                k7.findAndAddContactsByMid(Fmid)                                                              
                                k7.findAndAddContactsByMid(Gmid)
                                k7.findAndAddContactsByMid(Hmid)                                
                                k7.findAndAddContactsByMid(Imid)
                                k7.findAndAddContactsByMid(Jmid)
                                k7.findAndAddContactsByMid(g1MID)
                                k7.findAndAddContactsByMid(g2MID) 
                                k8.findAndAddContactsByMid(mid)                                
                                k8.findAndAddContactsByMid(Bmid)
                                k8.findAndAddContactsByMid(Cmid)
                                k8.findAndAddContactsByMid(Dmid)
                                k8.findAndAddContactsByMid(Emid)
                                k8.findAndAddContactsByMid(Fmid)                                                              
                                k8.findAndAddContactsByMid(Gmid)
                                k8.findAndAddContactsByMid(Hmid)                                
                                k8.findAndAddContactsByMid(Imid)
                                k8.findAndAddContactsByMid(Jmid)
                                k8.findAndAddContactsByMid(g1MID)
                                k8.findAndAddContactsByMid(g2MID) 
                                k9.findAndAddContactsByMid(mid)                                
                                k9.findAndAddContactsByMid(Bmid)
                                k9.findAndAddContactsByMid(Cmid)
                                k9.findAndAddContactsByMid(Dmid)
                                k9.findAndAddContactsByMid(Emid)
                                k9.findAndAddContactsByMid(Fmid)                                                              
                                k9.findAndAddContactsByMid(Gmid)
                                k9.findAndAddContactsByMid(Hmid)                                
                                k9.findAndAddContactsByMid(Imid)
                                k9.findAndAddContactsByMid(Jmid)
                                k9.findAndAddContactsByMid(g1MID)
                                k9.findAndAddContactsByMid(g2MID) 
                                k10.findAndAddContactsByMid(mid)                                
                                k10.findAndAddContactsByMid(Bmid)
                                k10.findAndAddContactsByMid(Cmid)
                                k10.findAndAddContactsByMid(Dmid)
                                k10.findAndAddContactsByMid(Emid)
                                k10.findAndAddContactsByMid(Fmid)                                                              
                                k10.findAndAddContactsByMid(Gmid)
                                k10.findAndAddContactsByMid(Hmid)                                
                                k10.findAndAddContactsByMid(Imid)
                                k10.findAndAddContactsByMid(Jmid)
                                k10.findAndAddContactsByMid(g1MID)
                                k10.findAndAddContactsByMid(g2MID) 
                                g1.findAndAddContactsByMid(mid)                                
                                g1.findAndAddContactsByMid(Bmid)
                                g1.findAndAddContactsByMid(Cmid)
                                g1.findAndAddContactsByMid(Dmid)
                                g1.findAndAddContactsByMid(Emid)
                                g1.findAndAddContactsByMid(Fmid)                                                              
                                g1.findAndAddContactsByMid(Gmid)
                                g1.findAndAddContactsByMid(Hmid)                                
                                g1.findAndAddContactsByMid(Imid)
                                g1.findAndAddContactsByMid(Jmid)                                
                                g1.findAndAddContactsByMid(g2MID) 
                                g2.findAndAddContactsByMid(mid)                                
                                g2.findAndAddContactsByMid(Bmid)
                                g2.findAndAddContactsByMid(Cmid)
                                g2.findAndAddContactsByMid(Dmid)
                                g2.findAndAddContactsByMid(Emid)
                                g2.findAndAddContactsByMid(Fmid)                                                              
                                g2.findAndAddContactsByMid(Gmid)
                                g2.findAndAddContactsByMid(Hmid)                                
                                g2.findAndAddContactsByMid(Imid)
                                g2.findAndAddContactsByMid(Jmid)
                                g2.findAndAddContactsByMid(g1MID)
                                g2.findAndAddContactsByMid(g2MID)                                                               
                                cl.sendMessage(to,"Sucsess!!!")
                            except:
                                cl.sendMessage(to,"Sucess!! add all bots...")
                                
                        elif cmd  == "mybot":
                          if msg._from in admin:
                              cl.sendContact(to, mid)
                              cl.sendContact(to, Amid)
                              cl.sendContact(to, Bmid)
                              cl.sendContact(to, Cmid)
                              cl.sendContact(to, Dmid)
                              cl.sendContact(to, Emid)
                              cl.sendContact(to, Fmid)                                             
                              cl.sendContact(to, Gmid)
                              cl.sendContact(to, Hmid)
                              cl.sendContact(to, Imid)
                              cl.sendContact(to, Jmid)
                              cl.sendContact(to, g1MID)
                              cl.sendContact(to, g2MID)
                              
                        elif cmd  == "midbot":
                          if msg._from in admin:
                              cl.sendMessage(msg.to,mid)
                              k1.sendMessage(msg.to,Amid)
                              k2.sendMessage(msg.to,Bmid)
                              k3.sendMessage(msg.to,Cmid)                            
                              k4.sendMessage(msg.to,Dmid)
                              k5.sendMessage(msg.to,Emid)
                              k6.sendMessage(msg.to,Fmid)
                              k7.sendMessage(msg.to,Gmid)
                              k8.sendMessage(msg.to,Hmid)
                              k9.sendMessage(msg.to,Imid)   
                              k10.sendMessage(msg.to,Jmid)          

                        elif cmd == "speedbot" or cmd == "spbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(to, "Kecepatan Maksimal bot protect🏁")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k1.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k2.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k3.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k4.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k5.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k6.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k7.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k8.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start
                               k9.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                               elapsed_time = time.time() - start       
                               k10.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")      
                               
                        elif cmd == "#clearban" or text.lower() == '#hapusbl':
                          if wait["selfbot"] == True:
                            if msg._from in admin:                          	
                              wait["blacklist"] = {}            
                              ragets = cl.getContacts(wait["blacklist"])
                              cl.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"]))))                             
                              k1.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"])))) 
                              k2.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"])))) 
                              k3.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"])))) 
                              k4.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"])))) 
                              k5.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"])))) 
                              k6.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"])))) 
                              k7.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"])))) 
                              k8.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"])))) 
                              k9.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"])))) 
                              k9.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"])))) 
                              
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)                                      
                                  cl.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))                              
                              else:
                                  cl.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  
                        elif text.lower() == "hapuschat":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               try:
                                   cl.removeAllMessages(op.param2)                                  
                                   cl.sendMessage(msg.to,"Chat sudah d bersihkan 👍")                                  
                               except:
                                   pass

                        elif cmd.startswith("bcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"🔴Broadcast \n\n" + str(pesan))

                        elif text.lower() == "sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               cl.sendMessage(msg.to, "🔴 Sname \n\n" + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("setsname "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Succes change Sname")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "🔴Sname change \n\nSname succes change to {}".format(str(key).lower()))

                        elif text.lower() == "reset sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "Succes Reset Sname ")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               cl.sendMessage(msg.to, "please wait")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Done...")
                            
                        elif cmd == "time":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Active " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "Group Info\n\nNama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in owner or msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ɪɴғᴏ\n"
                                ret_ += "\nNama Group : {}".format(G.name)
                                ret_ += "\nID Group : {}".format(G.id)
                                ret_ += "\nPembuat : {}".format(gCreator)
                                ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nJumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nJumlah Pending : {}".format(gPending)
                                ret_ += "\nGroup Qr : {}".format(gQr)
                                ret_ += "\nGroup Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"Group Name : " + str(G.name) + " \n\nMember List \n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    cl.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Leave in groups " +str(ginfo.name))

                        elif cmd == "flist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"🔰ʟɪsᴛ ᴛᴇᴍᴀɴ🔰\n\n"+ma+"\ᴛᴏᴛᴀʟ"+str(len(gid))+"ᴛᴇᴍᴀɴ")

                        elif cmd == "glist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"🔰ɢʀᴜᴘʟɪsᴛ 🔰\n\n"+ma+"\nTotal"+str(len(gid))+" Groups")

                        elif cmd == "curl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "ourl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(x.name)+ "\nᴜʀʟ ɢʀᴜᴘ: : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE FROFILE============#
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"Send Picture") 
                       
                        elif cmd == "upbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendMessage(msg.to,"Send your images...")          
                                
                        elif cmd == "upfoto":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["SKfoto"][mid] = True
                                cl.sendMessage(msg.to,"Send picture")                                
                                             
                        elif cmd == "1up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Amid] = True
                                cl.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "2up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Bmid] = True
                                cl.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "3up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Cmid] = True
                                cl.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "4up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Dmid] = True
                                cl.sendMessage(msg.to,"Send picture")

                        elif cmd == "5up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Emid] = True
                                cl.sendMessage(msg.to,"Send picture")

                        elif cmd == "6up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Fmid] = True
                                cl.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "7up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Gmid] = True
                                cl.sendMessage(msg.to,"Send picture")
                        elif cmd == "8up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Hmid] = True
                                cl.sendMessage(msg.to,"Send picture")
                        elif cmd == "9up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Imid] = True
                                cl.sendMessage(msg.to,"Send picture")
                        elif cmd == "10up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Jmid] = True
                                cl.sendMessage(msg.to,"Send picture")
#================BOT UPDATE NAME============#
                        elif cmd.startswith("name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("name1: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("name2: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("name3: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("name4: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k4.getProfile()
                                profile.displayName = string
                                k4.updateProfile(profile)
                                k4.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("name5: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k5.getProfile()
                                profile.displayName = string
                                k5.updateProfile(profile)
                                k5.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("name6: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k6.getProfile()
                                profile.displayName = string
                                k6.updateProfile(profile)
                                k6.sendMessage(msg.to,"Nama diganti jadi " + string + "") 
                                
                        elif cmd.startswith("name7: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k7.getProfile()
                                profile.displayName = string
                                k7.updateProfile(profile)
                                k7.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("name8: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k8.getProfile()
                                profile.displayName = string
                                k8 .updateProfile(profile)
                                k8.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("name9: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k9.getProfile()
                                profile.displayName = string
                                k9.updateProfile(profile)
                                k9.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("name10: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k10.getProfile()
                                profile.displayName = string
                                k10.updateProfile(profile)
                                k10.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("name11: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = g1.getProfile()
                                profile.displayName = string
                                g1.updateProfile(profile)
                                g1.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("name12: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = g2.getProfile()
                                profile.displayName = string
                                g2.updateProfile(profile)
                                g2.sendMessage(msg.to,"Nama diganti jadi " + string + "")                    
#===========BOT UPDATE============#
                        elif cmd == "mention" or text.lower() == 'tes':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                        elif cmd == "botlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔰ʙᴏᴛʟɪsᴛ🔰\n\n\n"+ma+"\n%s ʙᴏᴛs" %(str(len(Bots))))
                   
                        elif cmd == "stafflist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔰ᴀᴅᴍɪɴʟɪsᴛ🔰\n\n🔰ᴏᴡɴᴇʀ\n"+ma+"\n🔰ᴀᴅᴍɪɴ\n"+mb+"\n🔰sᴛᴀғғ:\n"+mc+"\n%s 🔰ᴀᴅᴍɪɴʟɪsᴛ🔰" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "protectlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                mg = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0
                                g = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectantijs
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +cl.getGroup(group).name + "\n"
                                gid = ghost
                                for group in gid:
                                    g = g + 1
                                    end = '\n'
                                    mg += str(g) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"⛎ᴅᴀғᴛᴀʀ ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ Sɪʟᴇɴᴛᵏᶦˡˡᵉʳ⛎\n\n🔒ᴘʀᴏᴛᴇᴄᴛ ǫʀ:\n"+ma+"\n🔒ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ:\n"+mb+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴀɴᴛɪᴋɪᴄᴋᴇʀ:\n"+mc+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ:\n"+md+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ:\n"+me+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ:\n"+mf+"\n🔒ɢʜᴏsᴛ:\n"+mg+"\n\n⛎ᴘʀᴏᴛᴇᴄᴛ ʟɪsᴛ %s ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛ⛎" %(str(len(protectqr)+len(protectinvite)+len(protectantijs)+len(protectcancel)+len(protectkick)+len(protectjoin)+len(ghost))))
                                
                        elif cmd == "skname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                k1.sendMessage(msg.to,responsename1)
                                k2.sendMessage(msg.to,responsename2)
                                k3.sendMessage(msg.to,responsename3)
                                k4.sendMessage(msg.to,responsename4)
                                k5.sendMessage(msg.to,responsename5)
                                k6.sendMessage(msg.to,responsename6)
                                k7.sendMessage(msg.to,responsename7)
                                k8.sendMessage(msg.to,responsename8)
                                k9.sendMessage(msg.to,responsename9)
                                k10.sendMessage(msg.to,responsename10)
                                
                                             
                        elif cmd == "masuk":
                         if msg._from in admin:
                           if msg.toType == 2:
                               group = cl.getGroup(to)
                               group.preventedJoinByTicket = False
                               cl.updateGroup(group)
                               invsend = 0                        
                               ticket = cl.reissueGroupTicket(to)
                               k1.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k2.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k3.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k4.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k5.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k6.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k7.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k8.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k9.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               k10.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)                               
                        
                        elif cmd == "invitebot":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Gmid,Hmid,Imid,Jmid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    k1.acceptGroupInvitation(msg.to)
                                    k2.acceptGroupInvitation(msg.to)
                                    k3.acceptGroupInvitation(msg.to)
                                    k4.acceptGroupInvitation(msg.to)
                                    k5.acceptGroupInvitation(msg.to)
                                    k6.acceptGroupInvitation(msg.to)
                                    k7.acceptGroupInvitation(msg.to)
                                    k8.acceptGroupInvitation(msg.to)
                                    k9.acceptGroupInvitation(msg.to)
                                    k10.acceptGroupInvitation(msg.to)
                                except:
                                    pass       
                               
                        elif cmd == "name":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               k1.sendMessage(msg.to, "۞❂✪₷ιlΣNƬ ₭ιll₠₹ ⋮➲➤")
                               k2.sendMessage(msg.to, "۞❂✪₷ιlΣNƬ ₭ιll₠₹ ⋮➲➤")
                               k3.sendMessage(msg.to, "۞❂✪₷ιlΣNƬ ₭ιll₠₹ ⋮➲➤")
                               k4.sendMessage(msg.to, "۞❂✪₷ιlΣNƬ ₭ιll₠₹ ⋮➲➤")
                               k5.sendMessage(msg.to, "۞❂✪₷ιlΣNƬ ₭ιll₠₹ ⋮➲➤")
                               k6.sendMessage(msg.to, "۞❂✪₷ιlΣNƬ ₭ιll₠₹ ⋮➲➤")
                               k7.sendMessage(msg.to, "۞❂✪₷ιlΣNƬ ₭ιll₠₹ ⋮➲➤")
                               k8.sendMessage(msg.to, "۞❂✪₷ιlΣNƬ ₭ιll₠₹ ⋮➲➤")
                               k9.sendMessage(msg.to, "۞❂✪₷ιlΣNƬ ₭ιll₠₹ ⋮➲➤")
                               k10.sendMessage(msg.to, "۞❂✪₷ιlΣNƬ ₭ιll₠₹ ⋮➲➤")
                                                       
                        elif cmd == "bye1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k1.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                k1.leaveGroup(msg.to)
                                
                        elif cmd == "bye2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k2.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                k2.leaveGroup(msg.to)
                                
                        elif cmd == "bye3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k3.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                k3.leaveGroup(msg.to)
                                
                        elif cmd == "bye4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k4.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                k4.leaveGroup(msg.to)
                                
                        elif cmd == "bye5":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k5.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                k5.leaveGroup(msg.to)
                                
                        elif cmd == "bye6":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k6.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                k6.leaveGroup(msg.to)
                                
                        elif cmd == "bye7":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k7.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                k7.leaveGroup(msg.to)
                                
                        elif cmd == "bye8":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k8.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                k8.leaveGroup(msg.to)   
                                
                        elif cmd == "bye9":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k9.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                k9.leaveGroup(msg.to)
                                
                        elif cmd == "bye10":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k10.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                k10.leaveGroup(msg.to)
                                                                                                             
                        elif cmd == "ghost in":
                          if msg._from in admin:
                           if msg.toType == 2:
                               group = cl.getGroup(to)
                               group.preventedJoinByTicket = False
                               cl.updateGroup(group)
                               invsend = 0
                               ticket = cl.reissueGroupTicket(to)
                               g1.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               g2.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               
                        elif cmd == "ghost lv":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                g1.sendMessage(msg.to, "Kicker Out  In "+str(G.name))
                                g1.leaveGroup(msg.to)
                                g2.leaveGroup(msg.to)
                                
                        elif cmd == ".bye":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "Makasih sudah invit\nketemu lain waktu... "+str(G.name))
                                cl.leaveGroup(msg.to)
                                
                        elif cmd == "pulang":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                               k1.leaveGroup(msg.to)
                               k2.leaveGroup(msg.to)
                               k3.leaveGroup(msg.to)
                               k4.leaveGroup(msg.to)
                               k5.leaveGroup(msg.to)
                               k6.leaveGroup(msg.to)
                               k7.leaveGroup(msg.to)
                               k8.leaveGroup(msg.to)
                               k9.leaveGroup(msg.to)
                               k10.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin or msg._from in owner:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        cl.sendMessage(i, " Silahkan invite Oner kami")
                                        cl.leaveGroup(i)
                                        cl.sendMessage(to,"Succes leave group " +h)
                                        
                        elif cmd.startswith("skpulang "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    k1.sendMessage(group,"sory tbp otw dulu\n\nketemu lain waktu ya\nsilahkan invite owner kami")
                                    k1.leaveGroup(group)
                                    k2.leaveGroup(group)
                                    k3.leaveGroup(group)
                                    k4.leaveGroup(group)
                                    k6.leaveGroup(group)
                                    k7.leaveGroup(group)
                                    k8.leaveGroup(group)
                                    k9.leaveGroup(group)
                                    k10.leaveGroup(group)
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = ' Sukses Leave Group \n Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    cl.sendMessage(msg.to, "")
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += " Nama grup : {}".format(G.name)
                                ret_ += "\n Pendingan : {}".format(gPending)
                                ret_ += "\n Jumlah Member : {}".format(str(len(G.members)))
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as e:
                                cl.sendMessage(to, str(e))         
                                        
                        elif cmd == "silent1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [g1MID])
                                    cl.sendMessage(msg.to,"Succes invite di"+str(ginfo.name)+" Siap Stay")
                                except:
                                    pass
                        elif cmd == "silent2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [g2MID])
                                    cl.sendMessage(msg.to,"Succes invite di"+str(ginfo.name)+" Siap Stay")
                                except:
                                    pass
#====================================================================                            
                        elif cmd == "timerespon":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "тιмe reѕpon\n\n geт proғιle\n   %.10f\n geт conтacт\n   %.10f\n geт groυp\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               start = time.time()                               
                               cl.sendMessage(msg.to, "proтecт ѕpeed....")                               
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "waĸтυ:\n{}".format(str(elapsed_time)))
                               
                        elif cmd == "lurk:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['SKreadPoint'][msg.to] = msg_id
                                 Setmain['SKreadMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurk:off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['SKreadPoint'][msg.to]
                                 del Setmain['SKreadMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['SKreadPoint']:
                                if Setmain['SKreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['SKreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['SKreadPoint'][msg.to]
                                        del Setmain['SKreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['SKreadPoint'][msg.to] = msg.id
                                    Setmain['SKreadMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========add img============# 
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"ҡıяıṃ ɢѧṃṃɞѧя ȗṅṭȗҡ ṃєṅɢɢѧṅṭı ɢяȗק...")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendMessage(msg.to,"ҡıяıṃ ғȏṭȏ ȗṅṭȗҡ ṃєṅɢɢѧṅṭı ɞȏṭś.....")
                                              
                        elif cmd == "changedual":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["ChangeVideoProfilevid"][msg._from] = True
                                cl.sendMessage(msg.to,"ҡıяıṃ ṿıԀєȏ ṅʏѧ...")
                                
                        elif cmd.startswith("changedualurl: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ","")                            
                                cl.downloadFileURL(url,'path','video.mp4')
                                settings["ChangeVideoProfilePicture"][msg._from] = True
                                cl.sendMessage(msg.to, "ҡıяıṃ ғȏṭȏṅʏѧ.....")
                                
                     
#==============add video==========================================================================
                        elif cmd.startswith("addimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                wait["Addimage"]["status"] = True
                                wait["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Silahkan kirim fotonya...") 
                            else:
                                cl.sendMessage(msg.to, "Foto itu sudah dalam list") 
                                
                        elif cmd.startswith("dellimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                cl.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Berhasil menghapus {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "Foto itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listimage":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Image 」\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\nTotal「{}」Images".format(str(len(images)))
                             cl.sendMessage(to, ret_)
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addvideo "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in videos:
                                wait["Addvideo"]["status"] = True
                                wait["Addvideo"]["name"] = str(name.lower())
                                videos[str(name.lower())] = ""
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim videonya...") 
                            else:
                                cl.sendMessage(msg.to, "Video itu sudah dalam list") 
                                
                        elif cmd.startswith("dellvideo "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in videos:
                                cl.deleteFile(videos[str(name.lower())])
                                del videos[str(name.lower())]
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Berhasil menghapus video {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "Video itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listvideo":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Video 」\n\n"
                             for video in videos:
                                 no += 1
                                 ret_ += str(no) + ". " + video.title() + "\n"
                             ret_ += "\nTotal「{}」Videos".format(str(len(videos)))
                             cl.sendMessage(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play video nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addmp3 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in audios:
                                wait["Addaudio"]["status"] = True
                                wait["Addaudio"]["name"] = str(name.lower())
                                audios[str(name.lower())] = ""
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Silahkan kirim mp3 nya...") 
                            else:
                                cl.sendMessage(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in audios:
                                cl.deleteFile(audios[str(name.lower())])
                                del audios[str(name.lower())]
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "listmp3":
                             no = 0
                             ret_ = "「 Daftar Lagu 」\n\n"
                             for audio in audios:
                                 no += 1
                                 ret_ += str(no) + ". " + audio.title() + "\n"
                             ret_ += "\nTotal「{}」Lagu".format(str(len(audios)))
                             cl.sendMessage(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play mp3 nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Sticker ] ============#                                            
                        elif cmd.startswith("addsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                wait["Addsticker"]["status"] = True
                                wait["Addsticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessaget(msg.to, "Silahkan kirim stickernya...") 
                            else:
                                cl.sendMessaget(msg.to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "Sticker itu tidak ada dalam list") 
                                 
                        elif text.lower() == "liststicker":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Sticker 」\n\n"
                             for sticker in stickers:
                                 no += 1
                                 ret_ += str(no) + ". " + sticker.title() + "\n"
                             ret_ += "\nTotal「{}」Stickers".format(str(len(stickers)))
                             cl.sendMessage(to, ret_) 
#=========== [ Add Audio] ============#
#====================================================================                                                       
                        elif cmd.startswith("indo:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=in&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)

                        elif cmd.startswith("korea:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ko&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("jp:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ja&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                                
                        elif cmd.startswith("thai:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=th&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("arab:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ar&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)  
                        elif cmd.startswith("jawa:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=jw&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                     
                        elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).mid
                                    s = cl.getContact(u).displayName
                                    hasil = cl.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        cl.likePost(str(sender), str(result), likeType=random.choice(typel))
                                        cl.createComment(str(sender), str(result), 'Auto Like by dhenza')
                                    cl.sendMessage(msg.to, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    cl.sendMessage(receiver, str(e))
                                                                               
                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                cl.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                cl.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                cl.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass                                                         
                            
                        elif msg.text.lower().startswith("smule: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            channel = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0"
                                r = web.get("https://citldesign.herokuapp.com/downloadsmule={}".format(urllib.parse.quote(channel)))
                                data = r.text
                                data = json.loads(data)
                                for design in data["result"]:
                                    image = design["image"]
                                    url = design["url"]
                                cl.sendImageWithURL(msg.to, image)
                                cl.sendAudioWithURL(msg.to, url)
                                cl.sendVideoWithURL(msg.to, url)
                                
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                cl.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                cl.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                cl.sendMessage(msg.to, str(njer))
                                                                                                      
                        
                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"Informasiâ¢\n\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak)

                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "Clone Profile \nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    cl.sendMessage(msg.to, "Gagal clone profile")
                            
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  lineProfile.displayName = str(myProfile["displayName"])
                                  lineProfile.statusMessage = str(myProfile["statusMessage"])
                                  lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                  cl.updateProfile(lineProfile)
                                  sendMention(msg.to, sender, "Restore Profile \nNama ", " \nBerhasil restore profile")
                              except:
                                  cl.sendMessage(msg.to, "Gagal restore profile")

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Spamtag change to " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                sendMention1(msg)
                                            except Exception as e:
                                                sendMention1(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")                        
                                                                
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(msg.to,"Jumlah melebihi batas")
                                                        
                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                          elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectqr ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)

                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)
                                    
                        elif 'Js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Protect Antikicker sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Anti Kicker 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect Anti Kicker sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Antikicker 」\n" + msgs)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Hantu sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Hantu  」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Hantu sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Hantu 」\n" + msgs)
                                    
                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in ghost:
                                      msgs = ""
                                  else:
                                      ghost.append(msg.to)
                                  if msg.to in protectantijs:
                                      msgs = ""
                                  else:
                                      protectantijs.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protecttion sudah diaktifkan"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protection diaktifkan"
                                  cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection sudah dimatikan"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)       
#===========KICKOUT============#       
                        elif ("Kicker " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Vc " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           g1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           g2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           g1.kickoutFromGroup(msg.to, [target])
                                           g2.kickoutFromGroup(msg.to, [target])
                                           g1.leaveGroup(msg.to)
                                           g2.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass
                                           
                        elif ("Bubar" in msg.text):
                            if msg._from in admin:
                             if msg.toType == 2:
                                 print ("[ 19 ] KICK ALL MEMBER")
                                 _name = msg.text.replace("Bubar","")                                 
                                 gs = k1.getGroup(msg.to)
                                 gs = k2.getGroup(msg.to)
                                 gs = k3.getGroup(msg.to)
                                 gs = k4.getGroup(msg.to)
                                 gs = k5.getGroup(msg.to)
                                 gs = k6.getGroup(msg.to)
                                 gs = k7.getGroup(msg.to)
                                 gs = k8.getGroup(msg.to)
                                 gs = k9.getGroup(msg.to)
                                 gs = k10.getGroup(msg.to)
                                 cl.sendMessage(msg.to,"「 Papay Sayang 😚😚😚」")
                                 cl.sendMessage(msg.to,"「 Sorry r̸o̸o̸m̸ n̸y̸a̸ k̸a̸m̸i̸ s̸i̸t̸a̸ s̸e̸e̸ y̸o̸u̸ s̸l̸a̸m̸ d̸a̸r̸i̸ TΣΔM SILΣΠT βΩT」")
                                 targets = []
                                 for g in gs.members:
                                     if _name in g.displayName:
                                         targets.append(g.mid)
                                 if targets == []:
                                     cl.sendMessage(msg.to,"ʙᴏᴛs ʟɪᴍɪᴛ")
                                 else:
                                     for target in targets:
                                       if not target in Bots:
                                          if not target in admin:
                                             if not target in staff:
                                               try:
                                                   dhenza= [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10]
                                                   kicker=random.choice(dhenza)
                                                   kicker.kickoutFromGroup(msg.to,[target])
                                                   print (msg.to,[g.mid])
                                               except Exception as error:
                                                   cl.sendMessage(msg.to, str(error))

                        elif text.lower() == 'silentkiller':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                           	if msg.toType == 2:
                                  ginfo = cl.getGroup(msg.to)
                                  cl.sendMessage(msg.to, "Proses Cleanse....")
                                  cl.sendMessage(msg.to, "silentkiller \nmember : " +str(len(ginfo.members)) + " \nFuck you...")
                                  G = cl.getGroup(msg.to)
                                  G.preventedJoinByTicket = False
                                  cl.updateGroup(G)
                                  Ticket = cl.reissueGroupTicket(msg.to)
                                  k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  g1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  g2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  _name = text.lower().replace('silentkiller','')
                                  gs = k1.getGroup(msg.to)
                                  gs = k2.getGroup(msg.to)
                                  gs = k3.getGroup(msg.to)
                                  gs = k4.getGroup(msg.to)
                                  gs = k5.getGroup(msg.to)
                                  gs = k6.getGroup(msg.to)
                                  gs = k7.getGroup(msg.to)
                                  gs = k8.getGroup(msg.to)
                                  gs = k9.getGroup(msg.to)
                                  gs = k10.getGroup(msg.to)
                                  gs = g1.getGroup(msg.to)
                                  gs = g2.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                  	if _name in g.displayName:
                                  	   targets.append(g.mid)
                                  if targets == []:
                                  	cl.sendMessage(msg.to, "ʙᴏᴛs ʟɪᴍɪᴛᴇ")
                                  else:
                                       for target in targets:
                                        if not target in Bots:
                                           if not target in admin:
                                              if not target in staff:
                                                 try:
                                                      random.choice(ABC).kickoutFromGroup(msg.to,[target])
                                                      G = cl.getGroup(msg.to)
                                                      G.preventedJoinByTicket = True
                                                      cl.updateGroup(G)
                                                      G.preventedJoinByTicket(G)
                                                      cl.updateGroup(G)
                                                 except:
                                                      pass
                                                      
                        elif text.lower() == 'killban':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              gid = cl.getGroupIdsJoined()
                              group = cl.getGroup(to)
                              gMembMids = [contact.mid for contact in group.members]
                              ban_list = []
                              for tag in wait["blacklist"]:
                                    ban_list += filter(lambda str: str == tag, gMembMids)
                              if ban_list == []:
                                    cl.sendMessage(to, "ʙᴏᴛs ʟɪᴍɪᴛ ")
                                    return
                              else:
                                    for i in gid:
                                    	for jj in ban_list:
                                         if jj in admin:
                                                pass
                                         elif jj in staff:
                                                pass
                                         elif jj in Bots:
                                                pass
                                         else:
                                                cl.kickoutFromGroup(i, [jj])
                                                
                        elif "Mainkan " in msg.text:
                           if msg._from in admin:
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]                                                                                                                                
                              targets = []
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:                                                                                                                                       
                                  try:
                                      cl.kickoutFromGroup(msg.to,[target])
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                  except:
                                      pass
                                      
                        elif "Invite " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass 
                                       
                        elif cmd == "gas":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ASSALAMUALAIKUM \nHALLOOO!!! SORRY ROOM KALIAN \n\nKEBANYAKAN ANU\nSILENT DATANG\nMAU SAPU ROOM GJ\nNO COMEND \nNO BAPER \nNO BACOT \nNO DESAH \nNO SPONSOR \nNO HATTERS\nROOM OKEP \nROOM JUDI\nROOM GAJELAS\SIAP KAMI BANTAII \n\n\n\n FUCK YOU...\nKENAPE LU PADA DIEM\nTANGKIS SU JANGAN CUMA NYIMAK\n\n\nDASAR ROOM PEA KAGAK JELAS\nSORRY BOS!!!\nGC LU MAU GUA SITA...!!!\n\n\n SALAM DARI KAMI SÌ´ÌÍÍÌÍÍÍÍÌ¬Ì¦IÌ´Ì¾ÍÌÌÍÍÌÌÌÍÍÍÌÍÌÌ²ÍÌ®ÍÌ¡LÌ´ÌÌ¯ÌÍÌ£ÍEÌµÍÌ°Ì»NÌ·ÌÌÌÌÌÌÍÍÌÌ®Ì¡Ì¤Ì©ÌÌ®TÌµÌÌªÌ­ÍÌÌ³ Ì¸ÍÌÌÌÌ²ÌªÌ±ÍKÌ¶ÍÍÌÌÍÌÌ¨ÌÌ¥IÌ¸ÌÍÌ¿ÍÌºÍÍÌ¹ÌÌ§LÌ¶ÍÌÍÌÌÌ«Ì§Ì¤Ì§Ì¨ÍÌLÌµÌÌ½ÍÍÌÍÌÌ¤ÍÌÌ³EÌ¸ÍÌ¡ÍÌÌ Ì¦RÌµÌÌÍÌÍÌÌÍÌ¬Ì¯ÌÍÌÌªÌ³ÌÌ\n\nHADIR DI ROOM ANDA\n\nRATA GAK RATA YANG PENTING KIBAR \nRATA KAMI SENANG\nGAKRATA TUNGGU KEDATANGAN KAMI LAGI\n\n\n  <<<SLAM CIAK SÌ´ÌÍÍÌÍÍÍÍÌ¬Ì¦IÌ´Ì¾ÍÌÌÍÍÌÌÌÍÍÍÌÍÌÌ²ÍÌ®ÍÌ¡LÌ´ÌÌ¯ÌÍÌ£ÍEÌµÍÌ°Ì»NÌ·ÌÌÌÌÌÌÍÍÌÌ®Ì¡Ì¤Ì©ÌÌ®TÌµÌÌªÌ­ÍÌÌ³ Ì¸ÍÌÌÌÌ²ÌªÌ±ÍKÌ¶ÍÍÌÌÍÌÌ¨ÌÌ¥IÌ¸ÌÍÌ¿ÍÌºÍÍÌ¹ÌÌ§LÌ¶ÍÌÍÌÌÌ«Ì§Ì¤Ì§Ì¨ÍÌLÌµÌÌ½ÍÍÌÍÌÌ¤ÍÌÌ³EÌ¸ÍÌ¡ÍÌÌ Ì¦RÌµÌÌÍÌÍÌÌÍÌ¬Ì¯ÌÍÌÌªÌ³ÌÌ>>> \n\n\n>>>>>>GO!!! <<<<<<\n\n\nCREATOR\n\n<<<<<<<<<<SÌ´ÌÍÍÌÍÍÍÍÌ¬Ì¦IÌ´Ì¾ÍÌÌÍÍÌÌÌÍÍÍÌÍÌÌ²ÍÌ®ÍÌ¡LÌ´ÌÌ¯ÌÍÌ£ÍEÌµÍÌ°Ì»NÌ·ÌÌÌÌÌÌÍÍÌÌ®Ì¡Ì¤Ì©ÌÌ®TÌµÌÌªÌ­ÍÌÌ³ Ì¸ÍÌÌÌÌ²ÌªÌ±ÍKÌ¶ÍÍÌÌÍÌÌ¨ÌÌ¥IÌ¸ÌÍÌ¿ÍÌºÍÍÌ¹ÌÌ§LÌ¶ÍÌÍÌÌÌ«Ì§Ì¤Ì§Ì¨ÍÌLÌµÌÌ½ÍÍÌÍÌÌ¤ÍÌÌ³EÌ¸ÍÌ¡ÍÌÌ Ì¦RÌµÌÌÍÌÍÌÌÍÌ¬Ì¯ÌÍÌÌªÌ³ÌÌ>>>>>>>>>>\n\nhttp://line.me/ti/p/~pxj5094s\nhttp://line.me/ti/p/~dhenz415")
                               cl.sendContact(to, mid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)                          
                               cl.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                               cl.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
#===========ADMIN ADD============
                        elif ("Staff " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴛᴀғғ")
                                       except:
                                           pass

                        elif ("Bot " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ʙᴏᴛ")
                                       except:
                                           pass

                        elif ("Admin " in msg.text):
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs sᴛᴀғғ")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs ʙᴏᴛs")
                                       except:
                                           pass
#====================================#                                         
                        
#====================================#
                        elif cmd == "admin on" or text.lower() == 'admin:on':
                            if msg._from in owner:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"Send Contact")

                        elif cmd == "admindell" or text.lower() == 'adminexpl:on':
                            if msg._from in owner:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "staff on" or text.lower() == 'staff:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "staffdell" or text.lower() == 'staffexpl:on':
                            if msg._from in owner or msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "bot on" or text.lower() == 'bot:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "botdell" or text.lower() == 'botexpl:on':
                            if msg._from in owner:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "fresh" or text.lower() == 'refresh':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to,"Loading...")
                                cl.sendMessage(msg.to,"Refresh done...")

                        elif cmd == "admin" or text.lower() == 'contact admin':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "staff" or text.lower() == 'contact staff':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)                                            
#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = True
                                cl.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["MentionKick"] = False
                                cl.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = True
                                cl.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = False
                                cl.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"Auto Join Ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"Auto join Ticket dinonaktifkan")
                                
                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if settings["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["unsendMessage"] = True
                                cl.sendMessage(msg.to,"detect unsend diaktifkan")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if settings["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["unsendMessage"] = False
                                cl.sendMessage(msg.to,"detect unsend dinonaktifkan")
             
                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                cl.sendMessage(msg.to,"detect timeline on")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                cl.sendMessage(msg.to,"detect timleline off ")
#===========COMMAND BLACKLIST============#
                        elif cmd == "banall":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                         if target not in wait["selfbot"] or target not in Bots:
                                            try:
                                                wait["blacklist"][target] = True
                                                cl.sendMessage(msg.to,"Anda ternoda")
                                            except:
                                                pass
                                                
                        elif cmd == "bandell":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"Limit bosku")
                                else:
                                    for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                cl.sendMessage(msg.to,"Sucsess clear banned")
                                            except:
                                                pass
                        elif ("talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("takbandell " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "talbandell" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif ("ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("bandell " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "bandell" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Nothing blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"Blacklist\n\n"+ma+"\n %s User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to," Talkban User\n\n"+ma+"\nTotal%sTalkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "bl" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                                        
                        elif cmd == "clearban" or text.lower() == 'cbl':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                              cl.sendMessage(msg.to,"Succes Bersihkan {} Daftar Blacklist".format(str(len(wait["blacklist"]))))
                              wait["blacklist"] = {}
                              
                        elif text.lower() == rname["rname"]+" bl" or text.lower() == sname["sname"]+" bl":
                          if wait["selfbot"] == True:
                            if sender in admin:
                              if bl['blacklist'] == {}:
                                cl.sendMessage(msg.to,"Nothing blacklist")
                              else:
                                num = 0
                                mc = []
                                for m_id in bl['blacklist']:
                                    mc.append(m_id)
                                cban = cl.getContacts(mc)
                                nban = []
                                for x in range(len(cban)):
                                    nban.append("%i - "%num+cban[x].displayName)
                                    num = (num+1)
                                bn = "\n".join(str(i)for i in nban)
                                cl.sendMessage(msg.to, "User Blacklist: \n\n" + bn + "\n")
                                print ("Cek blacklist")

                        elif text.lower() == rname["rname"]+" dbn" or text.lower() == sname["sname"]+" dbn":
                          if wait["selfbot"] == True:
                            if sender in admin:
                              cl.sendMessage(msg.to,"{} blacklist cleared.".format(str(len(bl['blacklist']))))
                              bl['blacklist'] = {}
                              with open('bl.json', 'w') as fp:
                                  json.dump(bl, fp, sort_keys=True, indent=4)
                        
                        elif text.lower() == 'dz':
                               cl.sendMessage(msg.to, " Selfbot Protect Premium")
                               cl.sendMessage(msg.to, " My Owner: line.me/ti/p/~teambotprotect")
#===========COMMAND SET============#
                        elif msg.contentType == 16:
                           if wait["Timeline"] == True:
                              msg.contentType = 0
                              msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                              random.choice(ABC).sendMessage(msg.to, "like done")
                              
                        elif 'Spesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Spesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Swelcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Swelcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Srespon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Srespon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Sspam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Sspam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["SKmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Ssider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ssider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cpesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cwelcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "crespon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cspam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "csider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
                        
                        elif cmd == "batre":
                            if msg._from in admin or msg._from in owner:
                               try:cl.inviteIntoGroup(to, [mid]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, [mid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               cl.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k1.inviteIntoGroup(to, [Amid]);has = "OK"
                               except:has = "NOT"
                               try:k1.kickoutFromGroup(to, [Amid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k1.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:k2.inviteIntoGroup(to, [Bmid]);has = "OK"
                               except:has = "NOT"
                               try:k2.kickoutFromGroup(to, [Bmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k2.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k3.inviteIntoGroup(to, [Cmid]);has = "OK"
                               except:has = "NOT"
                               try:k3.kickoutFromGroup(to, [Cmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               k3.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:k4.inviteIntoGroup(to, [Dmid]);has = "OK"
                               except:has = "NOT"
                               try:k4.kickoutFromGroup(to, [Dmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k4.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                              
                               try:k5.inviteIntoGroup(to, [Emid]);has = "OK"
                               except:has = "NOT"
                               try:k5.kickoutFromGroup(to, [Emid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k5.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k6.inviteIntoGroup(to, [Fmid]);has = "OK"
                               except:has = "NOT"
                               try:k6.kickoutFromGroup(to, [Fmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k6.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil)) 
                               try:k7.inviteIntoGroup(to, [Gmid]);has = "OK"
                               except:has = "NOT"
                               try:k7.kickoutFromGroup(to, [Gmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k7.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:k8.inviteIntoGroup(to, [Hmid]);has = "OK"
                               except:has = "NOT"
                               try:k8.kickoutFromGroup(to, [Hmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               k8.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:k9.inviteIntoGroup(to, [Imid]);has = "OK"
                               except:has = "NOT"
                               try:k9.kickoutFromGroup(to, [Imid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k9.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                              
                               try:k10.inviteIntoGroup(to, [Jmid]);has = "OK"
                               except:has = "NOT"
                               try:k10.kickoutFromGroup(to, [Jmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               k10.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                                                    
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Pᴀsᴜᴋᴀɴ Sɪʟᴇɴᴛᴷᶦˡˡᵉʳ ɢᴏ : %s" % str(group.name))
                                     group1 = cl.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k1.findGroupByTicket(ticket_id)
                                     k1.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k1.sendMessage(msg.to, "Asɪsᴛ 1 ɢᴏ : %s" % str(group.name))
                                     groupl = k1.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k2.findGroupByTicket(ticket_id)
                                     k2.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k2.sendMessage(msg.to, "Asɪsᴛ 2 ɢᴏ : %s" % str(group.name))
                                     groupl = k2.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k3.findGroupByTicket(ticket_id)
                                     k3.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k3.sendMessage(msg.to, "Asɪsᴛ 3 ɢᴏ : %s" % str(group.name))
                                     groupl = k3.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k4.findGroupByTicket(ticket_id)
                                     k4.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k4.sendMessage(msg.to, "Asɪsᴛ 4 ɢᴏ : %s" % str(group.name))
                                     groupl = k4.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k5.findGroupByTicket(ticket_id)
                                     k5.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k5.sendMessage(msg.to, "Asɪsᴛ 5 ɢᴏ : %s" % str(group.name))
                                     groupl = k5.findGroupByTicket(ticket_id)
                                 for ticket_id in n_links:
                                     group = k6.findGroupByTicket(ticket_id)
                                     k6.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k6.sendMessage(msg.to, "Asɪsᴛ 6 ɢᴏ : %s" % str(group.name))
                                     groupl = k6.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k7.findGroupByTicket(ticket_id)
                                     k7.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k7.sendMessage(msg.to, "Asɪsᴛ 7 ɢᴏ : %s" % str(group.name))
                                     groupl = k7.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k8.findGroupByTicket(ticket_id)
                                     k8.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k8.sendMessage(msg.to, "Asɪsᴛ 8 ɢᴏ : %s" % str(group.name))
                                     groupl = k8.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k9.findGroupByTicket(ticket_id)
                                     k9.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k9.sendMessage(msg.to, "Asɪsᴛ 9 ɢᴏ : %s" % str(group.name))
                                     groupl = k9.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k10.findGroupByTicket(ticket_id)
                                     k10.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k10.sendMessage(msg.to, "Asɪsᴛ 10 ɢᴏ : %s" % str(group.name))
                                     groupl = k10.findGroupByTicket(ticket_id)
                                     
    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
