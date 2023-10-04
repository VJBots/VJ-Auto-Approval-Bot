from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20389440"))
    API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
    BOT_TOKEN = getenv("BOT_TOKEN", "6564513574:AAGDqUaEmeu0m4DjLDetNc4nooVTWYT7Fzo")
    FSUB = getenv("FSUB", "VJ_Botz")
    CHID = int(getenv("CHID", "-1001623633000"))
    SUDO = list(map(int, getenv("").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
