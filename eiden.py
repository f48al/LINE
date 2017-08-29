# -*- coding: utf-8 -*-
import LineAlpha
from LineAlpha.Gen.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

cl = LineAlpha.LINE()
cl.login(qr=True)
cl.loginResult()

kk = LineAlpha.LINE()
kk.login(qr=True)
kk.loginResult()

ki = LineAlpha.LINE()
ki.login(qr=True)
ki.loginResult()

kc = LineAlpha.LINE()
kc.login(qr=True)
kc.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""Loli
[Id] - Show Group ID
[Mid] - Show MyID
[Me] - Show My Contact
[Yid] - Show your ID
[Join on/off] - Auto join group
[Leave on/off] - Allows the bot to leave the group

[*] Command in the groups [*]
[Ginfo] - Group Info
[Banlist] - Check Banlist

[*] Admin Commands [*]
[Glink on/off] - Invitation link for group
[Invite：「mid」] - Invite by ID
[Kick：「mid」] - Kick by ID
[Cancel] - Cancel Group invite
[Gn 「group name」] - Change Group Name
[Bye all] - Bot Leave
[Ban 「@」] - Ban By Tag
[Unban 「@」] - Unban By Tag
[Ban] - By Sharing Contact
[Unban] - By Sharing Contact
[Kill ban] - Kick all banned contact(s)
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid]
admin=["u20377b4500a8f852f3fe1b2ac1af99ee"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"[Ardh-]BOT1",
    "cName2":"[Ardh-]BOT2",
    "cName3":"[Ardh-]BOT3",
    "cName4":"[Ardh-]BOT4",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

cancelinvite = {
    'autoCancel':True,
    'autoCancelUrl':True
}

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                GG = kk.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(GG.members) <= wait["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(GG.members) <= wait["autoCancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kk.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                GGG = ki.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(GGG.members) <= wait["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(GGG.members) <= wait["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                GGGG = kc.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(GGGG.members) <= wait["autoCancel"]["members"]:
                            kc.rejectGroupInvitation(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(GGGG.members) <= wait["autoCancel"]["members"]:
                        kc.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kc.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                return
            elif msg.text in ["/Key","/help","/Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Kick ","")
                    cl.sendText(msg.to,"Good bye.")
                    cl.kickoutFromGroup(msg.to,[midd])
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        X = cl.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = [contact.mid for contact in X.invitee]
                            cl.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"No one is inviting")
                            else:
                                cl.sendText(msg.to,"Sorry, nobody absent")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Glink off","Link off"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned off")
                        else:
                            cl.sendText(msg.to,"Already turned off")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")

                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Glink on","Link on"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned on")
                        else:
                            cl.sendText(msg.to,"Already turned on")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")

                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                    else:
                        cl.sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Yid" == msg.text:
                isi = msg.from_
                cl.sendText(msg.to,isi)
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Join on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already on")
                    else:
                        cl.sendText(msg.to,"Auto join already on")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned on")
                    else:
                        cl.sendText(msg.to,"Auto join turned on")
            elif msg.text in ["Join off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already off")
                    else:
                        cl.sendText(msg.to,"Auto join already off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned off")
                    else:
                        cl.sendText(msg.to,"Auto join turned off")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        x = cl.getGroup(msg.to)
                        if x.preventJoinByTicket == True:
                            x.preventJoinByTicket = False
                            cl.updateGroup(x)
                        gurl = cl.reissueGroupTicket(msg.to)
                        cl.sendText(msg.to,"line://ti/g/" + gurl)
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text == "$set":
                    cl.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "$read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------

#-----------------------------------------------

            elif msg.text in ["All join"]:
                if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    print "kicker ok"
                    G.preventJoinByTicket(G)
                    ki.updateGroup(G)
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
#-----------------------------------------------
            elif msg.text in ["Bye all"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                            kk.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            cl.leaveGroup(msg.to)
                        except:
                            pass
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
#-----------------------------------------------
            elif "Cleanse" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "Cleansing"
                        _name = msg.text.replace("Cleanse","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        kk.sendText(msg.to,"Group cleansing begin")
                        kc.sendText(msg.to,"Goodbye :)")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        targets.remove("u20377b4500a8f852f3fe1b2ac1af99ee")
                        targets.remove("u4299ed31ab6b56f3a16b9fb37b5fe84d")
                        targets.remove("u7e8f0bef929262a88e864c551ad4a621")
                        targets.remove("u47a353d40d8d1e753fecc19894ed8264")
                        targets.remove("uc514e40341b19cfbd0d51571b50f7807")
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    klist=[ki,kk,kc,cl]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Group cleansed")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif "Ban @" in msg.text:
                    if msg.toType == 2:
                        if msg.from_ in admin:
                            print "[Ban]ok"
                            _name = msg.text.replace("Ban @","")
                            _nametarget = _name.rstrip('  ')
                            gs = ki.getGroup(msg.to)
                            gs = kk.getGroup(msg.to)
                            gs = kc.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendText(msg.to,"Contact not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Added to Blacklist")
                                    except:
                                        ki.sendText(msg.to,"Error")
                        else:
                            cl.sendText(msg.to,"Command denied.")
                            cl.sendText(msg.to,"Admin permission required.")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Unban]ok"
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Added to Whitelist")
                                except:
                                    ki.sendText(msg.to,"Added to Whitelist")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")

#-----------------------------------------------
            elif "Bc " in msg.text:
                if msg.from_ in admin:
                    bctxt = msg.text.replace("Bc ","")
                    ki.sendText(msg.to,(bctxt))
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                if msg.from_ in admin:
                    start = time.time()
                    cl.sendText(msg.to, "Progress...")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["abcded"]:
                    cl.sendText(msg.to,msg.to)
                    msg.to = msg.from_
                    cl.sendText(msg.to,msg.to)
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Ban")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Unban")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No user is Blacklisted")
                else:
                    cl.sendText(msg.to,"Blacklisted user(s)")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        if matched_list != []:
                            cl.sendText(msg.to,"Blacklisted contact noticed...")
                            cl.sendText(msg.to,"Begin Kicking contact")
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendText(msg.to,"It looks empty here.")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(msg.to,[jj])
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        cl.sendText(msg.to,"Canceling all pending(s) invitation.")
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(msg.to,[_mid])
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        strnum = msg.text.replace("random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.01)
                                group.name = name
                                cl.updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in "Absen":
                if msg.from_ in admin:
                    cl.sendText(msg.to, "Hadir")
                    kc.sendText(msg.to, "Hadir")
                    kk.sendText(msg.to, "Hadir")
                    ki.sendText(msg.to, "Hadir")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            else:
                if cl.getGroup(msg.to).preventJoinByTicket == False:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                else:
                    print "no action"
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = kk.getProfile()
                profile2.displayName = wait["cName2"]
                kk.updateProfile(profile2)

                profile3 = ki.getProfile()
                profile3.displayName = wait["cName3"]
                ki.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
