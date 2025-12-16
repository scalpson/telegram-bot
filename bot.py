# -*- coding: utf-8 -*-
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import os
import os
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# منو اصلی
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("ثبت نام", callback_data='register')],
        [InlineKeyboardButton("پلن‌ها", callback_data='plans')],
        [InlineKeyboardButton("ویدیو آموزش", callback_data='video')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # حتماً از await استفاده شود
    await update.message.reply_text('به ربات معامله گر خوش آمدید!', reply_markup=reply_markup)

# هندلر Callback
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'register':
        await query.edit_message_text(text="لطفاً نام و نام خانوادگی خود را وارد کنید:")
    elif query.data == 'plans':
        await query.edit_message_text(text="لیست پلن‌ها: ماهانه، 3 ماهه، سالانه")
    elif query.data == 'video':
        await query.edit_message_text(text="ویدیو آموزش در حال حاضر آماده نیست.")

# اجرای ربات
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    
    print("Bot is running...")
    app.run_polling()
