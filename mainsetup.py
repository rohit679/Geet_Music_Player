from cx_Freeze import *
includefiles=["images/music.ico",'images/mute.png','images/unmute.png','images/pause.png','images/stop.png','images/play.png','images/search.png','images/volume-up.png','images/volume-down.png']
excludes=[]
packages=[]
base=None

if sys.platform=="win64":
	base="Win64GUI"

shortcut_table=[
	("DesktopShortcut", #Shortcut
	 "DesktopFolder", #Directory
	 "Simple Music Player", #Name
	 "TARGETDIR", #component
	 "[TARGETDIR]\rohitmusic.exe", #Target
	 None, #Arguments
	 None, #Description
	 None, #Hotkey
	 None, #Icon
	 None, #Iconindex
	 None, #Showcmd
	 "TARGETDIR", #WKDir
	 )
]
msi_data={"Shortcut":shortcut_table}
bdist_msi_options={'data':msi_data}
setup(
	version="0.1",
	description="Simple music player by rohit prasad",
	author="Rohit Prasad",
	name="music player",
	options={'build_exe':{'include_files':includefiles},"bdist_msi":bdist_msi_options, },
	executables=[
		Executable(
			script="rohitmusic.py",
			base=base,
			icon='images/music.ico',
		)
	]
)