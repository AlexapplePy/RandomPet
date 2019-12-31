import telebot, requests, bs4
from bs4 import BeautifulSoup

#token
bot = telebot.TeleBot("TOKEN")

#buttons
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=20*100)
keyboard.row('\U00002728Get cat\U0001F63C', '\U00002728Get dog\U0001F436')

#random.dog parser with debuging nonetypes
def dog():
    page_link = 'https://random.dog/'
    response = requests.get(page_link)
    html = response.content
    soup = BeautifulSoup(html,'html.parser')
    obj = soup.find('img', attrs = {'id':'dog-img'})
    if obj is None:
        return dog()
    else:
        dogpic = 'https://random.dog/' + obj.attrs['src']
        return dogpic

#random.cat parser
def cat():
    page_link = 'https://random.cat/'
    response = requests.get(page_link)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    obj = soup.find('img', attrs={'id': 'cat'})
    return obj.attrs['src']

#/start
@bot.message_handler(commands=['start'])
def kitty_button(message):
    bot.send_message(message.chat.id,'Press the button', reply_markup=keyboard)

#keyboard and functions
@bot.message_handler(content_types=['text'])
def randomcat(message):
    if message.text == '\U00002728Get cat\U0001F63C':
        bot.send_photo(message.chat.id, cat())
    elif message.text == '\U00002728Get dog\U0001F436':
        bot.send_photo(message.chat.id, dog())
    else:
        bot.send_message(message.chat.id, 'Жми на кнопку')

bot.polling(none_stop=True)
