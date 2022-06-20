import os
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from pygame import mixer


root = Tk()

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

mixer.init()  # initializing the mixer

root.geometry('300x300')
root.title("Music Recommendation System")
root.iconbitmap(r'G:\MyCodeprojects\Minor Project\streamlit navbar flaskless main\assets\images\melody.ico')

text = Label(root, text='Lets make some noise!')
text.pack()


def play_music(song_name):
    path = "songs\\"+song_name+".mp3"
    try:
        paused  # Checks whether the 'paused' variable is initialized or not.
    except NameError:  # If not initialized then executes the code under except condition
        try:
            mixer.music.load(path)
            mixer.music.play()
            mixer.music.play()
            statusbar['text'] = "Playing music" + ' - ' + os.path.basename(path)
        except:
            tkinter.messagebox.showerror('File not found', 'could not find the file. Please check again.')

    else:  # If initialized the it goes to the else condition
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Music Paused"


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)
    # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1


playPhoto = PhotoImage(file=r'G:\MyCodeprojects\Minor Project\streamlit navbar flaskless main\assets\images\play.png')
playBtn = Button(root, image=playPhoto, command=lambda: play_music(song_name))
playBtn.pack()

stopPhoto = PhotoImage(file=r'G:\MyCodeprojects\Minor Project\streamlit navbar flaskless main\assets\images\stop.png')
stopBtn = Button(root, image=stopPhoto, command=stop_music)
stopBtn.pack()

pausePhoto = PhotoImage(file=r'G:\MyCodeprojects\Minor Project\streamlit navbar flaskless main\assets\images\pause.png')
pauseBtn = Button(root, image=pausePhoto, command=pause_music)
pauseBtn.pack()

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack()

statusbar = Label(root, text="Welcome", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
