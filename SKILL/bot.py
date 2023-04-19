import telebot
import extensions

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help_command(message):
    text = "Для начала работы введите команду в формате:\n<имя валюты> <в какую валюту перевести> <количество переводимой валюты>\nДля получения списка доступных валют введите /values."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values_command(message):
    text = "Доступные валюты:\nUSD - доллар США\nEUR - евро\nRUB - российский рубль"
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        base, quote, amount = message.text.split(' ')
        result = extensions.Converter.get_price(base.upper(), quote.upper(), amount)
    except extensions.APIException as e:
        bot.send_message(message.chat.id, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Не удалось обработать запрос\n{e}')
    else:
        text = f'{amount} {base.upper()} = {result} {quote.upper()}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
