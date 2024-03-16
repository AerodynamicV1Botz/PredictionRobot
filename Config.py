import os
from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 16574790))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', "c408c6b40e1ebd04b76c7d04a8de1dad")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "5658314356:AAEIWcIyXBsQhRrltN_Nki6Ra5GcrTY522s")
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    # SUDO USERS
SUDO_USER = os.environ.get("SUDO_USER", "").split())
)  # Input type must be interger

# You'll need a Private Group ID for this.
LOG_GROUP_ID = os.environ.get("LOG_GROUP_ID"))

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = os.environ.get(
    "PRIVATE_START_MESSAGE",
    "Hello! Welcome to my Personal Assistant Bot",
)

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
    START_IMG = os.environ.get('START_IMG', None)
    BOT_USERNAME = os.environ.get('BOT_USERNAME', None)
    OWNER_ID=1484735126
    OWNER_ID=5708737143
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', "AerodynamicV1_Update")
    if MUST_JOIN.startswith("@"):
        
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = ""
    API_HASH = ""
    BOT_TOKEN = ""
    START_IMG = ""
    DATABASE_URL = ""
    BOT_USERNAME=""
    OWNER_ID=1484735126
    OWNER_ID=5708737143
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]

DEVS = [1484735126, 5708737143]
