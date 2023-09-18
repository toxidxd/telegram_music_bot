
import sqlite3
import os
import time
from mutagen.mp3 import MP3
from mutagen import id3 as mu



def fGetSongInfo(sSongLocation):
    muTrack=MP3(sSongLocation)
    sAlbum = muTrack.tags['TALB'].text
    sArtist = muTrack.tags['TPE1'].text
    return sArtist, sAlbum

for file in os.listdir('upmusic/'):
    if file.split('.')[-1] == 'mp3':
        f = open('upmusic/'+file, 'rb')


        dfileid = '666'

        track = fGetSongInfo(f)


        artist = track[0]
        album = track[1]

        dartist = str(artist)
        dalbum = str(album)





        print('Artist:', artist)
        print('Album:', album)


        new_artists = [
        (dfileid, dartist, dalbum,),
        ]

        conn = sqlite3.connect('music_id3.db')
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO music_id VALUES (NULL, ?, ?, ?);", new_artists)
        conn.commit()
        conn.close



            #fileid = 666
            #track = fGetSongInfo(f)
            #title =
            #artist = track[0]
            #album = track[1]


        time.sleep(0.1)
