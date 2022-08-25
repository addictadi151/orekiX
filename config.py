from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = int(getenv("BOT_TOKEN"), "5527356677:AAElYDHZ0cJrN02jdh6HcEf2ooUvcZ9Zy4w")) 
API_ID = int(getenv("API_ID", "17027090"))
API_HASH = int(getenv("API_HASH"), "7fed20862f47bb90a759205c67a97cd0")) 
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = int(getenv("MONGO_DB_URI"), "mongodb+srv://Jerry:jerryxd@cluster0.1pjuwue.mongodb.net/?retryWrites=true&w=majority")) 
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5590420589").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5590420589").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001672156185"))
MUSIC_BOT_NAME = int(getenv("MUSIC_BOT_NAME"), "Jerry")) 
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = "https://github.com/addictadi151/orekiX"
UPSTREAM_BRANCH = "main"

SUPPORT_CHANNEL = "https://t.me/DANISH_BABA"
SUPPORT_GROUP = "https://t.me/WEFRIENDSCIRCLE"

THUMBNAIL = getenv("THUMB_LINK") 

botusername = str(getenv("BOT_USERNAME"))

if str(getenv("STRING_SESSION1")).strip() == "AQA3qFIKOClwVrVDY1E_Q7gEg8GDxi3gdgyvydtyNFguiRXIXVEo-Ilgv6mpJ1Meh1CSOfiU2EtSJ0yr_I-RdzOuhZWHStgwqQiVnGOKjMmu-l03dbB4na9yrrzRPxB5C3QgyWwxMyt9fV-dIdLzzjT2wUbJGYecHhhtR8bEpmXNFhJP8JMurXzFmOa-fiNUv3v3Yl7gVGHq012hPV882LVYmFZezVqwRzynhIH1tI0crEj3NWY1ODlM6iXpBQr8d7A0Wb55OGtkuI5-vRggnbi_26KdtAh2zuxYXk733Mq5BZG7bJjsB5wjM1J5EySl9HGmHG3wsunqQKaMzSEFEvHqAAAAAT0EXwwA":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))

if str(getenv("LIMIT")).strip().upper() == "FALSE":
    PL_LIMIT = "FALSE"
else:
    PL_LIMIT = "TRUE"

if str(getenv("PM_PERMIT")).strip().upper() == "FALSE":
    PM_PERMIT = "FALSE"
else:
    PM_PERMIT = "TRUE"
