import tkinter as tk
import os
import pygame as pg

#folders
folders = [r"C:\Users\ASUS\Desktop\music",r"C:\Users\ASUS\Desktop\music\Lo-Fi Music"]

#setting
root = tk.Tk()
root.title('music player')
root.geometry('600x800')
root.resizable(False,False)

status = tk.StringVar()
pg.init()
pg.mixer.init()

#button function

def playsong():
    showsong_Name.config(state="normal")    
    showsong_Name.delete("1.0","end")
    showsong_Name.insert("1.0",playlist.get("active"))
    showsong_Name.config(state="disabled")
    status.set("playing")
    pg.mixer.music.load(playlist.get("active"))
    pg.mixer.music.play()
    
def stopsong():
    status.set("stoped")
    pg.mixer.music.stop()

def pausesong():
    status.set("pause")
    pg.mixer.music.pause()
    
def unpausesong():
    status.set('unpauseing')
    pg.mixer.music.unpause()


#song music list
songplaylist = tk.LabelFrame(root, text="music list", bg="red", fg="white", width=580,height=90)
songplaylist.place(x=10, y=1, width=580, height=590)

scrolly = tk.Scrollbar(songplaylist, orient="vertical")
playlist = tk.Listbox(songplaylist, bg="blue", fg="white",selectmode="single",selectbackground="red",height=100,font=("",16),yscrollcommand=scrolly)

scrolly.config(command=playlist.yview)
scrolly.pack(fill="y", side="right")
playlist.pack(fill="both",padx=5,)


scrolly.config(command=playlist.yview)
scrolly.pack(fill="y", side="right")

#song track
trackFrame = tk.LabelFrame(root, text="song Track", bg="red", fg="white", width=580,height=90)
trackFrame.place(x=10, y=600, width=580, height=90)

showsong_Name = tk.Text(trackFrame, bg="blue",fg="white", width=50, height=1, state="disabled")
showsong_Name.grid(row=0 , column=0, padx=17, pady=13)

showstatue = tk.Label(trackFrame, bg="blue", fg="white",width=15, textvariable=status)
showstatue.grid(row=0, column=1)

#control panel
ctrplanel = tk.LabelFrame(root, text="control panel", bg="red",fg="white", bd=5,font=("Arial",12), padx=15)
ctrplanel.place(x=10 , y=700, width=580,height=90)

playbtn = tk.Button(ctrplanel, text="play",bg="blue",fg="white",width=15,command=playsong)
playbtn.grid(row=0, column=0, padx=10, pady=17)

stopbtn = tk.Button(ctrplanel, text="stop", width=15,bg="blue",fg="white", command=stopsong)
stopbtn.grid(row=0, column=1, padx=10, pady=17)


pausebtn = tk.Button(ctrplanel, text="pause", width=15,bg="blue",fg="white", command=pausesong)
pausebtn.grid(row=0, column=2, padx=10, pady=17)

unpausebtn = tk.Button(ctrplanel, text="unpauseing",bg="blue",fg="white", width=15, command=unpausesong)
unpausebtn.grid(row=0, column=3, padx=10, pady=17)

#os
os.chdir(r"C:\Users\ASUS\Desktop\music")
mysong = os.listdir()

for song in mysong:
    if ".mp3" in song:
        playlist.insert("end",song)
    
    
    
#loop
root.mainloop()