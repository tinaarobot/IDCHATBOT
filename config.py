from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
STRING_SESSION = getenv("STRING_SESSION", None)
OWNER_ID = int(getenv("OWNER_ID", "6922271843"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "THE_FRIENDZ")
UPDATE_CHNL = getenv("UPDATE_CHNL", "ROY_EDITX")
OWNER_USERNAME = getenv("OWNER_USERNAME", "LOCO_X_PILOT")


