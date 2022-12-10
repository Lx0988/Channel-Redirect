
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = "5300015911:AAHiwT8Ze-8bR3PaN0xGKlzxqNWADRFl7jg"

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = 7961171

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = "b2d798626afaf5f1e4bdb33988e3d377"

# Generate a user session string 
TG_USER_SESSION = "BQCU0K9e7yc3uf7BKg0HV5AXyKyH_bcIkPetK0wVuMOS3sjCoheeI1qM8kEPaaLOXMEkWe0r2tUdIfAujKQXCH7sX_bUJUAuVgitbCvEImlptn_BAglpPBrdzWbj0TRLhsBwxC_isLwqb2QaPguQYH2Dl0MsmNPyOlGDxa5decW4otL1-BDPmRr_x5uWKxLi5Vf2g74qU0TJLHNXBSFSVmDw-2eMAO-G30QvgmMzOm365RFRl9pFQqzORaielkbhXdyP1BIlgHXbVRibfEsDIbqBU3dw1YsBF8qZDFZESbiD1MjvqdHGkgmk6YFmaM9ZvtM6CQH_CtYsY-ZREPV07c6zAAAAAT2AioUA"

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = "-1001531149575"




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
