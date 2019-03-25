from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
from telegram import ChatAction
from gtts import gTTS

def apri(file,lista):
    f1 = open(file, "r")
    lista.extend(f1.read().splitlines())

def chiudi(file, lista):
    f2 = open(file, "w")
    for task in lista:
        f2.write(task + "\n")

def start(bot, update):
    update.message.reply_text("Ciao!")

def start(bot, update):
        update.message.reply_text("Ciao!")

def showTasks(bot, update):
        update.message.reply_text("Ciao!")

def newTask(bot, update):
    update.message.reply_text("Ciao!")

def removeTask(bot, update):
    update.message.reply_text("Ciao!")

def removeAllTasks(bot, update):
    update.message.reply_text("Ciao!")

"""
def tts(bot, update):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id, ChatAction.UPLOAD_AUDIO)

    testo=update.message.text
    tts=gTTS(text=testo, lang="it")
    tts.save("audio_file.mp3")
    voce=open("audio_file.mp3", "rb")
    bot.sendVoice(chat_id=chat_id, voice=voce)
"""

def main():
    file = "task_list.txt"
    lista = []

    updater=Updater("850353488:AAFBgFTZ-DkxbBhmVg0doE52z7nVTF9yY4c")
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("showTasks", start))
    dp.add_handler(CommandHandler("newTask", start))
    dp.add_handler(CommandHandler("removeTask", start))
    dp.add_handler(CommandHandler("removeAllTasks", start))

    updater.start_polling()

    apri(file, lista)
    updater.idle()
    chiudi(file, lista)

if __name__ == '__main__':
    main()