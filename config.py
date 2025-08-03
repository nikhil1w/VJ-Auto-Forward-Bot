from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "5ee98927939d175ca953297fbe309f37")
      API_ID = int(getenv("API_ID", "24869695"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8490857707:AAGrJ21XON-hAX161XANp0za4fsdKbV-ACU")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002702049353:-/connect -1002733606326").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
