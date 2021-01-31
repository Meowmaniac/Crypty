import telebot
from bottoken import TOKEN

bot = telebot.TeleBot(TOKEN)

# welcome message
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "I am Crypty. Nice to meet you, " + str(message.from_user.first_name))

# recieving message
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.from_user.id, 'Hello!')
    else:
        bot.send_message(message.from_user.id, "Sorry, I don't understand you :(")

# starting bot
bot.polling(none_stop=True)
