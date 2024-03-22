from pyrogram.types import InlineKeyboardButton

START_IMG = ["https://graph.org/file/4a0df73c438e618ac337d.jpg"]

PAYMENT_IMG = [
"https://graph.org/file/0efe9a166cf9177f193a9.jpg",
"https://graph.org/file/0efe9a166cf9177f193a9.jpg",
]

SIZE = [
"https://graph.org/file/096922735e511629f4933.jpg",
"https://graph.org/file/fab245e1f063b08b74aa2.jpg",
]

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

FUNWIN_IMG = [
"https://graph.org/file/e1b3936d257a1b408b2fb.jpg",
"https://graph.org/file/e1b3936d257a1b408b2fb.jpg",
]

FUNWINPARITY_IMG = [
"https://graph.org/file/6ee7466ebbec46a6fe80f.jpg"
"https://graph.org/file/f1e9800539af3154b3ac5.jpg",
"https://graph.org/file/349469066378c1c1b27ba.jpg",
"https://graph.org/file/ed0bf655df070867a98b0.jpg",
"https://graph.org/file/7e8337d909f9829b56003.jpg",
"https://graph.org/file/bb551518253815c5deb3e.jpg",
"https://graph.org/file/f945a2a251a7d2ae7dcc8.jpg",
"https://graph.org/file/ed0bf655df070867a98b0.jpg",
"https://graph.org/file/ff9315a6a5847b6d9e7c2.jpg",
"https://graph.org/file/7c14028a211908f82f2c4.jpg",
"https://graph.org/file/90bd67ea9655caee38fee.jpg",
"https://graph.org/file/6527972ee1ca626c199e9.jpg",
"https://graph.org/file/17213e0f9078e4c4c1bcb.jpg",
"https://graph.org/file/4f78b1055639de8ff5b43.jpg",
"https://graph.org/file/ecb9bfffc1883fae1ec96.jpg",
"https://graph.org/file/105c3d5c4390bee5992cf.jpg",
"https://graph.org/file/75c44e33848cd82586c89.jpg",
"https://graph.org/file/ec6ea1c24f05775839352.jpg",
"https://graph.org/file/569ace5488aefa50891f7.jpg",
"https://graph.org/file/f7171224427541ab9d54d.jpg",
]

