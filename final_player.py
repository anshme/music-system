                           # all required modules
import threading
import thread
import pygame
from subprocess import call

pygame.init()
pygame.mixer.init()
set= 0                                   	 # just a flag
file = ''   										#example


def music(file):
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	try:				#the program throws and exception at the end, it will always end with this exception
		while pygame.mixer.music.get_busy():
			pygame.time.Clock().tick(0)
	except:
		print("Exception occured. Ending program")

def pause():
	print( file + " paused")
	pygame.mixer.music.pause()
	global set
	set=1

def playsong():
	global set
	print ("Playing song named : " + file)
	if file != "" and set==0:
		t1 = threading.Thread(target = music ,args=(file,))      # separate thread to play music
		t1.setName("audio bajao")
		t1.start()
	elif set==1:
		pygame.mixer.music.unpause()

def stop():
	pygame.mixer.music.pause();
	global set
	set = 0    												# set =0 ,means song is  not playing currently

play = True
while(play):
	file = raw_input("\nEnter the file name (with extension)")
	ch = 0
	while (ch != 5):
		ch = input("\n1.Play choosen song\n2.Pause the playing song\n3.Resume the paused song\n4.Stop current song and play another song\n5.Exit player\nEnter the choice ")
		if(ch == 1):
			playsong()
		elif (ch == 2):
			pause()
		elif (ch == 3):
			print("\nResuming song")
			playsong()
		elif (ch == 4):
			print( file + " stopped")
			stop()
			break
		elif (ch == 5):
			print("Exiting player")
			play = False;


pygame.quit()
t1.join()   #  wait for music thread to join main thread
