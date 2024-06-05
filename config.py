import os

API_ID = int(os.environ.get("API_ID", "28908582"))
API_HASH = os.environ.get("API_HASH", "0d79d297bb8f56caed2c8f08bfc17289" )
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID","-1001760664883")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "5052476013"))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '-1001300777736')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
