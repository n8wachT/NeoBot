# -*- coding: utf-8 -*-
import telebot
from telebot import types
import functions
import triggers
 
functions.bot.skip_pending=True
triggers.bot.skip_pending=True
#############################################
#Listener
def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            print "[" + str(cid) + "]: " + m.text
 
functions.bot.set_update_listener(listener)
#############################################

################################################################## 
#Peticiones
functions.bot.polling(none_stop=True)
