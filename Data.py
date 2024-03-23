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
        [InlineKeyboardButton("[►Get All Game Prediction◄]", url="https://t.me/PredictorAerobot?start=allgame")],
        [InlineKeyboardButton("[►Tech Earning◄]", url="https://t.me/TechEarning_KingMasterMind"),
        InlineKeyboardButton("[►Support Chat◄]", url="https://t.me/EarningTeamSupportChat")],
        [InlineKeyboardButton("[►Get Premium Subscription◄]", url="https://t.me/PredictorAerobot?start=premium")],
    ]
    # PM Start Buttons
    start_buttons = [
        [
        InlineKeyboardButton("[►Agent◄]", url="https://telegram.me/Awesome_Vrajesh"),
        InlineKeyboardButton("[►Developer◄]", url="https://telegram.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►About◄]", url="about")
        ],
        [InlineKeyboardButton("[►Get All Game Prediction◄]", callback_data="allgame")],
        [InlineKeyboardButton("[►Get Premium Subscription◄]", callback_data="premium")],
        [InlineKeyboardButton("[►Tech Earning◄]", url="https://t.me/TechEarning_KingMasterMind"),
         InlineKeyboardButton("[►Support Chat◄]", url="https://t.me/EarningTeamSupportChat")],
    ]
    # Premium Subscription Message 
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
    #QR Message 
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
★Support » @EarningTeamSupportChat
    """
    # About Buttons
    about_buttons = [
        [InlineKeyboardButton(text="[►Join our Groups or Channels◄]", callback_data="chat")],
        [InlineKeyboardButton(text="[►Return Home◄]", callback_data="home")],
    ] 
    CHAT = """
This is All our Groups or Channels≈[🇮🇳] 
━━━━━━━━━━━━━━━━━━━━━━
★Network » @AerodynamicV1Botz
★Developer » @AerodynamicV1_OFFICIAL
★Owner » @Awesome_Vrajesh
★Update » @AerodynamicV1_UPDATE
★Tech Earning » @TechEarning_KingMasterMind
★Support » @EarningTeamSupportChat
    """
    # All Game Message
    ALLGAME = """
If you want prediction of all games then first take premium subscription then play prediction of all games 24 hours, whenever you want.
"""
    # All Game Buttons
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
    [InlineKeyboardButton("[►Fastparity◄]", callback_data="fastwinfastparity"),
     InlineKeyboardButton("[►Parity◄]", callback_data="fastwinparity")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    # FastWin Back Button
    fastwin_back = [
        [InlineKeyboardButton(text="[►Return FastWin Game◄]", callback_data="fastwin")],
    ]
    # FastWin Games 
    FASTPARITY = """
Hey {},

I'm FastWin Fastparity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /fastparity command.

Example:- /fastparity792

Ask your doubts at @EarningTeamSupportChat.
   """
    FASTWINRESULT = """
Hey {}, look at the Result ☝️

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://fastwin.app/LR?RG&C=3033148541

Register A new Account And Deposit 1000Rs and Use Our prediction To Make More Profits. 
    """
    # FastWin Result Buttons
    fastwin_result_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►FastWin❔◄]", callback_data="fastwin")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    fastwin_group_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►FastWin❔◄]", url="https://t.me/PredictorAerobot?start=fastwin")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    PARITY = """
Hey {},

I'm FastWin Parity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /parity command.

Example:- /parity792

Ask your doubts at @EarningTeamSupportChat.
   """
    TOSS = """
Hey {},

I'm FastWin Parity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /parity command.

Example:- /parity792

Ask your doubts at @EarningTeamSupportChat.
   """
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
    # FunWin Back Button
    funwin_back = [
        [InlineKeyboardButton(text="[►Return FunWin Game◄]", callback_data="funwin")],
    ]
    FUNWINFASTPARITY = """
Hey {},

I'm FastWin Fastparity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /fastparity command.

Example:- /fastparity792