FUNWINFASTPARITY_IMG = [
"https://graph.org/file/f1a03f7349a136cb7f1e1.jpg",
"https://graph.org/file/08858d76afa4afd257ee0.jpg",
"https://graph.org/file/7f9462843e93eb2bb7b40.jpg",
"https://graph.org/file/9065b78c6bcac98f9221c.jpg",
"https://graph.org/file/a6ea3c11261edaba9ac6b.jpg",
"https://graph.org/file/7099b879a81827f8e061a.jpg",
"https://graph.org/file/882445ad9131b02b3f54c.jpg",
"https://graph.org/file/5a44d2259d253aada769c.jpg",
"https://graph.org/file/65423793ea670254c7a38.jpg",
"https://graph.org/file/3eb8c038f31a3239ad184.jpg",
"https://graph.org/file/30e0c426c988eacd75782.jpg",
"https://graph.org/file/5a44d2259d253aada769c.jpg",
"https://graph.org/file/01330607ef98ccc4254f1.jpg",
"https://graph.org/file/15d4b7e695974d8b819a0.jpg",
"https://graph.org/file/cd8bedbce8db82a80d9e2.jpg",
"https://graph.org/file/b49c4303e347182243b0e.jpg",
"https://graph.org/file/d74152e0f477feed5054a.jpg",
"https://graph.org/file/b0d3c455ded88effbf979.jpg",
"https://graph.org/file/a713d3daeb8a6f2e3a81a.jpg",
"https://graph.org/file/3b00713d66156de3de9a6.jpg",
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
    startbuttons = [
        [
            InlineKeyboardButton("[►Fastwin◄]", url="https://t.me/PredictorAerobot?start=fastwin"),
            InlineKeyboardButton("[►FunWin◄]", url="https://t.me/PredictorAerobot?start=funwin")
        ],
        [
            InlineKeyboardButton("[►Tech Earning◄]", url="https://t.me/TechEarning_KingMasterMind"),
            InlineKeyboardButton("[►Prediction◄]", url="https://t.me/PredictorAerobot?start=about")
        ],
        [InlineKeyboardButton("[►Premium Subscription◄]", url="https://t.me/Awesome_Vrajesh")]
    ]
    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="[► Return Home ◄]", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
        InlineKeyboardButton("[►Developer◄]", url="https://telegram.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►Agent◄]", url="https://telegram.me/Awesome_Vrajesh")
        ],
        [InlineKeyboardButton("[►Get All Game Prediction◄]", callback_data="allgame")],
        [InlineKeyboardButton("[►Get Premium Subscription◄]", callback_data="premium")],
        [
        InlineKeyboardButton("[►Tech Earning◄]", url="https://t.me/TechEarning_KingMasterMind"),
        InlineKeyboardButton("[►Support Chat◄]", url="https://t.me/EarningTeamSupportChat")
        ],
    ]

    #QR
    QR = """
Scan This QR or Send money through Paytm, G-Pay, PhonePe or Any other UPI App.

✅After payment successful then Show me your payment receipt...!

After making the payment, send it to me here :- t.me/+36Pm3qwJKjMwOGM1

I will add you in premium users, then you can get predictions of all games for 24 hours.
"""
    # Payment Message
    PAYMENT = """
Send money through Paytm, G-Pay, PhonePe or Any other UPI App.

/QR 👈 use this command for scanner.

Name:- Vasava Vrajeshkumar

Payment UPI-:
━━━━━━━━━━━━━━━━━━━━━━
`vrajeshvasava22@paytm` 👈copy
━━━━━━━━━━━━━━━━━━━━━━
`vrajeshvasava22@jio` 👈copy
━━━━━━━━━━━━━━━━━━━━━━
✅After payment successful then Show me your payment receipt...!

After making the payment, send it to me here :- t.me/+36Pm3qwJKjMwOGM1

I will add you in premium users, then you can get predictions of all games for 24 hours.
"""

    # PREMIUM SUBSCRIPTION 
    PREMIUM = """
💫Premium Subscription of all games is being given at the same rate...🇮🇳
Buy it friend, all in one combo pack...😎

🔰🔰🔰Premium Plan Offers🔰🔰🔰
━━━━━━━━━━━━━━━━━━━━━━
💥 64% off  ₹700 
✅ ₹252 for 7 days 
━━━━━━━━━━━━━━━━━━━━━━
💥 66.66% off ₹1500 
✅ ₹500 for 15 days 
━━━━━━━━━━━━━━━━━━━━━━
💥 66.66% off ₹3000 
✅ ₹1000 for 30 days 
━━━━━━━━━━━━━━━━━━━━━━
💥 68% off ₹9,000 
✅ ₹2880 for 90 days
━━━━━━━━━━━━━━━━━━━━━━
💥 69% off ₹18,000
✅ ₹5500 for 180 days 
━━━━━━━━━━━━━━━━━━━━━━
💥 72% off ₹36500
✅ ₹10220 for 365 days
━━━━━━━━━━━━━━━━━━━━━━
🥳Select your Premium Plan...✨
🔰Click Payment Method Button🔰
"""
    
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
━━━━━━━━━━━━━━━━━━━━━━
This is All Game Predictor≈[🇮🇳]
A powerful Telegram Prediction bot to predict users to make profits yourself. 
━━━━━━━━━━━━━━━━━━━━━━
★Network » @AerodynamicV1Botz
★Developer » @AerodynamicV1_OFFICIAL
★Owner » @Awesome_Vrajesh
★Update » @AerodynamicV1_UPDATE
★Tech Earning » @TechEarning_KingMasterMind
★ChitChat » @EarningTeamSupportChat
★Support » @Fiewin_Colour_Prediction_Winner
★Free Promotion » @AerodynamicV1_Promotion
    """

    # Fastparity Message
    FASTPARITY = """
Hey {},

I'm FastWin Fastparity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /fastparity command.

Example:- /fastparity792

Ask your doubts at @EarningTeamSupportChat.
   """
    # Fastparity Message
    FUNWINFASTPARITY = """
Hey {},

I'm FastWin Fastparity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /fastparity command.

Example:- /fastparity792

Ask your doubts at @EarningTeamSupportChat.
   """

    # parity Message
    PARITY = """
Hey {},

I'm FastWin Parity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /parity command.

Example:- /parity792

Ask your doubts at @EarningTeamSupportChat.
   """
    
    BMWINGO = """
Hey {},

I'm Big Mumbai Wingo 1 Minute Game {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /BMwingo command.

Example:- /BMwingo792

Ask your doubts at @EarningTeamSupportChat.
"""
    BDGWINGO = """
Hey {},

I'm Big Daddy Wingo 1 Minute Game {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /BDGwingo command.

Example:- /BDGwingo792

Ask your doubts at @EarningTeamSupportChat.
"""
    GGWINGO = """
Hey {},

I'm GoaGame Wingo 1 Minute Game {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /GGwingo command.

Example:- /GGwingo792

Ask your doubts at @EarningTeamSupportChat.
"""
    # parity Message
    FUNWINPARITY = """
Hey {},

I'm FastWin Parity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /parity command.

Example:- /parity792

Ask your doubts at @EarningTeamSupportChat.
   """

    # Fast Message
    FAST = """
