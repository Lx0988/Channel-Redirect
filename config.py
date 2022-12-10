
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5300015911:AAHiwT8Ze-8bR3PaN0xGKlzxqNWADRFl7jg")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "7961171"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "b2d798626afaf5f1e4bdb33988e3d377")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQBFcTPHCdz1KIUDTBghJjJxoop7sXzdQ23pynzKHbmXB9yEKGPGhMpZ9m3JVrJVIaOHpK3rJwPKVTzdJ1lS3uEm_01ecfeY0hAnfLhNWo433D-iA-LofkjogqnfBAxTbVv81GSkDfpJbDgV3Ew-fx_WZYvZD5ria5_niXm7KREGWaQoXbTOqiHquhSv0tqo5_2Gv300rOqA9X2BQxiTB_qIQV-EvSXw0Wn33Ou7L6vcXplsyj52tLqfiybzELl87eaHZrTtKfHiJR52WZetNs8xfOX10muOQYuPKUek_u0JvwcERuGv5_mY1Hj6GJS4aN2eMdo_X1A56e3EcpEspIkCAAAAAUSZaVUA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001531149575")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
