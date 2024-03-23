from pyrogram.types import InlineKeyboardButton

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

     # Group Start Button
    start_group_buttons = [
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

    # PM Start Buttons
    start_pm_buttons = [
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
    #QR Button
    qr_buttons = [
        [InlineKeyboardButton(text="[►Send Here Payment Screenshot◄]", url="t.me/+36Pm3qwJKjMwOGM1")],
    ]
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
    # Payment Buttons
    payment_buttons = [
        [InlineKeyboardButton(text="[►Send Here Payment Screenshot◄]", url="t.me/+36Pm3qwJKjMwOGM1")],
        [InlineKeyboardButton(text="[►Premium Subscription◄]", callback_data="premium")],
    ] 
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
    # Premium Button
    premium_buttons = [
    [InlineKeyboardButton(text="[►Payment Method◄]", callback_data="payment")],
    [InlineKeyboardButton(text="[► Return Home ◄]", callback_data="home")],
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
    TIRANGAWINGO = """
Hey {},

I'm TIRANGA Wingo 1 Minute Game {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /TIRANGAwingo command.

Example:- /TIRANGAwingo792

Ask your doubts at @EarningTeamSupportChat.
"""
    # parity Message



    # Fastwin Buttons
    gggbuttons = [
        [
            InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
            InlineKeyboardButton("[►GoaGame❔◄]", url="goagame")
        ],
        [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    tirangabuttons = [
        [
            InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
            InlineKeyboardButton("[►Tiranga❔◄]", callback_data="tiranga")
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
    # FastWin Button
    fastwin_buttons = [
    [
        InlineKeyboardButton("[►Fastparity◄]", callback_data="fastwinfastparity"),
        InlineKeyboardButton("[►Parity◄]", callback_data="fastwinparity")
    ],   
        [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]

    # FastWin Games 
    FASTPARITY = """
Hey {},

I'm FastWin Fastparity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /fastparity command.

Example:- /fastparity792

Ask your doubts at @EarningTeamSupportChat.
   """
    FASTPARITYRESULT = """
Hey {}, look at the Result ☝️

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://fastwin.app/LR?RG&C=3033148541

Register A new Account And Deposit 1000Rs and Use Our prediction To Make More Profits. 
    """
    PARITY = """
Hey {},

I'm FastWin Parity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /parity command.

Example:- /parity792

Ask your doubts at @EarningTeamSupportChat.
   """
    PARITYRESULT = """
Hey {}, look at the Result ☝️

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://fastwin.app/LR?RG&C=3033148541

Register A new Account And Deposit 1000Rs and Use Our prediction To Make More Profits. 
    """
    TOSS = """
Hey {},

I'm FastWin Parity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /parity command.

Example:- /parity792

Ask your doubts at @EarningTeamSupportChat.
   """
    TOSSRESULT = """
Hey {}, look at the Result ☝️

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://fastwin.app/LR?RG&C=3033148541

Register A new Account And Deposit 1000Rs and Use Our prediction To Make More Profits. 
    """

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
    
    # FunWin Message 
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
First read the rules & regulations then create your Funwin account.
[FunWin Rules & Regulations](https://t.me/FunWin_Game_Prediction/114)
━━━━━━━━━━━━━━━━━━━━━━
▪️If you are new, join our official team link now.

✅FunWin Register Link:- https://bigmumbai.ink/#/register?invitationCode=787621083187
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which Funwin game prediction you want...👇
"""
    # FunWin Button
    funwin_buttons = [
    [InlineKeyboardButton(tect="[►Fastparity◄]", callback_data="funwinfastparity"),
     InlineKeyboardButton(text="[►Parity◄]", callback_data="funwinparity")],
    [InlineKeyboardButton(text="[►Rules & Regulation of FunWin Game◄]", url="https://t.me/FunWin_Game_Prediction/114")],
    [InlineKeyboardButton(text="[►Official Forcast Channel◄]", url="https://t.me/FunWin_Official_Predictionz")],
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    FUNWINFASTPARITY = """
Hey {},

I'm FastWin Fastparity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /fastparity command.

Example:- /fastparity792

Ask your doubts at @EarningTeamSupportChat.
   """
    
    FUNWINFASTPARITYRESULT = """
Hey {}, look at the Result ☝️

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://fastwin.app/LR?RG&C=3033148541

Register A new Account And Deposit 1000Rs and Use Our prediction To Make More Profits. 
    """
    FUNWINPARITY = """
Hey {},

I'm FastWin Parity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /parity command.

Example:- /parity792

Ask your doubts at @EarningTeamSupportChat.
   """
    FUNWINPARITYRESULT = """
Hey {}, look at the Result ☝️

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://fastwin.app/LR?RG&C=3033148541

Register A new Account And Deposit 1000Rs and Use Our prediction To Make More Profits. 
    """
    FUNWINTOSS = """
Hey {},

I'm FastWin Fastparity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /fastparity command.

Example:- /fastparity792

Ask your doubts at @EarningTeamSupportChat.
   """
    FUNWINTOSSRESULT = """
Hey {}, look at the Result ☝️

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://fastwin.app/LR?RG&C=3033148541

Register A new Account And Deposit 1000Rs & Use Our prediction To Make More Profits. 
    """
    
    # Home Button
    funwinhome = [
        [InlineKeyboardButton(text="[► Return FunWin ◄]", callback_data="funwin")],
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

    # Home Button
    fastwinhome = [
        [InlineKeyboardButton(text="[► Return FastWin ◄]", callback_data="fastwin")],
   ]
    tirangaback = [
        [InlineKeyboardButton(text="[► Return Tiranga ◄]", callback_data="tiranga")],
    ]
    goagameback = [
        [InlineKeyboardButton(text="[► Return GoaGame ◄]", callback_data="goagame")],
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

✅BM Register Link:- https://bigmumbai.ink/#/register?invitationCode=787621083187
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which Big Mumbai game prediction you want...👇
"""
    BMRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://bigmumbai.ink/#/register?invitationCode=787621083187
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
    TCRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://goagame.com/#/register?invitationCode=275731115445
"""
    TIRANGA = """
✅ Welcome to Tiranga Game🥳😎
━━━━━━━━━━━━━━━━━━━━━━
🔰Minimum Recharge -: 300Rs
🔰Minimum Withdrawal -: 110Rs 
🔰Withdraw timings -: 24hrs
✨Invite More, Earn More!

▪️If you are new, join our official team link now.

✅ Tiranga Register Link:- https://tirangalottery.in/#/register?invitationCode=14184791737
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which tiranga game prediction you want...👇
"""
    TIRANGARESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://tirangalottery.in/#/register?invitationCode=14184791737
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

✅ Mantrimall Register Link:- https://mantrishop.com/#/pages/person/register?r_code=3382608
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which Mantrimall game prediction you want...👇
"""
    MMRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://mantrishop.com/#/pages/person/register?r_code=3382608
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
        InlineKeyboardButton("[►Tiranga◄]", callback_data="tiranga"),
        InlineKeyboardButton("[►TC lottery◄]", callback_data="tclottery")
    ],
    [
        InlineKeyboardButton("[►91-Club◄]", callback_data="club91"),
        InlineKeyboardButton("[►Mantrimall◄]", callback_data="mantrimall"),
        InlineKeyboardButton("[►RummyBloc◄]", callback_data="rummybloc")
    ],   
        [InlineKeyboardButton(text="[► Return Home ◄]", callback_data="home")],
    ]