Hey {}, look at the Result ☝️

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://fastwin.app/LR?RG&C=3033148541

Register A new Account And Deposit 1000Rs and Use Our prediction To Make More Profits. 
    """

    # Fast Message




    TCRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://goagame.com/#/register?invitationCode=275731115445
"""
    TIRANGARESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://goagame.com/#/register?invitationCode=275731115445
"""

    # Fastwin Buttons
    gggbuttons = [
        [
            InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
            InlineKeyboardButton("[►GoaGame❔◄]", url="https://goagame.com/#/register?invitationCode=275731115445")
        ],
        [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
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
        [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
]

    # Fastwin Message 
    FASTWIN = """
✅ Welcome to FastWin Game🥳😎
━━━━━━━━━━━━━━━━━━━━━━
🔰Joining Bonus -: 40Rs
🔰Minimum Recharge -: 500Rs
🔰Minimum Withdrawal -: 530Rs 
🔰Withdraw timings -: 10am to 7pm
🔰Per Refer -:500Rs🤩🤩
🔰Everyday Lucky Lifafa 10rs 😚
✨Invite More, Earn More!

▪️If you are new, join our official team link now.

✅FastWin Register Link:- https://fastwin.app/LR?RG&C=3033148541
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which Fastwin game prediction you want...👇
"""

    # Home Button
    fastwinhome_buttons = [
    [
        InlineKeyboardButton("[►Fastparity◄]", callback_data="fastwinfastparity"),
        InlineKeyboardButton("[►Parity◄]", callback_data="fastwinparity")
    ],   
        [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]

        # Home Button
    fastwinhome = [
        [InlineKeyboardButton(text="[► Return FastWin ◄]", callback_data="fastwin")],
    ]
    
    # Fastwin Buttons
    fastwinbuttons = [
       [
            InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
            InlineKeyboardButton("[►Register Link◄]", url="https://fastwin.app/LR?RG&C=3033148541")
        ],
        [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
]

    # Fast Message
    FUNWINFAST = """
Hey {}, look at the Result ☝️

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://fastwin.app/LR?RG&C=3033148541

Register A new Account And Deposit 1000Rs and Use Our prediction To Make More Profits. 
    """
    
    # Fastwin Message 
    FUNWIN = """
✅ Welcome to FunWin Game🥳😎
━━━━━━━━━━━━━━━━━━━━━━
🔰Joining Bonus -: 20Rs
🔰Minimum Recharge -: 200Rs
🔰Minimum Withdrawal -: 530Rs 
🔰Withdraw timings -: 24hrs
🔰Per Refer -:238Rs🤩🤩
🔰Everyday Lucky Lifafa 10rs 😚
✨Invite More, Earn More!

▪️If you are new, join our official team link now.

✅FunWin Register Link:- https://bigmumbai.ink/#/register?invitationCode=787621083187
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which Funwin game prediction you want...👇
"""
    
    # Home Button
    funwinhome = [
        [InlineKeyboardButton(text="[► Return FunWin ◄]", callback_data="funwin")],
    ]
    
    # Home Button
    funwinhome_buttons = [
    [
        InlineKeyboardButton("[►Fastparity◄]", callback_data="funwinfastparity"),
        InlineKeyboardButton("[►Parity◄]", callback_data="funwinparity")
    ],   
        [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    
    # Home Button
    bdgbuttons = [
    [InlineKeyboardButton("[►Wingo 1 Minute◄]", callback_data="bdgwingo")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    # Home Button
    bmbuttons = [
    [InlineKeyboardButton("[►Wingo 1 Minute◄]", callback_data="bmwingo")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    # Home Button
    ggbuttons = [
    [InlineKeyboardButton("[►Wingo 1 Minute◄]", callback_data="ggwingo")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="goagame")],
    ]
    
    # Payment Button
    paymentbuttons = [
        [InlineKeyboardButton(text="[►Send Here Payment Screenshot◄]", url="t.me/+36Pm3qwJKjMwOGM1")],
        [InlineKeyboardButton(text="[►Premium Subscription◄]", callback_data="premium")],
    ]
    # QR
    qrbuttons = [
        [InlineKeyboardButton(text="[►Send Here Payment Screenshot◄]", url="t.me/+36Pm3qwJKjMwOGM1")],
    ]
    
    # Home Button
    paymenthome = [
    [InlineKeyboardButton(text="[►Payment Method◄]", callback_data="payment")],
    [InlineKeyboardButton(text="[► Return Home ◄]", callback_data="home")],
    ]
    
    # Home Button
    fastwinhome = [
        [InlineKeyboardButton(text="[► Return FastWin ◄]", callback_data="fastwin")],
   ]

    # All Game Prediction
    ALLGAME = """
If you want prediction of all games then first take premium subscription then play prediction of all games 24 hours, whenever you want.
"""
    GOAGAME = """
