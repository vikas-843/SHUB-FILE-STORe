# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
import os
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv

load_dotenv()

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
      
# Owner Information
API_ID = int(environ.get("API_ID", "26058820"))
API_HASH = environ.get("API_HASH", "cf34db4ed69493d377a2516056711cb6")
ADMINS = int(environ.get("ADMINS", "2135144380"))

# Database Information
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://Order:order@cluster0.aitjsft.mongodb.net/?retryWrites=true&w=majority")
CDB_NAME = environ.get("CDB_NAME", "clonepbotz")
DB_URI = environ.get("DB_URI", "mongodb+srv://Order:order@cluster0.aitjsft.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "Pathananimebotz")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "6500218577:AAGxXXjqiWDpAus68bJ8K0U0uOuV9nBusWE")
BOT_USERNAME = environ.get("BOT_USERNAME", "Subh_files_bot") # your bot username without @
PICS = (environ.get('PICS', 'https://telegra.ph/file/8f108d16fe9a4b8bac79f.jpg https://telegra.ph/file/8f108d16fe9a4b8bac79f.jpg')).split() # Bot Start Picture

# Auto Delete Information
AUTO_DELETE = int(environ.get("AUTO_DELETE", "7200")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "432000")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002065194475"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002065194475')).split()]

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# File Stream Config
class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'filetolinkpathanbotz'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002065194475'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('anime-file'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://subh-files-a5c5839f3d78.herokuapp.com/"
    else:
        URL = "https://subh-files-a5c5839f3d78.herokuapp.com/"



# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
    
