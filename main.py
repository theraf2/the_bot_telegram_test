import telebot


bot = telebot.TeleBot("6689470725:AAHmBYeY-g3Hbh1m_AzGgED64RaqFVXr_Vg")


@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, "مرحبا عزيزي انا بوت تجريبي خاص براف")

bot.polling()