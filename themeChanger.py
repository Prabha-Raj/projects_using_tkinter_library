
from tkinter import *

root=Tk()
root.title("Toggle theme")
root.geometry("400x600")
root.config(bg="white")


button_mode=True
def toggle():
	global button_mode
	if button_mode:
		button.config(text="Dark Mode",bg="white",fg="black")
		root.config(bg="black")
		button_mode=False
	else:
		button.config(text="Light Mode",bg="black",fg="white")
		root.config(bg="white")
		button_mode=True




button=Button(root,text="Light Mode",font="Calibri 15 bold",bg="black",fg="white",width="10",command=toggle)
button.pack(padx=50,pady=50)


root.mainloop()