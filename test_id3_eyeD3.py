
import sqlite3
import os
import time
import eyed3



for file in os.listdir('upmusic/'):
    if file.split('.')[-1] == 'mp3':
        f = open('upmusic/'+file, 'rb')

        audiofile = eyed3.load('upmusic/'+file)
        print (audiofile)






        #new_artists = [
        #(dfileid, dartist, dalbum,),
        #]

        #conn = sqlite3.connect('music_id3.db')
        #cursor = conn.cursor()
        #cursor.executemany("INSERT INTO music_id VALUES (NULL, ?, ?, ?);", new_artists)
        #conn.commit()
        #conn.close

        time.sleep(0.1)
