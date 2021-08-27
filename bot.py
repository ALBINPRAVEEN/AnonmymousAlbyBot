
from telegram.ext import Filters,Updater,MessageHandler,CommandHandler
from commands.commands import *
from functions.functions import *
from caption.setCaption import setCaption
import os
from config import Config

updater=Updater(Config.TOKEN,use_context=True)
dp=updater.dispatcher


#/start
dp.add_handler(CommandHandler('start',startMessage))
#/help
dp.add_handler(CommandHandler('help',helpMessage))

#Files
dp.add_handler(MessageHandler(Filters.document,sendFile))

#Media
dp.add_handler(MessageHandler(Filters.video,sendMedia))

#Photos
dp.add_handler(MessageHandler(Filters.photo,sendPhoto))

#Text & Caption
dp.add_handler(MessageHandler(Filters.text,setCaption))

#Stickers
dp.add_handler(MessageHandler(Filters.sticker,sendSticker))

#Voice
dp.add_handler(MessageHandler(Filters.voice,sendVoice))

#Audio
dp.add_handler(MessageHandler(Filters.audio,sendAudio))

updater.start_polling()
updater.idle()
