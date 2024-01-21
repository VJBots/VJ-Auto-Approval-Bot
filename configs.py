# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28421635"))
    API_HASH = getenv("API_HASH", "a4856de5fec0b9b3601ff06425f3f58e)
    BOT_TOKEN = getenv("BOT_TOKEN", "6947074831:AAHfx5XvS6p0BXjamh3mdIKtjaC6MMgM4x0")
    FSUB = getenv("FSUB", "TeamAnimePedia")
    CHID = int(getenv("CHID", "-1001991806323)
    SUDO = list(map(int, getenv("SUDO", "6657660775").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Filebot:Filebot@cluster0.1kdt8x3.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

