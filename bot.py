# -*- coding: utf-8 -*-
# import config
import telebot
import os
import time
import sqlite3
import re
import string
from mutagen.mp3 import MP3

bot = telebot.TeleBot('465106047:AAGzJs9aO5QXxt2QGBfNQgcdxjsrVAvJMKI')


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, "Как тебя зовут?")
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(
        message.chat.id, 'Привет, {name}!'
        .format(name=message.text))


@bot.message_handler(commands=['addmusic'])
def musupload(message):
    for file in os.listdir('upmusic/'):

        if file.split('.')[-1] == 'mp3':
            f = open('upmusic/' + file, 'rb')
            msg = bot.send_audio(message.chat.id, f)
            bot.send_message(message.chat.id, msg.audio.file_id, reply_to_message_id=msg.message_id)
            dfileid = msg.audio.file_id
            track = MP3('upmusic/' + file)
            artist = track.tags['TPE1'].text
            album = track.tags['TALB'].text
            # artist = 0
            # album = 1
            dartist = str(artist)
            dalbum = str(album)
            dartist = re.sub(r"[\[\]',\n\s]", "", dartist)
            dalbum = re.sub(r"[\[\]',\n\s]", "", dalbum)
            dartist = dartist.lower()
            dalbum = dalbum.lower()

            new_artists = [
                (dfileid, dartist, dalbum,),
            ]

            conn = sqlite3.connect('music_id.db')
            cursor = conn.cursor()
            cursor.executemany("INSERT INTO music_id VALUES (NULL, ?, ?, ?);", new_artists)
            conn.commit()
            conn.close()

            time.sleep(10)


@bot.message_handler(commands=['limpbizkit'])
def limpbizkit(message):
    sent = bot.send_message(message.chat.id, "Приятного прослушивания!)")

    conn = sqlite3.connect('music_id.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM music_id WHERE artist = 'limpbizkit'")
    row = cursor.fetchone()
    while row is not None:
        bot.send_audio(message.chat.id, row[1])
        row = cursor.fetchone()
    conn.commit()
    conn.close()


@bot.message_handler(commands=['linkinpark'])
def linkinpark(message):
    sent = bot.send_message(message.chat.id, "Приятного прослушивания!)")

    conn = sqlite3.connect('music_id.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM music_id WHERE artist = 'linkinpark'")
    row = cursor.fetchone()
    while row is not None:
        bot.send_audio(message.chat.id, row[1])
        row = cursor.fetchone()
    conn.commit()
    conn.close()


@bot.message_handler(commands=['lesbiansonecstasy'])
def lesbiansonecstasy(message):
    sent = bot.send_message(message.chat.id, "Приятного прослушивания!)")

    conn = sqlite3.connect('music_id.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM music_id WHERE artist = 'lesbiansonecstasy'")
    row = cursor.fetchone()
    while row is not None:
        bot.send_audio(message.chat.id, row[1])
        row = cursor.fetchone()
    conn.commit()
    conn.close()


bot.polling(none_stop=True)
