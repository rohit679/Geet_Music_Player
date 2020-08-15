def unmutemusic():
	global currentvol
	root.unmutebutton.grid_remove()
	root.mutebutton.grid()
	mixer.music.set_volume(currentvol)

def mutemusic():
	global currentvol
	root.mutebutton.grid_remove()
	root.unmutebutton.grid()
	currentvol=mixer.music.get_volume()
	mixer.music.set_volume(0)

def resumemusic():
	root.ResumeButton.grid_remove()
	root.PauseButton.grid()
	mixer.music.unpause()
	AudioStatusLabel.configure(text='Playing...')

def volumeup():
	vol=mixer.music.get_volume()
	mixer.music.set_volume(vol+0.05)
	ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
	ProgressbarVolume['value']=mixer.music.get_volume()*100	

def volumedown():
	vol=mixer.music.get_volume()
	mixer.music.set_volume(vol-0.05)
	ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
	ProgressbarVolume['value']=mixer.music.get_volume()*100	

def stopmusic():
	mixer.music.stop()
	AudioStatusLabel.configure(text='Stopped...')
	ProgressbarMusicStartTimeLabel.configure(text='0:00:0')

def pausemusic():
	mixer.music.pause()
	root.PauseButton.grid_remove()
	root.ResumeButton.grid()
	AudioStatusLabel.configure(text='Paused...')

def playmusic():
	ad=audiotrack.get()
	mixer.music.load(ad)
	ProgressbarLabel.grid()
	root.mutebutton.grid()
	ProgressbarMusicLabel.grid()
	mixer.music.set_volume(0.4)
	ProgressbarVolume['value']=40
	ProgressbarVolumeLabel['text']='40%'
	mixer.music.play()
	AudioStatusLabel.configure(text='Playing...')
 
	Song=MP3(ad)
	totalsonglength=int(Song.info.length)
	ProgressbarMusic['maximum']=totalsonglength
	ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
	def Progressbarmusictick():
		CurrentSongLength=mixer.music.get_pos()//1000
		ProgressbarMusic['value']=CurrentSongLength
		ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
		ProgressbarMusic.after(2,Progressbarmusictick)
	Progressbarmusictick()
def musicurl():
	try:
		dd=filedialog.askopenfilename(initialdir='D:/songs mp3/new songs',title='select audio file',filetype=(('MP3','*.mp3'),('WAV','*.wav')))
	
	except:
		dd=filedialog.askopenfilename(title='select audio file',filetype=(('MP3','*.mp3'),('WAV','*.wav')))
	audiotrack.set(dd)

