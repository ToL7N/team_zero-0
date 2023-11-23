import asyncio
import random
import telethon
from telethon import events
from queue import Queue
from telethon.tl.types import DocumentAttributeVideo
import requests
from telethon.sync import functions
from telethon.tl.functions.channels import JoinChannelRequest
from user_agent import generate_user_agent
import requests
from user_agent import *
from config import *
from threading import Thread

band = []
isclaim = ["off"]
isauto = ["off"]
with open("band.txt", "r") as f:
    f = f.read().split()
    band.append(f)

que = Queue()

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"

def gen_user(choice):
    if choice == "6":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in band[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "100":
        c = random.choices(a) 
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], s[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in band[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], s[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "1":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0],'_'[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in band[0]:
            c = random.choices(a)
            d = random.choices(e)
            f = [c[0], d[0], c[0],'_'[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "2":
        q = random.choices(b)
        w = random.choices(b)
        E = random.choices(b)
        r = random.choices(b)
        f = [q[0], w[0], E[0], r[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = 'vip'+username
        if username in band[0]:
            E = random.choices(b)
            w = random.choices(b)
            r = random.choices(b)
            q = random.choices(b)
            f = [q[0], w[0], E[0], r[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = 'vip'+username
        else:
            pass
    if choice == "3":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in band[0]:
            c = random.choices(a)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "4":
        c = random.choices(a)
        d = random.choices(e)
        k = random.choices(e)
        f = [c[0], k[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in band[0]:
            c = random.choices(a)
            d = random.choices(e)
            f = [c[0], c[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "5":
        c = d = random.choices(a)
        d = random.choices(e)
        k = d = random.choices(e)
        f = [c[0], d[0], d[0], d[0], k[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in band[0]:
            c = random.choices(a)
            d = random.choices(e)
            k = d = random.choices(e)
            f = [c[0], d[0], d[0], d[0], k[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    return username

@a.on(events.NewMessage(outgoing=True, pattern=r"تيربو"))
async def bh(event):
    await a(JoinChannelRequest("AbnBashaar"))
    await a.send_message(event.chat_id, '''تثبيت قناة + يوزر قناتك + يوزر
L7N + نوع + يوزر قناتك
تثبيت حساب + يوزر
stop = ايقاف
الصيد = عدد المحاولات
وضع اليوزر دون @

1 aba_b
2 vip1234
3 abaaab
4 acbbbb
5 acccb
6 abcbot

فحص + 2 @يوزر قناتك
''')

@a.on(events.NewMessage(outgoing=True, pattern=r"فحص"))
async def bh(event):
    if ispay2[0] == "yes":
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        c = str(msg[1])
        choice = str(msg[0])
        await event.edit(f"تم بدأ الصيد .! قناة السورس @illl0")

        @a.on(events.NewMessage(outgoing=True, pattern=r"الصيد"))
        async def _(event):
            if ispay2[0] == "yes":
                if "on" in isclaim:
                    await event.edit(f"Clicks = ``({t})`` ** ")
                elif "off" in isclaim:
                    await event.edit("There is NO working check !")
                else:
                    await event.edit("ايرور")
            else:
                pass
        for i in range(2000000):
            if ispay2[0] == 'no':
                break
            username = ""

            username = gen_user(choice)
            t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
            t.start()
            t.join()
            isav = que.get()
            if "Available" in isav:
                try:
                    await a(functions.channels.UpdateUsernameRequest(
                        channel=bh, username=username))
                    await a.send_file("i5tbot", 'https://telegra.ph/file/1340fae37117e4f85f9af.mp4', caption=f''' 
𓆩 We are the strongest @illl0 !'
⎱UserName: ❲ @{username} ❳
⎱ClickS: ❲ 1828 ❳
⎱Save: ❲ Channel ❳
⎱By : ❲ 𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™ ❳                                     ''')
                    await event.client.send_message(event.chat_id, f'''
𓆩 We are the strongest @illl0 !'
⎱UserName: ❲ @{username} ❳
⎱ClickS: ❲ 1828 ❳
⎱Save: ❲ Channel ❳
⎱By : ❲ 𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™ ❳    
    ''')
                    break
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    with open("band.txt", "a") as f:
                        f.write(f"\n{username}")
                except Exception as eee:
                    await a.send_message(event.chat_id, f'''error with {username}
{str(eee)}''')
                    if "A wait of" in str(eee):
                        break
                    else:
                        pass
                    t += 2
                    await asyncio.sleep(1)
        isclaim.clear()
        isclaim.append("off")
        t = ""

@a.on(events.NewMessage(outgoing=True, pattern=r"تثبيت"))
async def _(event):
    if ispay2[0] == "yes":
        trys = 0
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg[0] == "قناة":
            isauto.clear()
            isauto.append("on")
            msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[1])
            ch = str(msg[0])
            await a.send_message(event.chat_id, f"Started successfully → `{ch}`")
            for i in range(15000000):
                if ispay2[0] == 'no':
                    break
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    try:
                        await a(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))
                        
                        await a.send_file("i5tbot", 'https://telegra.ph/file/1340fae37117e4f85f9af.mp4', caption=f'''
𓆩 We are the strongest @illl0 !'
⎱UserName: ❲ @{username} ❳
⎱ClickS: ❲ 1828 ❳
⎱Save: ❲ Channel ❳
⎱By : ❲ 𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™ ❳                            ''')
                        await a.send_file(event.chat_id, 'https://telegra.ph/file/6bd6a1cde2b1a9f2256f7.mp4', caption=f'''
𓆩 We are the strongest @illl0 !'
⎱UserName: ❲ @{username} ❳
⎱ClickS: ❲ 1828 ❳
⎱Save: ❲ Channel ❳
⎱By : ❲ 𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™ ❳                            
 ''')
                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"band the @{username} ")
                        break
                else: 
                    pass
                trys += 1
                await asyncio.sleep(0.5)
            trys = ""
            isauto.clear()
            isauto.append("off")
            await a.send_message(event.chat_id, "done ⤷ 1")

@a.on(events.NewMessage(outgoing=True, pattern=r"تثبيت"))
async def _(event):
    if ispay2[0] == "yes":
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg[0] == "حساب":
            isauto.clear()
            isauto.append("on")
            msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[0])
            await a.send_message(event.chat_id, f"ok - `{username}`")
            for i in range(1500000000):
                if ispay2[0] == 'no':
                    break
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    try:
                        await a(functions.account.UpdateUsernameRequest(
                            username=username))
                        trys += 1
                        await a.send_file(event.chat_id, 'https://telegra.ph/file/bcccc26d9ad8390159240.mp4', caption=f'''
𓆩 We are the strongest @illl0 !'
⎱UserName: ❲ @{username} ❳
⎱ClickS: ❲ {trys} ❳
⎱Save: ❲ Channel ❳
⎱By : ❲ 𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™ ❳    
''')
                        await a.send_file("i5tbot", 'https://telegra.ph/file/bcccc26d9ad8390159240.mp4', caption=f'''
𓆩 We are the strongest @illl0 !'
⎱UserName: ❲ @{username} ❳
⎱ClickS: ❲ {trys} ❳
⎱Save: ❲ Channel ❳
⎱By : ❲ 𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™ ❳   
''')
                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"band the @{username} ")
                        break
                else:
                    pass
                trys += 1

            trys = ""
            isauto.clear()
            isauto.append("off")
            await a.send_message(event.chat_id, "done bro")
            
