import telebot

bot = telebot.TeleBot('1142444591:AAEHPDFYm6s3RHnSjxgYWZ9TTl0Ojm4OvGQ')




@bot.message_handler(content_types=['text'])
def send_message(message):
  if message.text == "Привет":
    bot.send_message(message.chat.id, "Привет")
  elif message.text == "Пока":
     bot.send_message(message.chat.id, "Пока")
bot.polling(none_stop=True, interval=0)

