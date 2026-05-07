import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8415514217:AAFgSxR_RPuzge7J7tXYDFrmIFalRUeFTB8")
    API_ID = int(os.environ.get("API_ID", 27317669))
    API_HASH = os.environ.get("API_HASH", "11b88c331c5d44fde57cf91de1a2156b")
    AUTH_USER = os.environ.get('AUTH_USERS', '6947378236').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER if user_id]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "𝗥𝗼𝘆 𝗝𝗮𝗮𝘁™"#Here You Can Change with Your Name  or any custom name or title you prefer
    
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1002360435278))
    DB_NAME = os.environ.get("DB_NAME", "cluster0")
    FORCE_SUB = int(os.environ.get("FORCE_SUB", -1002360435278))
    FREEMIUM_LIMIT = int(os.environ.get("FREEMIUM_LIMIT", 10))
    LOG_GROUP = int(os.environ.get("LOG_GROUP", -1002896498332))
    MONGO_DB = os.environ.get("MONGO_DB", "mongodb+srv://coolcriminal:Cool@cluster0.idhak.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    OWNER_ID = int(os.environ.get("OWNER_ID", 6947378236))
    PREMIUM_LIMIT = int(os.environ.get("PREMIUM_LIMIT", 5000))
