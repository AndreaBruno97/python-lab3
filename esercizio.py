from telegram.ext import Updater, Filters, CommandHandler, MessageHandler

def apri(file,lista):
    f1 = open(file, "r")
    lista.extend(f1.read().splitlines())

def chiudi(file, lista):
    f2 = open(file, "w")
    for task in lista:
        f2.write(task + "\n")

def start(bot, update):
    update.message.reply_text("Hello!")

def showTasks(bot, update, lista):
    if len(lista)==0:
        update.message.reply_text("Nothing to do, here!")
    else:
        update.message.reply_text(lista)

def newTask(bot, update, lista, args):
    new=" ".join(args)
    lista.append(new)
    update.message.reply_text("Task added")

def removeTask(bot, update, lista, args):
    old=" ".join(args)
    if old in lista:
        lista.remove(old)
        update.message.reply_text("Element removed")
    else:
        update.message.reply_text("No such element")

def removeAllTasks(bot, update, lista, args):
    sub=" ".join(args)
    lung=len(lista)
    eliminati=0
    messaggio="The elements "
    i = 0
    while i < lung:
        if lista[i].find(sub) >= 0:
            eliminati+=1
            messaggio = messaggio + "\"" + lista[i] + "\" "
            del lista[i]
            i -= 1
            lung -= 1
        i += 1
    messaggio = messaggio + "were removed"
    if eliminati == 0:
        update.message.reply_text("No element removed")
    else:
        update.message.reply_text(messaggio)

def main():
    file = "task_list.txt"
    lista = []

    updater=Updater("850353488:AAFBgFTZ-DkxbBhmVg0doE52z7nVTF9yY4c")
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("showTasks", showTasks))
    dp.add_handler(CommandHandler("newTask", newTask, pass_args=True))
    dp.add_handler(CommandHandler("removeTask", removeTask, pass_args=True))
    dp.add_handler(CommandHandler("removeAllTasks", removeAllTasks, pass_args=True))

    updater.start_polling()

    apri(file, lista)
    updater.idle()
    chiudi(file, lista)

if __name__ == '__main__':
    main()