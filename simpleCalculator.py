#tkinter library practice

from tkinter import * 

def add():
	try:
		a=eval(n1.get())
		b=eval(n2.get())
		c=a+b
		res.config(text=c)
	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")
def sub():
	try:
		a=eval(n1.get())
		b=eval(n2.get())
		c=a-b
		res.config(text=c)
	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")
def mul():
	try:
		a=eval(n1.get())
		b=eval(n2.get())
		c=a*b
		res.config(text=c)
	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")
def div():
	try:
		a=eval(n1.get())
		b=eval(n2.get())
		c=a//b
		res.config(text=c)
	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")
	
def rem():
	try:
		a=eval(n1.get())
		b=eval(n2.get())
		c=a%b
		res.config(text=c)
	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")


					#tkinter is an Library for creating of GUI base Aploction
Root=Tk() 					#creating object of the Tk() class Tk() is class of the tkinter Library
#Root.iconbitmap('tampLogo.png')
#Root.iconphoto(True,PhotoImage(file='calcLogo.png'))
Root.config(bg="pink")
Root.title("Sc")					#title Function is change title of the box	
Root.geometry("500x400+290+90")				#geometry function is for set the widthxheigth+left+top
Root.resizable(False,False)
lbl1=Label(Root,text="Simple Calculator",fg="black",bg="pink",font=("Arial 20 bold"))  #Label() is for set the properties of heading in the box
lbl1.place(x=130,y=0)					#place() function is to set the position text/heading
lbl2=Label(Root,text="Enter First Number : ",fg="black",bg="pink",font=("Arial 12 bold"))
lbl2.place(x=15,y=50)
lbl3=Label(Root,text="Enter second Number : ",fg="black",bg="pink",font=("Arial 12 bold"))
lbl3.place(x=15,y=80)
n1=Entry(Root,font=("Arial 10"),width="30",fg="red",bg="lightgray")
n1.place(x=220,y=50)
n2=Entry(Root,font=("Arial 10"),width="30",fg="red",bg="lightgray")
n2.place(x=220,y=80)
res=Label(Root,fg="black",bg="pink",font=("Arial 15 bold"),width="35")
res.place(x=40,y=130)
btnAdd=Button(Root,text="ADDITION",font=("Arial 10"),fg="white",bg="gray",width="15",command=add)
btnAdd.place(x=80,y=200)
btnSub=Button(Root,text="SUBTRACTION",font=("Arial 10"),fg="white",bg="gray",width="15",command=sub)
btnSub.place(x=270,y=200)
btnMul=Button(Root,text="MULTIPLICATION",font=("Arial 10"),fg="white",bg="gray",width="15",command=mul)
btnMul.place(x=80,y=250)
btnDiv=Button(Root,text="DIVISION",font=("Arial 10"),fg="white",bg="gray",width="15",command=div)
btnDiv.place(x=270,y=250)
btnDiv=Button(Root,text="REMENDAR",font=("Arial 10"),fg="white",bg="gray",width="15",command=rem)
btnDiv.place(x=175,y=300)



Root.mainloop()