def createwidthes():
	global imbrowse,implay,impause,imvolumeup,imvolumedown,imstop,imresume,immute,imunmute	#******************image register
	global AudioStatusLabel,ProgressbarLabel,ProgressbarVolume,ProgressbarVolumeLabel,ProgressbarMusicLabel,ProgressbarMusic,ProgressbarMusicEndTimeLabel,ProgressbarMusicStartTimeLabel

	implay=PhotoImage(file='images/play.png')
	imresume=PhotoImage(file='images/play.png')
	imstop=PhotoImage(file='images/stop.png')
	impause=PhotoImage(file='images/pause.png')
	imbrowse=PhotoImage(file='images/search.png')
	imvolumeup=PhotoImage(file='images/volume-up.png')
	imvolumedown=PhotoImage(file='images/volume-down.png')
	immute=PhotoImage(file='images/mute.png')
	imunmute=PhotoImage(file='images/unmute.png')

	#********************change size of images
	imbrowse=imbrowse.subsample(20,20)
	implay=implay.subsample(20,20)
	imstop=imstop.subsample(20,20)
	impause=impause.subsample(20,20)
	imvolumeup=imvolumeup.subsample(20,20)
	imvolumedown=imvolumedown.subsample(20,20)
	imresume=imresume.subsample(20,20)
	immute=immute.subsample(20,20)
	imunmute=imunmute.subsample(20,20)


	#***************************Labels
	TrackLabel=Label(root,text='select audio track:',bg='lightskyblue',font=('arial',15,'italic bold'))
	TrackLabel.grid(row=0,column=0,padx=20,pady=20)

	AudioStatusLabel=Label(root,text='',bg='lightskyblue',font=('arial',15,'italic bold'),width=20)
	AudioStatusLabel.grid(row=2,column=1)

	#**********************entry box
	TrackLabelEntry=Entry(root,font=('arial',15,'italic bold'),width=35,text=audiotrack)
	TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)

	#********************Button
	BrowseButton=Button(root,text='search',bg='deeppink',font=('arial',15,'italic bold'),width=200,bd=5,activebackground='purple4',image=imbrowse,compound=RIGHT,command=musicurl)
	BrowseButton.grid(row=0,column=2,padx=20,pady=20)

	PlayButton=Button(root,text='Play',bg='green2',font=('arial',15,'italic bold'),width=200,bd=5,activebackground='purple4',image=implay,compound=RIGHT,command=playmusic)
	PlayButton.grid(row=1,column=0,padx=20,pady=20)

	root.PauseButton=Button(root,text='Pause',bg='yellow',font=('arial',15,'italic bold'),width=200,bd=5,activebackground='purple4',image=impause,compound=RIGHT,command=pausemusic)
	root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

	root.ResumeButton=Button(root,text='Resume',bg='yellow',font=('arial',15,'italic bold'),width=200,bd=5,activebackground='purple4',image=imresume,compound=RIGHT,command=resumemusic)
	root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
	root.ResumeButton.grid_remove()
	
	root.mutebutton=Button(root,text='mute',width=100,bg='yellow',activebackground='purple4',bd=5,image=immute,compound=RIGHT,command=mutemusic)
	root.mutebutton.grid(row=3,column=3)
	root.mutebutton.grid_remove()

	root.unmutebutton=Button(root,text='unmute',width=100,bg='yellow',activebackground='purple4',bd=5,image=imunmute,compound=RIGHT,command=unmutemusic)
	root.unmutebutton.grid(row=3,column=3)
	root.unmutebutton.grid_remove()

	VolumeUpButton=Button(root,text='Volume up',bg='blue',font=('arial',15,'italic bold'),width=200,bd=5,activebackground='purple4',image=imvolumeup,compound=RIGHT,command=volumeup)
	VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)

	StopButton=Button(root,text='Stop',bg='red',font=('arial',15,'italic bold'),width=200,bd=5,activebackground='purple4',image=imstop,compound=RIGHT,command=stopmusic)
	StopButton.grid(row=2,column=0,padx=20,pady=20)

	VolumeDownButton=Button(root,text='Volume Down',bg='blue',font=('arial',15,'italic bold'),width=200,bd=5,activebackground='purple4',image=imvolumedown,compound=RIGHT,command=volumedown)
	VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)

	#***************************progress bar volume
	ProgressbarLabel=Label(root,text='',bg='red')
	ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
	ProgressbarLabel.grid_remove()
	ProgressbarVolume=Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',value=0,length=190)
	ProgressbarVolume.grid(row=0,column=0,ipadx=5)

	ProgressbarVolumeLabel=Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
	ProgressbarVolumeLabel.grid(row=0,column=0)

	#*****************************progress bar music
	ProgressbarMusicLabel=Label(root,text='',bg='red')
	ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
	ProgressbarMusicLabel.grid_remove()

	ProgressbarMusicStartTimeLabel=Label(ProgressbarMusicLabel,text='0:00:0',bg='red',width=6)
	ProgressbarMusicStartTimeLabel.grid(row=0,column=0)

	ProgressbarMusic=Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
	ProgressbarMusic.grid(row=0,column=1,ipadx=370,ipady=3)

	ProgressbarMusicEndTimeLabel=Label(ProgressbarMusicLabel,text='0:00:0',bg='red')
	ProgressbarMusicEndTimeLabel.grid(row=0,column=2)

#****************************main window
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter .ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
root=Tk()
root.geometry('1100x500+200+50')
root.title('simple music player')
root.iconbitmap('images/music.ico')
root.resizable(False,False)
root.configure(bg='lightskyblue')
#*********************************global variable
audiotrack=StringVar()
currentvol=0
totalsonglength=0
text=''
count=0
#**********************************slider
ss='developed by rohit prasad'

SliderLabel=Label(root,text=ss,bg='lightskyblue',font=('arial',40,'italic bold'))
SliderLabel.grid(row=4	,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTrick():
	global count,text
	if count>=len(ss):
		count=-1
		text=''
	else:
		text=text+ss[count]
		SliderLabel.configure(text=text)
	count+=1
	SliderLabel.after(200,IntroLabelTrick)
IntroLabelTrick()
mixer.init()
createwidthes()
root.mainloop()
