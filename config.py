# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "19275563"))
API_HASH = getenv("API_HASH", "332213ccd9f10bd2924e4824172e791e")
BOT_TOKEN = getenv("BOT_TOKEN", "7848960852:AAHJHVhH3_u--eoSxO7qRG1Nhr9PIOl6Pas")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5617986165").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://kingrajashish43211:rOYviMdPMPfCvSlR@cluster0.j3o3sbf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002736554970")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002590849783"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", "BQEmHysAGNjGx3tlmcCz4e64wx_mttE4GaJLLXRRPxpUt94PMSuR3ytvY-Os6x2SRJqLg3QKqJDT1EUY16rRZdtppG8cP9mQpki6vXub7q3IwnRLA5HkCouHhBGBQARo_gjnuxbrmRUmbkJnYBR6vsAW9Vl2XkoCmXtljASqj2gvc7k0Tg0tu2OlGLlMb77pwrELhL1KjN9V9Iz6wCFgobliFIhtAChUsQzjzJU7NhaLUTOnm0b8_6fuxT9Ve40Fskfm96O56lQ67k65lnRrho6pkg_j7xTcGOXQM6h1R0UJOacHomfE0-cUu4-smr8MpHNiSzQENgRvzdOjgRLwMRVk5vAzZgAAAAFO26p1AA")
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
