import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://t.me/tamcinemas')
    START_TXT = environ.get("START_TXT", '''𝙃𝙚𝙮 {},
𝙈𝙮𝙨𝙚𝙡𝙛 <a href=https://t.me/{}>{}</a>,\n\n𝗧𝗿𝘂𝘀𝘁 𝗺𝗲 ❗ 𝗜 𝗰𝗮𝗻 𝗼𝗳𝗳𝗲𝗿 𝘆𝗼𝘂 𝗠𝗢𝗩𝗜𝗘𝗦/𝗦𝗘𝗥𝗜𝗘𝗦. 𝗦𝗮𝘃𝗲 𝘆𝗼𝘂𝗿 𝗧𝗶𝗺𝗲 𝗯𝘆 𝗔𝗱𝗱𝗶𝗻𝗴 𝗠𝗲𝗵 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 𝗮𝗻𝗱 𝗲𝗻𝗷𝗼𝘆 𝗺𝘆 𝗰𝗮𝗽𝗮𝗯𝗶𝗹𝗶𝘁𝗶𝗲𝘀 \n\nᴀʀᴇ ʏᴏᴜ ʀᴇᴀᴅʏ ᴍʏ ʙᴜᴅᴅʏ...🤪''')
  
    HELP_TXT = "Hᴇʏ {}\nHᴇʀᴇ Mꜱ Mʏ Hᴇʟᴩ"
   
    ABOUT_TXT = """✯ 𝙈𝙮 𝙉𝙖𝙢𝙚: {}
✯ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧: <a href=t.me/tamcinemas>𝙋𝙧𝙖𝙫𝙚𝙚𝙣 𝙆𝙪𝙢𝙖𝙧 𝙆</a>
✯ 𝙇𝙞𝙖𝙗𝙧𝙖𝙧𝙮: 𝙋𝙮𝙧𝙤𝙜𝙧𝙖𝙢
✯ 𝙇𝙖𝙣𝙜𝙪𝙖𝙜𝙚: 𝙋𝙮𝙩𝙝𝙤𝙣 3
✯ 𝘿𝙖𝙩𝙖𝙗𝙖𝙨𝙚: 𝙈𝙤𝙣𝙜𝙤 𝘿𝘽
✯ 𝘽𝙤𝙩 𝙎𝙚𝙧𝙫𝙚𝙧: 𝙆𝙤𝙮𝙚𝙗
✯ 𝘽𝙪𝙞𝙡𝙙 𝙎𝙩𝙖𝙩𝙪𝙨: v2.0.1 [ 𝙈𝙖𝙨𝙩𝙚𝙧 𝙍𝙤𝙨𝙝𝙞 🪶 ]"""
   
    SOURCE_TXT ="""<b>NOTE:</b>
- ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʜᴇʀᴇ ◉› :<a href=https://github.com/shinchan2627/Master-Roshi-Bot>𝙈𝙖𝙨𝙩𝙚𝙧 𝙍𝙤𝙨𝙝𝙞 🪶</a>

<b>ᴅᴇᴠ: <a herf=https://t.me/tamcinemas>Praveen Kumar K</a></b>"""
    
    
    """<b>𝙈𝙖𝙨𝙩𝙚𝙧 𝙍𝙤𝙨𝙝𝙞 🪶 is an open source project</b>

You can easily get its source code from github - <a href='https://github.com/shinchan2627/Master-Roshi-Bot'></a>"""
   
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ꜱᴇᴀʀᴄʜ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
   
    BUTTON_TXT = """Help: <b>Buttons</b>

- Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:t.me/tamcinemas)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
   
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
   
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
  
    
    STATUS_TXT = """★ 𝙏𝙤𝙩𝙚𝙡 𝙁𝙞𝙡𝙚𝙨: <code>{}</code>
★ 𝙏𝙤𝙩𝙚𝙡 𝙐𝙨𝙚𝙧𝙨: <code>{}</code>
★ 𝙏𝙤𝙩𝙚𝙡 𝘾𝙝𝙖𝙩𝙨: <code>{}</code>
★ 𝙐𝙨𝙚𝙙 𝙎𝙩𝙤𝙧𝙖𝙜𝙚: <code>{}</code> 𝙼𝚒𝙱
★ 𝙁𝙧𝙚𝙚 𝙎𝙩𝙤𝙧𝙖𝙜𝙚: <code>{}</code> 𝙼𝚒𝙱"""
  
    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

◉ ɢʀᴏᴜᴩ: {a}
◉ ɢ-ɪᴅ: <code>{b}</code>
◉ ʟɪɴᴋ: @{c}
◉ ᴍᴇᴍʙᴇʀꜱ: <code>{d}</code>
◉ ᴀᴅᴅᴇᴅ ʙʏ: {e}

◉ ʙʏ: @{f}</b>"""
  
    LOG_TEXT_P = """#ɴᴇᴡ_ᴜꜱᴇʀ
    
◉ ᴜꜱᴇʀ-ɪᴅ: <code>{}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {}
◉ ᴜꜱᴇʀɴᴀᴍᴇ: @{}

◉ ʙʏ: @{}</b>"""