Ask your doubts at @EarningTeamSupportChat.
   """  
    FUNWINRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Ask your doubts at @EarningTeamSupportChat.
"""
    # FunWin Result Buttons
    funwin_result_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►FunWin❔◄]", callback_data="funwin")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    funwin_group_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►FunWin❔◄]", url="https://t.me/PredictorAerobot?start=funwin")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    FUNWINPARITY = """
Hey {},

I'm FunWin Parity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /funwinparity command.

Example:- /funwinparity986

Ask your doubts at @EarningTeamSupportChat.
   """
    FUNWINTOSS = """
Hey {},

I'm FumWin Toss {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /fumwintoss command.

Example:- /funwintoss987

Ask your doubts at @EarningTeamSupportChat.
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
    # GoaGame Button
    goagame_buttons = [
    [InlineKeyboardButton("[►Wingo 1 Minute◄]", callback_data="goagamewingo")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    # GoaGame Back Button
    goagame_back = [
        [InlineKeyboardButton(text="[►Return GoaGame◄]", callback_data="goagame")],
    ]
    GGWINGO = """
Hey {},

I'm GoaGame Wingo 1 Minute Game {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /GGwingo command.

Example:- /GGwingo792

Ask your doubts at @EarningTeamSupportChat.
"""
    GGRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://goagame.com/#/register?invitationCode=275731115445
"""
    # GoaGame Result Buttons
    goagame_result_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►GoaGame❔◄]", callback_data="goagame")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    goagame_group_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►GoaGame❔◄]", url="https://t.me/PredictorAerobot?start=goagame")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
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
    # Big Mumbai Button
    bigmumbai_buttons = [
    [InlineKeyboardButton("[►Wingo 1 Minute◄]", callback_data="bigmumbaiwingo")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    # Big Mumbai Back Button
    bigmumbai_back = [
        [InlineKeyboardButton(text="[►Return Big Mumbai Game◄]", callback_data="bigmumbai")],
    ]
    BMWINGO = """
Hey {},

I'm Big Mumbai Wingo 1 Minute Game {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /BMwingo command.

Example:- /BMwingo792

Ask your doubts at @EarningTeamSupportChat.
"""
    BMRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://bigmumbai.ink/#/register?invitationCode=787621083187
"""
    # Big Mumbai Result Buttons
    bigmumbai_result_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►BigMumbai❔◄]", callback_data="bigmumbai")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    bigmumbai_group_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►BigMumbai❔◄]", url="https://t.me/PredictorAerobot?start=bigmumbai")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    BDG = """
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
    # GoaGame Button
    bdg_buttons = [
    [InlineKeyboardButton("[►Wingo 1 Minute◄]", callback_data="bdgwingo")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    # FunWin Back Button
    bdg_back = [
        [InlineKeyboardButton(text="[►Return Big-Daddy-Game◄]", callback_data="bdg")],
    ]
    BDGWINGO = """
Hey {},

I'm Big Daddy Wingo 1 Minute Game {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /BDGwingo command.

Example:- /BDGwingo792

Ask your doubts at @EarningTeamSupportChat.
"""
    BDGRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://www.bdggame.in/#/register?invitationCode=S4ewD527
"""
    # BDG Result Buttons
    bdg_result_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►GoaGame❔◄]", callback_data="bdg")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    bdg_group_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►GoaGame❔◄]", url="https://t.me/PredictorAerobot?start=bdg")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    TCLOTTERY = """
    COMING SOON...
    """
    # TC Button
    tc_buttons = [
    [InlineKeyboardButton("[►Wingo 1 Minute◄]", callback_data="tcwingo")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    # TC Back Button
    tc_back = [
        [InlineKeyboardButton(text="[►Return TC Lottery Game◄]", callback_data="tc")],
    ]
    TCRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://goagame.com/#/register?invitationCode=275731115445
"""
    # TC Result Buttons
    tc_result_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►TC Lottery❔◄]", callback_data="tc")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    tc_group_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►TC Lottery❔◄]", url="https://t.me/PredictorAerobot?start=tc")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
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
    # tiranga Button
    tiranga_buttons = [
    [InlineKeyboardButton("[►Wingo 1 Minute◄]", callback_data="tirangawingo")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    # tiranga Back Button
    tiranga_back = [
        [InlineKeyboardButton(text="[►Return Tiranga Game◄]", callback_data="tiranga")],
    ]
    TIRANGAWINGO = """
Hey {},

I'm TIRANGA Wingo 1 Minute Game {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /TIRANGAwingo command.

Example:- /TIRANGAwingo792

Ask your doubts at @EarningTeamSupportChat.
"""
    TIRANGARESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://tirangalottery.in/#/register?invitationCode=14184791737
"""
    # tiranga Result Buttons
    tiranga_result_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►Tiranga❔◄]", callback_data="tiranga")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    tiranga_group_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►Tiranga❔◄]", url="https://t.me/PredictorAerobot?start=tiranga")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    KGLOTTERY = """
    COMING SOON...
    """
    91CLUB = """
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
    # 91club Button
    91club_buttons = [
    [InlineKeyboardButton("[►Wingo 1 Minute◄]", callback_data="91clubwingo")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    # 91club Back Button
    91club_back = [
        [InlineKeyboardButton(text="[►Return 91-Club Game◄]", callback_data="91club")],
    ]
    91CLUBRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://91club-4.com/#/register?invitationCode=777284419608
"""
    # 91club Result Buttons
    91club_result_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►91-Club❔◄]", callback_data="91club")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    91club_group_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►91-Club❔◄]", url="https://t.me/PredictorAerobot?start=91club")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    RUMMYBLOC = """
✅ Welcome to Rummy Bloc Game🥳😎
━━━━━━━━━━━━━━━━━━━━━━
🔰Minimum Recharge -: 300Rs
🔰Recharge Bonus -: 300Rs
🔰Minimum Withdrawal -: 100Rs 
🔰Withdraw timings -: 24hrs
✨Invite More, Earn More!

▪️If you are new, join our official team link now.

✅Register Link:- https://rummybloc.in?from_gameid=9328965&channelCode=200000
━━━━━━━━━━━━━━━━━━━━━━
🔰Click on the button below which Rummy Bloc game prediction you want...👇
"""
    # RummyBloc Button
    rummybloc_buttons = [
    [InlineKeyboardButton("[►DragonTigerFight◄]", callback_data="dragontigerfight"),
    InlineKeyboardButton("[►AndarBahar◄]", callback_data="andarbahar")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    # RummyBloc Back Button
    rummybloc_back = [
        [InlineKeyboardButton(text="[►Return RummyBloc Game◄]", callback_data="rummybloc")],
    ]
    ANDARBAHAR = """
Hey {},

I'm RummyBloc AndarBahar {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /RummyBlocAB command.

Example:- /RummyBlocAB

Ask your doubts at @EarningTeamSupportChat.
   """
    DRAGONTIGERFIGHT = """
Hey {},

I'm RummyBloc DragonTigerFight {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /RummyBlocDTF command.

Example:- /RummyBlocDTF

Ask your doubts at @EarningTeamSupportChat.
   """
    RUMMYBLOCRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 5-7 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Ask your doubts at @EarningTeamSupportChat.
"""
    # RummyBloc Result Buttons
    rummybloc_result_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►RummyBloc❔◄]", callback_data="rummybloc")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    rummybloc_group_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►RummyBloc❔◄]", url="https://t.me/PredictorAerobot?start=rummybloc")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
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
    # Mantrimall Button
    mantrimall_buttons = [
    [InlineKeyboardButton("[►Parity 3 Minute◄]", callback_data="mantrimallparity")],   
    [InlineKeyboardButton(text="[►Return All Games◄]", callback_data="allgame")],
    ]
    # Mantrimall Back Button
    mantrimall_back = [
        [InlineKeyboardButton(text="[►Return MantriMall Game◄]", callback_data="mantrimall")],
    ]
    MANTRIMALLPARITY = """
Hey {},

I'm Mantrimall Parity {} to get 24 hour prediction 

Enter the last 3 digits of the period number with the /MMparity command.

Example:- /MMparity986

Ask your doubts at @EarningTeamSupportChat.
"""
    MANTRIMALLRESULT = """
Hey {}, look at the Result ☝️

🔥Prepare your fund for 7-9 level management to avoid losses.
✨When you take Risks and push yourself, you do well ✓.

Make Sure To register Your new  Account With Our Special Link To Get Accurate Prediction 
 
Special Link - https://mantrishop.com/#/pages/person/register?r_code=3382608
"""
    # Mantrimall Result Buttons
    mantrimall_result_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►MantriMall❔◄]", callback_data="mantrimall")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
    mantrimall_group_buttons = [
       [InlineKeyboardButton("[►Developer◄]", url="https://t.me/AerodynamicV1_Official"),
        InlineKeyboardButton("[►MantriMall❔◄]", url="https://t.me/PredictorAerobot?start=mantrimall")],
       [InlineKeyboardButton("[►Support💬◄]", url="https://t.me/EarningTeamSupportChat"),
        InlineKeyboardButton("[►Tech Earning🔔◄]", url="https://t.me/TechEarning_KingMasterMind")]
    ]
