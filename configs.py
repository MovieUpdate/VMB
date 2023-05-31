# (c) @AbirHasan2005 | @PredatorHackerzZ

import os


class Config(object):
    API_ID = os.environ.get("26283171")
    API_HASH = os.environ.get("7f23ff440eb6b551998c6c02f769071c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merger_Bot")
    UPDATES_CHANNEL = os.environ.get("-1001935083830")
    LOG_CHANNEL = os.environ.get("-1001912598096")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 100))
    STREAMTAPE_API_USERNAME = os.environ.get("63a74539acd7eafafa57")
    STREAMTAPE_API_PASS = os.environ.get("PWolGPB6BLf0zM9")
    MONGODB_URI = os.environ.get("mongodb+srv://MovieUpdate:movieupdate8270@cluster0.itptmrb.mongodb.net/?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER",1229483828))

    START_TEXT = """
𝐇𝐞𝐥𝐥𝐨! 𝐃𝐮𝐟𝐟𝐞𝐫, 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐚 𝐕𝐢𝐝𝐞𝐨 𝐌𝐞𝐫𝐠𝐞𝐫 𝐁𝐨𝐭 𝐛𝐲 [MovieUpdate](https://t.me/RequesterMUBot)!
𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐜𝐚𝐧 𝐌𝐞𝐫𝐠𝐞 𝐌𝐮𝐥𝐭𝐢𝐩𝐥𝐞 𝐕𝐢𝐝𝐞𝐨𝐬 𝐢𝐧 𝐎𝐧𝐞 𝐕𝐢𝐝𝐞𝐨 𝐀𝐧𝐃 𝐕𝐢𝐝𝐞𝐨 𝐅𝐨𝐫𝐦𝐚𝐭𝐬 𝐬𝐡𝐨𝐮𝐥𝐝 𝐛𝐞 𝐬𝐚𝐦𝐞. 

𝐌𝐚𝐝𝐞 𝐛𝐲 @RequesterMUBot
"""
    CAPTION = "𝐕𝐢𝐝𝐞𝐨 𝐌𝐞𝐫𝐠𝐞𝐝 𝐛𝐲 @{}\n\n𝐌𝐚𝐝𝐞 𝐛𝐲\n\n@RequesterMUBot"
    PROGRESS = """
🛠 𝐏𝐞𝐫𝐜𝐞𝐧𝐭𝐚𝐠𝐞 : {0}%
✅ 𝐃𝐨𝐧𝐞: {1}
📡 𝐓𝐨𝐭𝐚𝐥: {2}
🚀 𝐒𝐩𝐞𝐞𝐝: {3}/s
⏳ 𝐄𝐓𝐀: {4}
"""
