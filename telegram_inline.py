import sys
from time import *
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from gpiozero import LED

blue = LED(17)

#LED
def on():
        blue.on()
        return
def off():
        blue.off()
        return
def blink():
	count = 0
	while (count < 9): 
		blue.on()
		sleep(1)
		blue.off()
		sleep(1)
		count = count + 1
	return

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='On', callback_data='on')],
                   [InlineKeyboardButton(text='Off', callback_data='off')],
                   [InlineKeyboardButton(text='Blink', callback_data='blink')],
               ])

    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    
    if query_data == 'on':
        bot.answerCallbackQuery(query_id, on())
    elif query_data == 'off':
        bot.answerCallbackQuery(query_id, off())
    elif query_data == 'blink':
        bot.answerCallbackQuery(query_id, blink())

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    sleep(10)
