from telegram.ext import Updater, CommandHandler

# Botunuzun API anahtarını buraya ekleyin
TOKEN = "6520654911:AAEPFSqACfRU15zeT9UWygYpg_SOeET3eXo"

# /start komutunu işleyen fonksiyon
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba! Benim adım Komut Botu. Nasıl yardımcı olabilirim?")

# /echo komutunu işleyen fonksiyon
def echo(update, context):
    # Gelen mesajı al ve tekrar gönder
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    # Botunuzun tetikleyicisini oluşturun
    updater = Updater(TOKEN, use_context=None)
    dispatcher = updater.dispatcher

    # /start ve /echo komutlarına uygun işleyicileri ekleyin
    start_handler = CommandHandler('start', start)
    echo_handler = CommandHandler('echo', echo)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    # Botu çalıştırın
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
