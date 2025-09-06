from MITSURIMUSIC.core.bot import TOXIC
from MITSURIMUSIC.core.dir import dirr
from MITSURIMUSIC.core.git import git
from MITSURIMUSIC.core.userbot import Userbot
from MITSURIMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = TOXIC()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
