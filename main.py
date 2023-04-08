                #    ************* MUSIC PLAYER *************
                #             CodeClause Intership 
                #  ***********************************************
                
                #               Perumalla Dharan


# Importing the needed modules
from tkinter import filedialog
import tkinter
from tkinter import *
import os
import pygame
# import pygame.mixer


# Creating and initializing the window 
root = Tk()  
root.title("Music Player")  
root.geometry("500x300")  


# Initializing 
pygame.mixer.init()  


# Creating menu 
menubar = Menu(root)
root.config(menu=menubar)


# Adding Frame to the root
frame = LabelFrame(root)
frame.pack()


# Global Variables 

# Variable to store the songs in a list
songs = []
# Variable to keep track of the current song
current_song = ""
# Variable to keep track of the current song
paused = False


# Various functions of the music player
# Function to load the music 
def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    # Checks for the files with extension .mp3
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    # Inserts the songs into songlist
    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]


# Function to play tthe song
def play_music():
    global current_song, paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False


# Function to puse the song
def pause_music():
    global current_song, paused

    try:
        # songlist.selection_clear(0, END)
        # songlist.selection_set(songs.index(current_song)+1)
        # current_song = songs[songlist.curselection()[0]]
        # play_music()
        pygame.mixer.music.pause()
    except:
        # pass
        pygame.mixer.music.unpause()


# Function to play the previous song
def prev_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song)-1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


# Function to play the next song
def next_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song)+1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


# Creating the menu 
organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Organise', menu=organise_menu)


# Displaying the songlist 
songlist = Listbox(root, bg="white", width=100, height=60)
songlist.pack()


# Loading the images 
play_button_image = PhotoImage(file='play.png')
pause_button_image = PhotoImage(file='pause.png')
previous_button_image = PhotoImage(file='previous.png')
next_button_image = PhotoImage(file='next.png')


# Adding functionalities to the buttons 
play_button = Button(frame, image=play_button_image, command=play_music)
pause_button = Button(frame, image=pause_button_image, command=pause_music)
previous_button = Button(frame, image=previous_button_image, command=prev_music)
next_button = Button(frame, image=next_button_image, command=next_music)


# Placing the buttons
play_button.grid(row=0, column=0)
pause_button.grid(row=0, column=1)
previous_button.grid(row=0, column=2)
next_button.grid(row=0, column=3)

# Running the main loop
root.mainloop()  
