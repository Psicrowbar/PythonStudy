from utils import ConvertionException,CryptoConverter
from config import keys,TOKEN
import telebot


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text ="Чтобы начать работу введите команду боту в формате : \n <имя валюты>  \
<в какую валюту перевести> \
<количество переводимой валюты> \
введите /values чтобы получить список доступных валют"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def value(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text,key,))
    bot.reply_to(message, text)
@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) == 3:
            quote, base, amount = values
            totalbase = CryptoConverter.convertcurrency(quote, base, amount, len(values))
        else:
            raise ConvertionException('Вы ввели неверное количество параметров.')
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка ввода пользователя: \n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не возможно обработать команду:\n{e}')
    else:
        totalbase_float = float(totalbase)
        amount_float = round(float(amount),3)
        text = f'Цена {amount} {quote} в {base}  - {totalbase_float * amount_float}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)