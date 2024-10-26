import json
import os

from VIPMUSIC.core.bot import VIPBot
from VIPMUSIC.core.dir import dirr
from VIPMUSIC.core.git import git
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()

git()

dbb()

heroku()

sudo()

app = VIPBot()

userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}

YOUTUBE = {
    "access_token": "ya29.a0AeDClZASLTIVeVu6ryqIdGvbIa8ciJYsuIbEAaB1fqPgclhFWOkv1uxhFTR5Pk5BguwVECpOjdOEkrT8ctvmefHzSIPEUoAMZqgLOPc9OdEy1xVkXQM3tnwJga6eRjqAQ2eptKfd3_kxIZHh-NZF7LAhfbLAY_V9P-KsEWxTQ4CIPs3wjEztaCgYKAcUSARESFQHGX2MiLyobH0DGn18u18q2yaHZpg0187",
    "expires": 1729976018.907575,
    "refresh_token": "1//05AEnUA8gnn6nCgYIARAAGAUSNwF-L9Ir3759d17CZH48CJpeAd7Aw-BSYUz6LcbKvKXZJ3F8cmgTX3QvkZ3Uf4pR7-nCDeRNWPg",
    "token_type": "Bearer"
}

os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
