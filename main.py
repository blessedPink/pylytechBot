import telebot
bot = telebot.TeleBot('1871612634:AAGbcCXieSCeGP__N4e1lqpBE_RGFxIK9gY')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
##try to image that its no shlakocode

bot.polling(none_stop=True, interval=0)
