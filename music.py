from tkinter import *
import pygame
import os
import time
class MusicPlayer:
	def __init__(self,root):
		self.root=root
		self.root.title("Music Player")
		self.root.geometry("1000x400+200+200")
		pygame.init()
		pygame.mixer.init()
		#bg=pygame.image.load("p1.jpg")
		self.track=StringVar() #declaring track variable
		self.status=StringVar() #declaring status variable
		
#creating track frame for track and status variable
		trackframe=LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
		trackframe.place(x=0,y=0,width=600,height=200)

#inserting song track label
		songtrack=Label(trackframe,textvariable=self.track,width=35,font=("times new roman",15,"bold"),bg="grey",fg="gold",bd=5,relief=GROOVE)
		songtrack.grid(row=1,column=0,padx=10,pady=5)


#inserting song status label
		trackstatus=Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold",bd=5,relief=GROOVE)
		trackstatus.grid(row=3,column=1,padx=10,pady=5)

#creating  button frame
		buttonframe=LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
		buttonframe.place(x=0,y=200,width=600,height=200)

#inserting play button
		playbtn=Button(buttonframe,text="PLAY",width=20,height=1,font=("times new roman",16,"bold"),bg="green",fg="white",bd=5,command=self.playsong)
		playbtn.grid(row=0,column=0,padx=10,pady=5)

#inserting pause button
		playbtn=Button(buttonframe,text="PAUSE",width=20,height=1,font=("times new roman",16,"bold"),bg="green",fg="white",bd=5,command=self.pausesong)
		playbtn.grid(row=0,column=1,padx=10,pady=5)
#inserting unpause button
		playbtn=Button(buttonframe,text="RESUME",width=20,height=1,font=("times new roman",16,"bold"),bg="green",fg="white",bd=5,command=self.unpausesong)
		playbtn.grid(row=1,column=0,padx=10,pady=5)
#inserting rewind button
		playbtn=Button(buttonframe,text="REWIND",width=20,height=1,font=("times new roman",16,"bold"),bg="green",fg="white",bd=5,command=self.rewindsong)
		playbtn.grid(row=1,column=1,padx=10,pady=5)



#inserting stop button
		playbtn=Button(buttonframe,text="STOP",width=20,height=1,font=("times new roman",16,"bold"),bg="green",fg="white",bd=5,command=self.stopsong)
		playbtn.grid(row=2,column=0,padx=20,pady=5)




#creating playlist frame
		playlistframe=LabelFrame(self.root,text="PLAYLIST",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
		playlistframe.place(x=600,y=0,width=400,height=400)
#inserting scrollbar
		scrol_y=Scrollbar(playlistframe,orient=VERTICAL)
#inserting playlist listbox
		self.playlist=Listbox(playlistframe,selectbackground="gold",selectmode=SINGLE,font=("times new roman",20,"bold"),bg="black",fg="white",bd=5,relief=GROOVE,yscrollcommand=scrol_y.set)
		scrol_y.pack(side=RIGHT,fill=Y)
		scrol_y.config(command=self.playlist.yview)
		self.playlist.pack(fill=BOTH)
#changing directory for fetching songs
		os.chdir("C:/Users/Sahil Mody/Desktop/songs")
#fetching songs
		songtracks=os.listdir()
		songs=[]
#inserting songs into playlist
		for track in songtracks:
			self.playlist.insert(END,track)
			if track.endswith(".mp3"):
				songs.append(track)


	def playsong(self):

#displaying play song title
		self.track.set(self.playlist.get(ACTIVE))
#displaying status	
		self.status.set("-Playing")
#loading selected song
		pygame.mixer.music.load(self.playlist.get(ACTIVE))
#playing selected song
		pygame.mixer.music.play()
	 
	def pausesong(self):
		self.status.set("-Paused")
		pygame.mixer.music.pause()
			
		
	def unpausesong(self):
		self.status.set("-Playing")
		pygame.mixer.music.unpause()
	def stopsong(self):
		self.status.set("-Stopped")
		pygame.mixer.music.stop()
	def rewindsong(self):
		pygame.mixer.music.rewind()
	def next(self):
		pygame.mixer.music.load(self.playlist.get(ACTIVE))
		pygame.mixer.music.play()


	


root=Tk()
MusicPlayer(root)
root.mainloop()