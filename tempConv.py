#Temprature Converter by using tkinter library.

from tkinter import *

def ctof():
	try:
		c=eval(tb.get())
		f=(((c*9)/5)+32)
		res.config(text=(f,"F"))
	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")
def ftoc():
	try:
		f=int(tb.get())
		c=(((f-32)/9)*5)
		res.config(text=(c,"°C"))
	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")	

root=Tk()
root.iconphoto(True,PhotoImage(file='tampLogo.png'))
root.geometry("500x400")
root.resizable(False,False)
root.title("TempConv")
root.config(bg="pink")
lbl=Label(root,text="Temprature Converter",bg="pink",font=("Arial 20 bold"))
lbl.place(x=100,y=10)
tb=Entry(root,font=("Arial 15 "),width="40",border="2")
tb.place(x=25,y=60)
res=Label(root,font=("Arial 15"),width="40",bg="yellow")
res.place(x=25,y=100)
btnctof=Button(root,text="C to F",font=("Arial 10 bold"),width="20",fg="white",bg="black",command=ctof)
btnctof.place(x=25,y=180)
btnftoc=Button(root,text="F to C",font=("Arial 10 bold"),width="20",fg="white",bg="black",command=ftoc)
btnftoc.place(x=300,y=180)
root.mainloop()