from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}.
Welcome to {}

I am the Master of Whisperers (like Varys in Game of Thrones).

You can use me to send whispers to your friend in groups and channels (even if I'm not there).
Only that friend and you will be able to read the message even though others are in same group. 

To see how to use me press 'How to Use' below.

By @StarkBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("ðŸ”’ Send a Whisper ðŸ”’", switch_inline_query="")],
        [InlineKeyboardButton(text="ðŸ  Return Home ðŸ ", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("ðŸ”’ Send a Whisper ðŸ”’", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("How to Use â”", callback_data="help"),
            InlineKeyboardButton("ðŸŽª About ðŸŽª", callback_data="about")
        ],
        [InlineKeyboardButton("â™¥ More Amazing bots â™¥", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("ðŸŽ¨ Support Group ðŸŽ¨", url="https://t.me/StarkBotsChat")],
    ]

    # Help Message
    HELP = """
Just type the message in below format in any chat.

`@WhisperStarkBot your_message friend_username/id`
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/WhisperBot)

Inspired By : nnbbot

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """
