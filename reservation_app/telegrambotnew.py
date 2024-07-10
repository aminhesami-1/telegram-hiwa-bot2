from random import randint
import logging
from reservation_script import  set_reservation_time , check_user_reservation_time , show_r_data
from telegram import (
    
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    InputMediaAudio,MenuButton, MenuButtonCommands, MenuButtonWebApp, MenuButtonDefault
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    filters,
)
import time
import asyncio
from data import (
    list2,
    start_text,
    kid_and_adult_dis,
    caption_voice,
    kid_and_adult_dis2,
    caption_voice2,
    Darbare,
    ReservedTime
)
import sys
from my_script import *

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keys = [
        [
            InlineKeyboardButton(text="بزرگسالان(16 به بالا)", callback_data="1"),
            InlineKeyboardButton(text="کودکان و نوجوانان(6تا 16)", callback_data="2"),
        ],
        [InlineKeyboardButton(text="سوالات متداول", callback_data="3")],
        [InlineKeyboardButton(text="درباره مدرسه دودکانی", callback_data="4")],
        [InlineKeyboardButton(text="مشاوره حضوری رایگان", callback_data="moshavere")],
    ]
    markup = InlineKeyboardMarkup(keys)
    media = InputMediaPhoto(media=open("doodkani_photo\DSC00279.jpg", "rb"))
    if update.effective_message.text == "/start":

        photo = await context.bot.send_photo(
            chat_id=update.effective_chat.id, photo="doodkani_photo\DSC00279.jpg"
        )
        await context.bot.edit_message_caption(
            chat_id=update.effective_chat.id, caption=start_text, message_id=photo.id
        )
        await context.bot.edit_message_reply_markup(
            chat_id=update.effective_chat.id, message_id=photo.id, reply_markup=markup
        )
    else:

        photo = await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.id,
            media=media,
        )
        await context.bot.edit_message_caption(
            chat_id=update.effective_chat.id,
            caption=start_text,
            message_id=photo.id,
            reply_markup=markup,
        )
        await context.bot.edit_message_reply_markup(
            chat_id=update.effective_chat.id, message_id=photo.id, reply_markup=markup
        )


async def myq(key: str, update: Update, context: ContextTypes.DEFAULT_TYPE):
    x = list2.get(key)
    keys = [[InlineKeyboardButton(text="بازگشت", callback_data="qback")]]
    markup = InlineKeyboardMarkup(keys)
    media = InputMediaPhoto(
        media=open("doodkani_photo/photo_12_2024-06-08_18-33-42.jpg", "rb")
    )
    photo = await context.bot.edit_message_media(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.id,
        media=media,
    )
    await context.bot.edit_message_caption(
        chat_id=update.effective_chat.id,
        caption=f"\n {x[1]}حواب سوال",
        message_id=photo.id,
    )
    await context.bot.edit_message_reply_markup(
        chat_id=update.effective_chat.id, message_id=photo.id, reply_markup=markup
    )


async def question(qlist, update: Update, context: ContextTypes.DEFAULT_TYPE):
    main_text = ""
    keys = []
    row = []

    for i, (k, v) in enumerate(qlist.items()):
        main_text += str(i + 1) + "-" + v[0] + "\n\n"

        button = InlineKeyboardButton(text=k.replace("q", ""), callback_data=k)
        row.append(button)
        if (i + 1) % 4 == 0:
            keys.append(row)
            row = []
    media = InputMediaPhoto(
        media=open("doodkani_photo/photo_11_2024-06-08_18-33-42.jpg", "rb")
    )
    photo = await context.bot.edit_message_media(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.id,
        media=media,
    )
    await context.bot.edit_message_caption(
        chat_id=update.effective_chat.id, caption=main_text, message_id=photo.id
    )
    if row:
        keys.append(row)

    keys.append([InlineKeyboardButton(callback_data="back", text="بازگشت")])
    markup = InlineKeyboardMarkup(keys)
    await context.bot.edit_message_reply_markup(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.id,
        reply_markup=markup,
    )


