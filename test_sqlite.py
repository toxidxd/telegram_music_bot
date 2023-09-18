import sqlite3










print(" ------------------------------------------------- ")
print("  ")
print("  ")
print("Выдача музыки")


conn = sqlite3.connect('music_id.db')
cursor = conn.cursor()


cursor.execute("SELECT * FROM music_id WHERE artist = 'linkinpark'")

row = cursor.fetchone()

#print(row[1])

while row is not None:
	#print(row)
	print(" ========= ")
	print("artist =", row[2])
	print("album =", row[3])
	print("fileid =", row[1])
	print(" ========= ")
	row = cursor.fetchone()

conn.commit()
conn.close


print("  ")
print("  ")
print(" ------------------------------------------------- ")


#		ifileid = input("input id: ")
#		#igenre = input("Введите жанр")
#		iartist = input ("input artist: ")
#		ialbum = input ("input album: ")
#
#		new_artists = [
#		(ifileid, ialbum, iartist,),
#		]
#
#
#		conn = sqlite3.connect('music_id.db')
#		cursor = conn.cursor()
#		cursor.executemany("INSERT INTO music_id VALUES (NULL, ?, ?, ?);", new_artists)
#		conn.commit()
#
#
#		conn.close
