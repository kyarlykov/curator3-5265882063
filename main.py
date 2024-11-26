import telebot

bot = telebot.TeleBot("7830398777:AAEr95QR9Vj7-E_uxa2kof0afQc3LgdhhtQ")


# обработка команды
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здоровки!', parse_mode='Markdown')


@bot.message_handler(commands=['neuronet'])
def botok(message):
    bot.send_message(message.chat.id, '[*Нейросеть*](https://rugpt.io/nejroset-dlya-napisaniya-teksta)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['course'])
def mybot(message):
    bot.send_message(message.chat.id, '[*Курс*](https://umschool.net/)', parse_mode='Markdown')


@bot.message_handler(commands=['photomath'])
def main1(message):
    bot.send_message(message.chat.id, '[*Фотомач*](https://photomath.ru/)', parse_mode='Markdown')


@bot.message_handler(commands=['diary'])
def main2(message):
    bot.send_message(message.chat.id, '[*Дневник*](https://dnevnik.egov66.ru/login/)', parse_mode='Markdown')


bot.infinity_polling()