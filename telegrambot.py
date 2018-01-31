#code:{syamsi}

import sys
from time import sleep
import random
import datetime
import telepot
from gpiozero import LED

red = LED(17)

#LED
def on(): # turn on LED
        red.on()
        return
def off(): #turn off LED
        red.off()
        return
def blink(): #make LED blink
	count = 0
	while (count < 9): 
		red.on()
		sleep(1)
		red.off()
		sleep(1)
		count = count + 1
	return

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s' % command)

    if (command == 'on' or command == 'On'):
       bot.sendMessage(chat_id, on())
    if (command == 'off' or command == 'Off'):
       bot.sendMessage(chat_id, off())
    elif (command == 'blink' or command == 'Blink'):
       bot.sendMessage(chat_id, blink())

bot = telepot.Bot('529721689:AAE46-AE6dhjMI9PWwwHnYd-y4pHkw2mU34')
bot.message_loop(handle)
print ('I am listening...')

while 1:
     sleep(10)
