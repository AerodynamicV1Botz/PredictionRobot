from pyrogram.types import InlineKeyboardButton

DFASTPARITY_IMG = [
"https://graph.org/file/8e58b2d5c29e4dd4a1356.jpg",
"https://graph.org/file/8e58b2d5c29e4dd4a1356.jpg",
]

FASTWIN_IMG = [
"https://graph.org/file/1ca3b40f02bdae4273414.jpg",
"https://graph.org/file/1ca3b40f02bdae4273414.jpg",
]

FASTPARITY_IMG = [
"https://graph.org/file/36cca83089dcdb491bf30.jpg",
"https://graph.org/file/a9e7ddacfc1609222db7d.jpg",
"https://graph.org/file/5c022f19bbf35fcccfb3e.jpg",
"https://graph.org/file/b8e5286a132683ec5c8f3.jpg",
"https://graph.org/file/67fef880e884f53665046.jpg",
"https://graph.org/file/6ada8d933e65552e3f393.jpg",
"https://graph.org/file/6310519782e9c91177460.jpg",
"https://graph.org/file/7051eebc8db7385a23b1a.jpg",
"https://graph.org/file/907c390a9e05dc4783c6a.jpg",
"https://graph.org/file/d3ed9cf197e2e6929a73a.jpg",
"https://graph.org/file/f84481f3be97455acd998.jpg",
"https://graph.org/file/14e00d0ad3f15ec7708f5.jpg",
"https://graph.org/file/ce968e6f650229e35625c.jpg",
"https://graph.org/file/4a3749e8fa0956ddf0259.jpg"
"https://graph.org/file/6e86160ccaf99eefe98d7.jpg",
"https://graph.org/file/76bb3198300f16017e648.jpg",
"https://graph.org/file/65708613a6918d9d5fd72.jpg",
"https://graph.org/file/a9de9d03d90fe71971eb7.jpg",
"https://graph.org/file/df3c1b63f6be30c7635da.jpg",
"https://graph.org/file/5b1abf3d89f410dcd5abc.jpg",
]

class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can force your group's users to join a particular chat. 
The chat can be a group or channel. It can be private or public.

📚Use below buttons to learn more !

•Made By [AerodynamicV1~🇮🇳](https://telegram.me/AerodynamicV1_OFFICIAL)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="[► Return Home ◄]", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("[►👁️‍🗨️Tutorial◄]", url="https://youtu.be/flYDpr4Ox1c"),
            InlineKeyboardButton("[►How to Use❔◄]", callback_data="help")
        ],
        [
            InlineKeyboardButton("[►Tech Earning◄]", url="https://t.me/TechEarning_KingMasterMind"),
            InlineKeyboardButton("[►About Me◄]", callback_data="about")
        ],
        [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/Fiewin_Colour_Prediction_Winner"),
        InlineKeyboardButton("[►Update🔔◄]", url="https://t.me/AerodynamicV1_UPDATE")]
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub @AerodynamicV1_UPDATE` or `/forcesubscribe -1001212351472`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

     🔰**Available Commands**🔰

/fsub Or /forcesubscribe chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel

__**{►👁️‍🗨️ Watch Tutorial👉 [Click Here](https://youtu.be/flYDpr4Ox1c)◄}**__
    """


    # About Message
    ABOUT = """
**About This Bot** 

This is Aero ✘ Force Subscriber~🇮🇳
A powerful Telegram subscribing bot to force users in your group to join a particular chat. 
────────────────────
★Network » @AerodynamicV1Botz
★Developer » @AerodynamicV1_OFFICIAL
★Update » @AerodynamicV1_UPDATE
★Tech Earning » @TechEarning_KingMasterMind
★Support » @Fiewin_Colour_Prediction_Winner
★Free Promotion » @AerodynamicV1_Promotion
    """

    # Fastparity Message
    FASTPARITY = """
Hey {},

I'm FastWin Fastparity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /fastparity command.

Example:- /fastparity792

Ask your doubts at Support Chat.
   """

    # Fast Message
    FAST = """
Hey {}, look at the Result ☝️

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://fastwin.app/LR?RG&C=3033148541

Register A new Account And Deposit 1000Rs and Use Our prediction To Make More Profits. 
    """
    
    # Fasthome Button
    fasthome_buttons = [
        [InlineKeyboardButton(text="[► Return Home ◄]", callback_data="aerohome")],
    ]
    # Fastwin Buttons
    gamebuttons = [
        [
            InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
            InlineKeyboardButton("[►FastWin❔◄]", url="https://t.me/TechEarning_KingMasterMind/9932")
        ],
        [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/https://t.me/+0l6L5-ArBRU2ZGRl"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
]

    # Fastwin Message 
    FASTWIN = """
Get Fastparity Prediction To Enter Last 3 digits of period with /fastparity Command.
Example:- /fastparity001 to /fastparity999

» Signup Bonus - ₹20
» Minimum Recharge - ₹500
» Minimum Withdrawal - ₹530
» Per Refer ₹250
» Daily Lucky Rupees 
•Invite More, Earn More!

★Agent-: @AerodynamicV1_Official

If you are new, Join now with our official team link✓.
•FastWin Register Link:- https://fastwin.app/LR?RG&C=3033148541
"""

    # Fastwin Buttons
    fastwinbuttons = [
       [
            InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
            InlineKeyboardButton("[►Register Link◄]", url="https://fastwin.app/LR?RG&C=3033148541")
        ],
        [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/https://t.me/+0l6L5-ArBRU2ZGRl"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
]
    
