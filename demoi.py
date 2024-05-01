import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pyttsx3

def speak():
    global text_area, gender_combobox, speed_combobox
    
    text = text_area.get("1.0", "end-1c")
    voice = gender_combobox.get()
    speed = speed_combobox.get()
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 150 if speed == 'Fast' else 100 if speed == 'Normal' else 50)
    voices = engine.getProperty('voices')
    
    for v in voices:
        if voice.lower() in v.name.lower():
            engine.setProperty('voice', v.id)
            break
            
    engine.say(text)
    engine.runAndWait()

def download():
    print("Download functionality goes here")

root = tk.Tk()
root.title("Text to speech")
root.geometry("900x450+100+200")
root.resizable(False, False)
root.configure(bg="#305065")

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="pic/ddm.png")
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)

Label(Top_frame, text="TEXT TO SPEECH", font="arial 30 bold", bg="white", fg="black").place(x=100, y=30)

text_area = Text(root, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=760, y=160)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='readonly', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

imageicon = PhotoImage(file="pic/rrrrrr.png")
btn = Button(root, text="Speak", compound=LEFT, image=imageicon, width=130, font="arial 14 bold", command=speak)
btn.place(x=550, y=280)

imageicon2 = PhotoImage(file="pic/hhhh.png")
save = Button(root, text="Save", compound=LEFT, image=imageicon2, width=130, bg="green", font="arial 14 bold", command=download)
save.place(x=730, y=280)

root.mainloop()