✅ Welcome to GoaGame Game🥳
━━━━━━━━━━━━━━━━━━━━━━
🔰Minimum Recharge -: 300Rs
🔰Minimum Withdrawal -: 110Rs 
🔰Withdraw timings -: 24hrs
✨Invite More, Earn More!

▪️If you are new, join our official team link now.

✅GoaGame Register Link:- https://goagame.com/#/register?invitationCode=275731115445
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which GoaGame game prediction you want...👇
"""
    GGRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://goagame.com/#/register?invitationCode=275731115445
"""
    BIGMUMBAI = """
✅ Welcome to Big Mumbai Game🥳😎
━━━━━━━━━━━━━━━━━━━━━━
🔰Minimum Recharge -: 300Rs
🔰Minimum Withdrawal -: 110Rs 
🔰Withdraw timings -: 24hrs
✨Invite More, Earn More!

▪️If you are new, join our official team link now.

✅BM Register Link:- https://www.bdggame.in/#/register?invitationCode=S4ewD527220
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which Big Mumbai game prediction you want...👇
"""
    BMRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://goagame.com/#/register?invitationCode=275731115445
"""
    BIGDADDYGAME = """
✅ Welcome to Big Daddy Game🥳😎
━━━━━━━━━━━━━━━━━━━━━━
🔰Minimum Recharge -: 300Rs
🔰Minimum Withdrawal -: 110Rs 
🔰Withdraw timings -: 24hrs
✨Invite More, Earn More!

▪️If you are new, join our official team link now.

✅BDG Register Link:- https://www.bdggame.in/#/register?invitationCode=S4ewD527
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which Big Daddy game prediction you want...👇
"""
    BDGRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://www.bdggame.in/#/register?invitationCode=S4ewD527
"""
    TCLOTTERY = """
    COMING SOON...
    """
    KGLOTTERY = """
    COMING SOON...
    """
    CLUB91 = """
✅ Welcome to 91 Club Game🥳😎
━━━━━━━━━━━━━━━━━━━━━━
🔰Minimum Recharge -: 300Rs
🔰Minimum Withdrawal -: 110Rs 
🔰Withdraw timings -: 24hrs
✨Invite More, Earn More!

▪️If you are new, join our official team link now.

✅ 91 Club Register Link:- https://91club-4.com/#/register?invitationCode=777284419608
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which 91 club game prediction you want...👇
"""
    C91RESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://91club-4.com/#/register?invitationCode=777284419608
"""
    RUMMYBLOC = """
✅ Welcome to Rummy Bloc Game🥳😎
━━━━━━━━━━━━━━━━━━━━━━
🔰Minimum Recharge -: 300Rs
🔰Recharge Bonis -: 300Rs
🔰Minimum Withdrawal -: 100Rs 
🔰Withdraw timings -: 24hrs
✨Invite More, Earn More!

▪️If you are new, join our official team link now.

✅Register Link:- https://rummybloc.in?from_gameid=9328965&channelCode=200000
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which Rummy Bloc game prediction you want...👇
"""
    RBRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://rummybloc.in?from_gameid=9328965&channelCode=200000
"""
    MANTRIMALL = """
✅ Welcome to Mantrimall Game🥳😎
━━━━━━━━━━━━━━━━━━━━━━
🔰Minimum Recharge -: 300Rs
🔰Minimum Withdrawal -: 200Rs 
🔰Per Refer -: 120Rs
🔰Withdraw timings -: 24hrs
✨Invite More, Earn More!

▪️If you are new, join our official team link now.

✅ Mantrimall Register Link:- https://www.bdggame.in/#/register?invitationCode=S4ewD527220
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which Mantrimall game prediction you want...👇
"""
    MMRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://goagame.com/#/register?invitationCode=275731115445
"""
    # Home Button
    allgamebuttons = [
    [
        InlineKeyboardButton("[►FastWin◄]", callback_data="fastwin"),
        InlineKeyboardButton("[►GoaGame◄]", callback_data="goagame"),
        InlineKeyboardButton("[►FunWin◄]", callback_data="funwin")
    ],
    [
        InlineKeyboardButton("[►Big-Mumbai◄]", callback_data="bigmumbai"),
        InlineKeyboardButton("[►Big-Daddy-Game◄]", callback_data="bigdaddygame")
    ],
    [
        InlineKeyboardButton("[►KG Lottery◄]", callback_data="kglottery"),
        InlineKeyboardButton("[►TC lottery◄]", callback_data="tclottery")
    ],
    [
        InlineKeyboardButton("[►91-Club◄]", callback_data="club91"),
        InlineKeyboardButton("[►RummyBloc◄]", callback_data="rummybloc")
    ],   
        [InlineKeyboardButton(text="[► Return Home ◄]", callback_data="home")],
    ]
