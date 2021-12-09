import telebot
import sqlite3

bot = telebot.TeleBot("5091468418:AAE0OBuw3xHxx0OT7rsAQlJiru4DfzOlv0E")


conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS 'ids' (id STRING UNIQUE , is_admin BOOLEAN , UNIQUE(id))")


def db(id, root):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT OR IGNORE INTO ids(id, is_admin) VALUES({id}, {root})")
    conn.commit()


def read_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ids")
    ids = cursor.fetchall()
    return ids


@bot.message_handler(content_types=["poll", "text", "photo", "document", "audio"])
def func(message):
    user_lst = read_db()
    chat_id = message.chat.id
    message_id = message.message_id

    if message.text == "2235":
        db(chat_id, True)
    else:
        db(chat_id, False)

    for i in user_lst:
        if i[0] == chat_id:
            if i[1] == 1:
                for i in user_lst:
                    bot.forward_message(i[0], chat_id, message_id)


bot.polling()
