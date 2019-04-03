import glob
from mutagen.mp3 import MP3
import re

fhand = open('list.txt','w')
for song_name in glob.glob('*.mp3'):
	audio = MP3(song_name)
	print (str(song_name))
	fhand.write((song_name) +  "|" + str(audio.info.length) +  "\n")
fhand.close()

song_name = list()
song_length = list()
fhand = open('list.txt')
for line in fhand:
	attribute = line.split("|")
	song_length.append(attribute[1])
	song_name.append(attribute[0])
	#song_length = float(attr[-1])
	#print(song_length)
fhand.close()

print(song_name)
print(song_length)
