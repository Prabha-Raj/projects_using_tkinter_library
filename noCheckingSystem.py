#tkinter library practice

from tkinter import * 

def prime():
	try:
		a=eval(n1.get())
		count=0
		for i in range(1,a+1):
			if a%i==0:
				count+=1
		if count==2:
			res.config(text="It is A Prime No.")
		else:
			res.config(text="It is A Not Prime No.")
	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")
def odd():
	try:
		a=eval(n1.get())
		if a%2==0:
			res.config(text="It is A Even No.")
		else:
			res.config(text="It is A Odd No.")
	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")
def Arm():
	try:
		a=eval(n1.get())
		
		res.config(text=c)
	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")
def BtoD():
	try:
		num=eval(n1.get())
		ln=len(str(num))
		power=0
		bnum=0
		for i in range(ln):
			num1=num%10
			bnum=num1*(2**power)+bnum
			power+=1
			num//=10
		res.config(text=bnum)
	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")
def DtoB():
	try:
		num=int(n1.get())
		y=str()
		while num>0:
			y=str(num%2)+y
			num=num//2	
		y=int(y)
		res.config(text=y)

	except ValueError:
		res.config(text="Only allow Numeric Value")
	except NameError:
		res.config(text="Only allow Numeric Value")
	except SyntaxError:
		res.config(text="Only allow Numeric Value")


	
def fact():
	try:
		a=eval(n1.get())
		c=1
		for i in range(a,0,-1):
			c=c*i
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
Root.iconphoto(True,PhotoImage(file='calcLogo.png'))
Root.config(bg="pink")
Root.title("Number checker")					#title Function is change title of the box	
Root.geometry("500x400+290+90")				#geometry function is for set the widthxheigth+left+top
Root.resizable(False,False)
lbl1=Label(Root,text="Check Your Number",fg="black",bg="pink",font=("Arial 20 bold"))  #Label() is for set the properties of heading in the box
lbl1.place(x=130,y=0)					#place() function is to set the position text/heading
lbl2=Label(Root,text="Enter A Number : ",fg="black",bg="pink",font=("Arial 12 bold"))
lbl2.place(x=15,y=50)
n1=Entry(Root,font=("Arial 10"),width="30",fg="red",bg="lightgray")
n1.place(x=220,y=50)
res=Label(Root,fg="black",bg="pink",font=("Arial 15 bold"),width="35")
res.place(x=40,y=130)
btnPrime=Button(Root,text="Is Prime",font=("Arial 10"),fg="white",bg="gray",width="15",command=prime)
btnPrime.place(x=80,y=200)
btnOdd=Button(Root,text="Is Odd",font=("Arial 10"),fg="white",bg="gray",width="15",command=odd)
btnOdd.place(x=270,y=200)
btnArm=Button(Root,text="Binary To Decimal",font=("Arial 10"),fg="white",bg="gray",width="15",command=BtoD)
btnArm.place(x=80,y=250)
btnPali=Button(Root,text="Decimal To Binary",font=("Arial 10"),fg="white",bg="gray",width="15",command=DtoB)
btnPali.place(x=270,y=250)
btnFact=Button(Root,text="Find Factorial",font=("Arial 10"),fg="white",bg="gray",width="15",command=fact)
btnFact.place(x=175,y=300)



Root.mainloop()