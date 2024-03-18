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

I'm {}

If you want 24 hour predictions, I am here online for you.
More Games predictions to buy Premium Subscription.

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
            InlineKeyboardButton("[►Fastwin◄]", callback_data="help"),
            InlineKeyboardButton("[►GoaGame◄]", callback_data="help2"),
            InlineKeyboardButton("[►FunWin◄]", callback_data="help3")
        ],
        [
            InlineKeyboardButton("[►BigMumbai◄]", callback_data="help4"),
            InlineKeyboardButton("[►91-Club◄]", callback_data="help5"),
            InlineKeyboardButton("[►Daman◄]", callback_data="help6")
        ],
        [
            InlineKeyboardButton("[►Tech Earning◄]", url="https://t.me/TechEarning_KingMasterMind"),
            InlineKeyboardButton("[►Prediction◄]", callback_data="about")
        ],
        [InlineKeyboardButton("[►Premium Subscription◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]

    # Help Message
    HELP = """
I'm FastWin Fastparity @PredictorAerobot. 

Get 24 hour free prediction, I am active to get prediction any time by using /fastparity command.

Enter the last 3 digits of the period number with the /fastparity command.

Example:- /fastparity241

Make Sure To register Your new Account With Our FastWin Special Link To Get Accurate Prediction 
 
Register A new Account & Deposit 1000Rs & Use Our prediction To Make More Profits. 

» Signup Bonus - ₹20
» Minimum Recharge - ₹500
» Minimum Withdrawal - ₹530
» Per Refer ₹250
» Daily Lucky Rupees 
•Invite More, Earn More!
★Agent-: @AerodynamicV1_Official

If you are new, Join now with our official team link✓.
•FastWin Special Link:- https://fastwin.app/LR?RG&C=3033148541
"""

    # About Message
    ABOUT = """
**About This @PredictorAerobot** 

This is All Game Predictor≈[🇮🇳]
A powerful Telegram Prediction bot to predict users to make profits yourself. 
────────────────────
★Network » @AerodynamicV1Botz
★Developer » @AerodynamicV1_OFFICIAL
★Owner » @Awesome_Vrajesh
★Update » @AerodynamicV1_UPDATE
★Tech Earning » @TechEarning_KingMasterMind
★ChitChat » t.me/+0l6L5-ArBRU2ZGRl
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
    
