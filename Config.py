import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 16574790))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', "c408c6b40e1ebd04b76c7d04a8de1dad")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "5658314356:AAEIWcIyXBsQhRrltN_Nki6Ra5GcrTY522s")
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    BOT_USERNAME = os.environ.get('BOT_USERNAME', None)
    SUDO_ID=1484735126
    SUDO_ID1=1484735126
    SUDO_ID2=1484735126
    SUDO_ID3=1484735126
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
    DATABASE_URL = ""
    BOT_USERNAME=""
    OWNER_ID=5708737143
    SUDO_ID=1484735126
    SUDO_ID1=5989615933
    SUDO_ID2=6237097151
    SUDO_ID3=2057015874
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]

DEVS = [1484735126, 5708737143]