async def adult(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keys = [
        [
            InlineKeyboardButton(
                text="دوره فول استک ۸ ماهه طراحی سایت", callback_data="fullstack"
            )
        ],
        [
            InlineKeyboardButton(
                text="دوره طراحی سایت با وردپرس بدون کدنویسی", callback_data="wordpress"
            )
        ],
        [InlineKeyboardButton(text="دوره سئو و بهینه سازی سایت", callback_data="seo")],
        [
            InlineKeyboardButton(
                text="دوره آموزشی ادمینی حرفه ای اینستاگرام", callback_data="instagram"
            )
        ],
        [InlineKeyboardButton(text="بازگشت", callback_data="back")],
    ]
    markup = InlineKeyboardMarkup(keys)
    media = InputMediaPhoto(
        media=open("doodkani_photo/photo_10_2024-06-08_18-33-42.jpg", "rb")
    )
    photo = await context.bot.edit_message_media(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.id,
        media=media,
    )
    await context.bot.edit_message_caption(
        chat_id=update.effective_chat.id,
        message_id=photo.id,
        caption="برای دریافت اطلاعات مربوط به حوزه مورد نظر خود کلیک کنید",
    )
    await context.bot.edit_message_reply_markup(
        chat_id=update.effective_chat.id, message_id=photo.id, reply_markup=markup
    )


async def kids(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keys = keys = [
        [
            InlineKeyboardButton(text="6 تا 7 سال", callback_data="6-7"),
            InlineKeyboardButton(text=" بالای 8 سال ", callback_data="8+"),
        ],
        [InlineKeyboardButton(text="بازگشت", callback_data="back")],
    ]
    markup = InlineKeyboardMarkup(keys)
    media = InputMediaPhoto(
        media=open("doodkani_photo/photo_9_2024-06-08_18-33-42.jpg", "rb")
    )
    photo = await context.bot.edit_message_media(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.id,
        media=media,
    )
    await context.bot.edit_message_caption(
        chat_id=update.effective_chat.id,
        message_id=photo.id,
        caption="سن فرزند خود را وارد کنید",
    )
    await context.bot.edit_message_reply_markup(
        chat_id=update.effective_chat.id, message_id=photo.id, reply_markup=markup
    )


async def vkids(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keys = keys = [
        [
            InlineKeyboardButton(text="6 تا 7 سال", callback_data="6-7"),
            InlineKeyboardButton(text=" بالای 8 سال ", callback_data="8+"),
        ],
        [InlineKeyboardButton(text="بازگشت", callback_data="back")],
    ]
    markup = InlineKeyboardMarkup(keys)
    ###++++++++++++++++++++++++++++++++++++

    photo = await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="doodkani_photo/photo_8_2024-06-08_18-33-42.jpg",
    )
    await context.bot.edit_message_caption(
        chat_id=update.effective_chat.id,
        caption="سن فرزند خود را وارد کنید",
        message_id=photo.id,
    )
    await context.bot.edit_message_reply_markup(
        chat_id=update.effective_chat.id, message_id=photo.id, reply_markup=markup
    )


async def vadult(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keys = [
        [
            InlineKeyboardButton(
                text="دوره فول استک ۸ ماهه طراحی سایت", callback_data="fullstack"
            )
        ],
        [
            InlineKeyboardButton(
                text="دوره طراحی سایت با وردپرس بدون کدنویسی", callback_data="wordpress"
            )
        ],
        [InlineKeyboardButton(text="دوره سئو و بهینه سازی سایت", callback_data="seo")],
        [
            InlineKeyboardButton(
                text="دوره آموزشی ادمینی حرفه ای اینستاگرام", callback_data="instagram"
            )
        ],
        [InlineKeyboardButton(text="بازگشت", callback_data="back")],
    ]
    markup = InlineKeyboardMarkup(keys)
    ###++++++++++++++++++++++++++++++++++++

    photo = await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="doodkani_photo/photo_7_2024-06-08_18-33-42.jpg",
    )
    await context.bot.edit_message_caption(
        chat_id=update.effective_chat.id,
        caption="برای دریافت اطلاعات مربوط به حوزه مورد نظر خود کلیک کنید",
        message_id=photo.id,
    )
    await context.bot.edit_message_reply_markup(
        chat_id=update.effective_chat.id, message_id=photo.id, reply_markup=markup
    )

######======================================------ Reservation Script ------==================================#####
                                                                                                                  



###=========================================----- RESERVATIONS-TIME -----====================================###

async def ReservationsTime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = await show_r_data()
    

    keys = []
    
    async for item in data :
        keys.append([InlineKeyboardButton(text=f"{item.check_in}", callback_data=f"{item.id}ReservationTime")])
    markup = InlineKeyboardMarkup(keys)
        
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=ReservedTime,
            
            reply_markup=markup,
        )
    




NAME, AGE, NUMBER, SHOW,V_CODE , VERIFY  = range(6)


async def Reservation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.effective_user.id

    is_user_verifyed = await is_user_verify(user_id)
    is_user_id_seted = await is_user_id_set(user_id)

    if is_user_id_seted :
            if is_user_verifyed:
                await ReservationsTime(update , context)
                return ConversationHandler.END
            else : 
                await update.message.reply_text(
                "برای ثبت وقت مشاوره به سوالات زیر جواب دهید"
                "برای لغو درخواست /cancel را وارد کنید.\n\n"
                "نام و نام خانوادگی فرزند خود را وارد کنید؟",
            )
                return NAME
    else :
            keys = keys = [[InlineKeyboardButton(text="بازگشت", callback_data="back")]]
            markup = InlineKeyboardMarkup(keys)
            await set_user_id(user_id)
            await update.message.reply_text(
                "برای ثبت وقت مشاوره به سوالات زیر جواب دهید"
                "برای لغو درخواست /cancel را وارد کنید.\n\n"
                "نام و نام خانوادگی فرزند خود را وارد کنید؟",
            )
            return NAME

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.effective_user.id
    Name = update.message.text
    await set_user_name(user_id=user_id, name=Name)
    user = update.message.from_user
    await update.message.reply_text(
        "نام فرزند شما سیو شد, %s! سن فرزند خود را وارد کنید؟" % update.message.text,
        reply_markup=ReplyKeyboardRemove(),
    )
    return AGE


async def age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    age = update.message.text
    user_id = update.effective_user.id
    await set_user_age(user_id, age=age)

    await update.message.reply_text(
        f"سن فرزند شما ذخیره شد شماره موبایل خود را وارد کنید  !"
    )

    return NUMBER


async def number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    number = update.message.text
    user_id = update.effective_user.id
    await set_user_number(user_id=user_id, number=number)
    
    data = await show_user_data(user_id=user_id)

    await update.message.reply_text(
        f"""نام شما :  {data[0]} \t 
سن شما : {data[1]}  \t
شماره موبایل شما: {data[2]} \t \n برای تایید کلمه تایید را ارسال کنید و برای بغو کلمه بغو""".replace(
            "(", " "
        ).replace(
            ")", " "
        ),

    )

    return V_CODE


async def my_v_code(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.effective_message.text == "تایید":
        v_code = randint(100000 , 999999)
        user_id = update.effective_user.id
        await V_code(user_id , v_code)
        await update.message.reply_text(
            text= 'we send a v_code to use'
        )
        return VERIFY
    elif update.effective_message.text == "لغو":
        await delete_user_data(user_id)
        await update.message.reply_text(
            text="info deleted try again❌ /Reservation",
        )
        return ConversationHandler.END



async def verify(update : Update , contex: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.id
    v_code = update.effective_message.text
    is_true = await check_v_code(user , v_code)
    if is_true:
        await contex.bot.send_message(chat_id=update.effective_chat.id , text='your in')
    else : 
        await delete_user_data(user)
        await contex.bot.send_message(chat_id=update.effective_chat.id , text='your code is wrong try again')

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    user = update.message.from_user
    await update.message.reply_text(
        "وقت مشاوره شما ثبت شد.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


async def call_back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    callback_data = update.callback_query.data
    if callback_data == "1":
        await adult(update, context)
    elif callback_data == "2":
        await kids(update, context)
    elif callback_data == "3":
        # all_question = await get_questions()?
        await question(list2, update, context)
    elif callback_data == "4":
        keys = [[InlineKeyboardButton(text="بازگشت", callback_data="back")]]
        markup = InlineKeyboardMarkup(keys)
        media = InputMediaPhoto(
            media=open("doodkani_photo/photo_6_2024-06-08_18-33-42.jpg", "rb")
        )
        photo = await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            media=media,
            message_id=update.effective_message.id,
        )
        await context.bot.edit_message_caption(
            chat_id=update.effective_chat.id, caption=Darbare, message_id=photo.id
            
        )
        await context.bot.edit_message_reply_markup(
            chat_id=update.effective_chat.id, message_id=photo.id, reply_markup=markup
        )
    elif callback_data == 'moshavere':
        await context.bot.send_message(chat_id=update.effective_chat.id, text='برای مشاوره رایگان کلیک کنید \n /Reservation')
        
    if callback_data == "6-7":
        keys = [
            [
                InlineKeyboardButton(
                    text="توضیحات به صورت ویس", callback_data="6-7voice"
                ),
                InlineKeyboardButton(
                    text="توضیحات به صورت متن", callback_data="6-7text"
                ),
            ],
            [InlineKeyboardButton(text="بازگشت", callback_data="kback")],
        ]
        markup = InlineKeyboardMarkup(keys)
        media = InputMediaPhoto(
            media=open("doodkani_photo/photo_5_2024-06-08_18-33-42.jpg", "rb")
        )
        photo = await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            media=media,
            message_id=update.effective_message.id,
        )
        await context.bot.edit_message_caption(
            chat_id=update.effective_chat.id,
            caption=kid_and_adult_dis2,
            message_id=photo.id,
        )
        await context.bot.edit_message_reply_markup(
            chat_id=update.effective_chat.id, message_id=photo.id, reply_markup=markup
        )

    elif callback_data == "8+":
        keys = [
            [
                InlineKeyboardButton(
                    text="توضیحات به صورت ویس", callback_data="8+voice"
                ),
                InlineKeyboardButton(
                    text="توضیحات به صورت متن", callback_data="8+text"
                ),
            ],
            [InlineKeyboardButton(text="بازگشت", callback_data="kback")],
        ]
        markup = InlineKeyboardMarkup(keys)
        media = InputMediaPhoto(
            media=open("doodkani_photo/photo_4_2024-06-08_18-33-42.jpg", "rb")
        )
        photo = await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            media=media,
            message_id=update.effective_message.id,
        )
        await context.bot.edit_message_caption(
            chat_id=update.effective_chat.id,
            caption=kid_and_adult_dis,
            message_id=photo.id,
        )
        await context.bot.edit_message_reply_markup(
            chat_id=update.effective_chat.id, message_id=photo.id, reply_markup=markup
        )

    if callback_data == "back":
        await start(update, context)
    if "q" in callback_data:
        for i in range(len(list2)):
            if callback_data == f"q{i+1}":
                await myq(callback_data, update, context)
            else:
                pass
        if callback_data == "qback":
            await question(list2, update, context)
    if callback_data == "kback":
        await kids(update, context)
    if callback_data == "vkback":
        await vkids(update, context)

    if callback_data == "8+text":

        keys = [[InlineKeyboardButton(text="بازگشت", callback_data="kback")]]
        markup = InlineKeyboardMarkup(keys)
        media = InputMediaPhoto(
            media=open("doodkani_photo/photo_3_2024-06-08_18-33-42.jpg", "rb")
        )
        photo = await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            media=media,
            message_id=update.effective_message.id,
        )
        await context.bot.edit_message_caption(
            chat_id=update.effective_chat.id,
            caption=kid_and_adult_dis,
            message_id=photo.id,
        )
        await context.bot.edit_message_reply_markup(
            chat_id=update.effective_chat.id, reply_markup=markup, message_id=photo.id
        )
    if callback_data == "8+voice":
        await context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=update.effective_message.id
        )
        audioo = InputMediaAudio(
            media=open("doodkani_voice\methood.ogg", "rb"),
            caption=caption_voice,
        )

        keys = [[InlineKeyboardButton(text="بازگشت", callback_data="vkback")]]
        markup = InlineKeyboardMarkup(keys)
        with open("doodkani_voice/ahamiat.ogg", "rb") as f:
            voice = await context.bot.send_audio(
                chat_id=update.effective_chat.id, audio=f, caption=caption_voice
            )
        await context.bot.edit_message_reply_markup(
            chat_id=update.effective_chat.id, message_id=voice.id, reply_markup=markup
        )
    if callback_data == "False":
        await delete_user_data(user_id)
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.id,
            text="info deleted try again❌ /Reservation",
        )
    if callback_data == "True":
        v_code = randint(100000 , 999999)
        user_id = update.effective_user.id
        await V_code(user_id , v_code)
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.id,
            text= 'we send a v_code to use'
        )
        return VERIFY
    




    ###===============================================================================================================================================================================#
    if callback_data == "6-7text":

        keys = [[InlineKeyboardButton(text="بازگشت", callback_data="kback")]]
        markup = InlineKeyboardMarkup(keys)
        media = InputMediaPhoto(
            media=open("doodkani_photo/photo_2_2024-06-08_18-33-42.jpg", "rb")
        )
        photo = await context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            media=media,
            message_id=update.effective_message.id,
        )
        await context.bot.edit_message_caption(
            chat_id=update.effective_chat.id,
            caption=kid_and_adult_dis2,
            message_id=photo.id,
        )
        await context.bot.edit_message_reply_markup(
            chat_id=update.effective_chat.id, reply_markup=markup, message_id=photo.id
        )

    if callback_data == "6-7voice":
        keys = [[InlineKeyboardButton(text="بازگشت", callback_data="vkback")]]
        markup = InlineKeyboardMarkup(keys)
        await context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=update.effective_message.id
        )

        with open("doodkani_voice/method.ogg", "rb") as f:
            voice = await context.bot.send_audio(
                chat_id=update.effective_chat.id, audio=f, caption=caption_voice2
            )
            await context.bot.edit_message_reply_markup(
                chat_id=update.effective_chat.id,
                message_id=voice.id,
                reply_markup=markup,
            )
    if callback_data == "fullstack":
        keys = [[InlineKeyboardButton(text="بازگشت", callback_data="adult-back")]]
        markup = InlineKeyboardMarkup(keys)
        await context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=update.effective_message.id
        )
        with open("doodkani_voice/fullstack.ogg", "rb") as f:
            voice = await context.bot.send_audio(
                chat_id=update.effective_chat.id,
                audio=f,
                caption="توضیحات مربوط به دوره fullstack به صورت ویس",
            )
            await context.bot.edit_message_reply_markup(
                chat_id=update.effective_chat.id,
                message_id=voice.id,
                reply_markup=markup,
            )
    if callback_data == "seo":
        keys = [[InlineKeyboardButton(text="بازگشت", callback_data="adult-back")]]
        markup = InlineKeyboardMarkup(keys)
        await context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=update.effective_message.id
        )
        with open("doodkani_voice/seo.ogg", "rb") as f:
            voice = await context.bot.send_audio(
                chat_id=update.effective_chat.id,
                audio=f,
                caption="توضیحات مربوط به دوره wordpress به صورت ویس",
            )
            await context.bot.edit_message_reply_markup(
                chat_id=update.effective_chat.id,
                message_id=voice.id,
                reply_markup=markup,
            )
    if callback_data == "wordpress":
        keys = [[InlineKeyboardButton(text="بازگشت", callback_data="adult-back")]]
        markup = InlineKeyboardMarkup(keys)
        await context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=update.effective_message.id
        )
        with open("doodkani_voice/wordpress.ogg", "rb") as f:
            voice = await context.bot.send_audio(
                chat_id=update.effective_chat.id,
                audio=f,
                caption="توضیحات در مورد دوره وردپرس به صورت ویس",
            )
            await context.bot.edit_message_reply_markup(
                chat_id=update.effective_chat.id,
                message_id=voice.id,
                reply_markup=markup,
            )
    if callback_data == "instagram":
        keys = [[InlineKeyboardButton(text="بازگشت", callback_data="adult-back")]]
        markup = InlineKeyboardMarkup(keys)
        await context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=update.effective_message.id
        )
        with open("doodkani_voice/instagram.ogg", "rb") as f:
            voice = await context.bot.send_audio(
                chat_id=update.effective_chat.id,
                audio=f,
                caption=" توضیحات در مورد دوره اینستاگرام به صورت وی",
            )
            await context.bot.edit_message_reply_markup(
                chat_id=update.effective_chat.id,
                message_id=voice.id,
                reply_markup=markup,
            )

    if callback_data == "adult-back":
        await vadult(update, context)
    if 'ReservationTime' in callback_data :
        user_id = update._effective_user.id
        Reservation_id = callback_data.replace('ReservationTime' , '')
        if await check_user_reservation_time(user_id=user_id):
            await context.bot.send_message(chat_id=update.effective_chat.id , text='fuck off your in ')
        else :
            await set_reservation_time(user_id , Reservation_id)
            await context.bot.send_message(text=f'', chat_id=update.effective_chat.id)


if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token("7435936193:AAHWbaX-DRQfYIdlwKA0JPDgB_mqaj8xMWY")
        .build()
    )
    start_handler = CommandHandler("start", start)
    ReservationHandler_handler =CommandHandler('ReservationsTime',ReservationsTime)
    call_back_handler = CallbackQueryHandler(call_back)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("Reservation", Reservation)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, age)],
            NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, number)],
            V_CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, my_v_code)],
            VERIFY : [MessageHandler(filters.TEXT & ~filters.COMMAND, verify)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    application.add_handler(start_handler)
    application.add_handler(call_back_handler)

    application.run_polling()
