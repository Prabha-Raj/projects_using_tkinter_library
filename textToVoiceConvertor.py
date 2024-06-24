

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os



root=Tk()
root.title("Text to Speech")
root.geometry("900x450+80+50")
root.resizable(False,False)
root.configure(bg="#305065")


engine = pyttsx3.init()


def speak():
	text=text_area.get(1.0,END)
	print(text)
	gender=gender_Combobox.get()
	print(gender)
	speed=speed_Combobox.get()
	print(speed)
	voices=engine.getProperty("voices")
	
	def setVoice():
		if (gender == "Male"):
			engine.setProperty("voice",voices[0].id)
			engine.say(text)
			engine.runAndWait()
		else:
			engine.setProperty("voice",voices[1].id)
			engine.say(text)
			engine.runAndWait()
	if text:
		if speed=="Fast":
			engine.setProperty('rate',250)
			setVoice()
		elif speed=="Normal":
			engine.setProperty('rate',150)
			setVoice()
		else:
			engine.setProperty('rate',60)
			setVoice()
		
def download():
	print()


#icon
#image_icon=PotoImage(file="Speack.png")
#root.iconphoto(False,image_icon)


#Top Frame
Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)


#Logo=PhotoImage(file="speaker Logo.png")
#Label(Top_fram,image=Logo,bg="white").place(x=10,y=5)

Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)

#*************************************************************
text_area=Text(root,font="Robot 20",padx="10",pady="10",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)


gender_Combobox=Combobox(root,values=["Male","Female"],font="arial 14",state="r",width=10)
gender_Combobox.place(x=550,y=200)
gender_Combobox.set("Male")

speed_Combobox=Combobox(root,values=["Fast","Normal","Slow"],font="arial 14",state="r",width=10)
speed_Combobox.place(x=730,y=200)
speed_Combobox.set("Normal")

#imageicon=PhotoImage(file="Speak.png")
#btn=Button(root,text="Speak",compound=LEFT,image=imageicon,width=130,font="Calibri 14 bold")
#btn.place(x=550,y=280)

btn1=Button(root,text="SPEAK",width=10,font="Calibri 14 bold",command=speak)
btn1.place(x=565,y=280)
btn2=Button(root,text="SAVE",width=10,font="Calibri 14 bold",command=download)
btn2.place(x=745,y=280)


root.mainloop()