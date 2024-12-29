# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
