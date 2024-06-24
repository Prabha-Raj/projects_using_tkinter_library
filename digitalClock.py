#Digital Clock

from tkinter import *
import time

def presentTime():
	showTime=time.strftime("%I:%M:%S %p")
	lblTime.config(text=showTime)
	lblTime.after(200,presentTime)
		

root=Tk()
root.geometry("1000x200")
root.resizable(False,False)
root.title("Digital Clock ( INDIAN TIME )")
lblTime=Label(root,font=("Arial 120 bold"),fg="blue",bg="orange",)
lblTime.pack()
presentTime()

root.mainloop()