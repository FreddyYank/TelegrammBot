import telebot
import time

token = '5992942897:AAFgfBhPoldn36g8_lGSasRSNE6ReXs8P94'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['timer'])
def say(message):
    for i in range(9):
        time.sleep(1)
        bot.send_message(message.chat.id, i +1)

@bot.message_handler(commands=['say'])
def say(message):
    text = " ".join(message.text.split(' ')[1:])
    bot.reply_to(message, f'***{text.upper()}!***')

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    file_ID = 'CAACAgIAAxkBAAEIEApkCeH8aypCSgNoFg15QN7wFvXOcAACFQADwDZPE81WpjthnmTnLwQ'
    bot.send_sticker(message.chat.id, sticker=f'{file_ID}')
@bot.message_handler(commands=["start", "help"])
def send_message(message):
    bot.reply_to(message, "Чем могу помочь?")

@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, "Текст содержит слово \"Плохой\"")
        return
    text = message.text[::-1]
    bot.reply_to(message, f"Текст: {message.text}; перевёрнутый: {text}")
bot.polling()
