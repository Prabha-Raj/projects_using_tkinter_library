#Currency Convertor using tkinter dropdown

from tkinter import *

def convTo():
	try:
		select1=menu1.get()
		select2=menu2.get()
		money=eval(en1.get())
	except NameError:
		res.configure(text="Only Allow Numeric Value")
	except SyntaxError:
		res.configure(text="Only Allow Numeric Value")

	if select1=="INR" and select2=="USD":
		usd=money*0.012				
		res.config(text=usd)
	elif select1=="INR" and select2=="EUR":
		eur=money*0.011
		res.config(text=eur)
	elif select1=="INR" and select2=="GBP":
		gbp=money*0.0096
		res.config(text=gbp)
	elif select1=="INR" and select2=="CAD":
		cad=money*0.016
		res.config(text=cad)
	elif select1=="INR" and select2=="AUD":
		aud=money*0.019
		res.config(text=aud)
	elif select1=="INR" and select2=="PKR":
		pkr=money*3.63
		res.config(text=pkr)
	elif select1=="USD" and select2=="INR":
		inr=money*82.60
		res.config(text=inr)
	elif select1=="USD" and select2=="EUR":				
		eur=money*0.92
		res.config(text=eur)
	elif select1=="USD" and select2=="GBP":
		gbp=money*0.79
		res.config(text=gbp)
	elif select1=="USD" and select2=="CAD":
		cad=money*1.36
		res.config(text=cad)
	elif select1=="USD" and select2=="AUD":
		aud=money*1.56
		res.config(text=aud)
	elif select1=="USD" and select2=="PKR":
		pkr=money*299.50
		res.config(text=pkr)
	elif select1=="EUR" and select2=="INR":
		inr=money*89.30
		res.config(text=inr)
	elif select1=="EUR" and select2=="USD":
		usd=money*1.08
		res.config(text=usd)
	elif select1=="EUR" and select2=="GBP":
		gbp=money*0.86
		res.config(text=gbp)
	elif select1=="EUR" and select2=="CAD":				
		cad=money*1.47
		res.config(text=cad)
	elif select1=="EUR" and select2=="AUD":
		aud=money*1.68
		res.config(text=aud)
	elif select1=="EUR" and select2=="PKR":
		pkr=money*323.74
		res.config(text=pkr)
	elif select1=="GBP" and select2=="INR":
		inr=money*104.12
		res.config(text=inr)
	elif select1=="GBP" and select2=="USD":
		usd=money*1.26
		res.config(text=usd)
	elif select1=="GBP" and select2=="EUR":
		eur=money*1.17
		res.config(text=eur)
	elif select1=="GBP" and select2=="CAD":
		cad=money*1.71
		res.config(text=cad)
	elif select1=="GBP" and select2=="AUD":
		aud=money*1.96
		res.config(text=aud)
	elif select1=="GBP" and select2=="PKR":
		pkr=money*377.62
		res.config(text=pkr)
	elif select1=="CAD" and select2=="INR":			
		inr=money*60.83
		res.config(text=inr)
	elif select1=="CAD" and select2=="USD":
		usd=money*0.74
		res.config(text=usd)
	elif select1=="CAD" and select2=="EUR":
		eur=money*0.68
		res.config(text=eur)
	elif select1=="CAD" and select2=="GBP":
		gbp=money*0.58
		res.config(text=gbp)
	elif select1=="CAD" and select2=="AUD":
		aud=money*1.15
		res.config(text=aud)
	elif select1=="CAD" and select2=="PKR":
		pkr=money*220.60
		res.config(text=pkr)

	elif select1=="AUD" and select2=="INR":		
		inr=money*53.04
		res.config(text=inr)
	elif select1=="AUD" and select2=="USD":
		usd=money*0.64
		res.config(text=usd)
	elif select1=="AUD" and select2=="EUR":
		eur=money*0.59
		res.config(text=eur)
	elif select1=="AUD" and select2=="GBP":
		gbp=money*0.51
		res.config(text=gbp)
	elif select1=="AUD" and select2=="CAD":
		cad=money*0.87
		res.config(text=cad)
	elif select1=="AUD" and select2=="PKR":
		pkr=money*192.31
		res.config(text=pkr)

	elif select1=="PKR" and select2=="INR":			#choice1=["INR","USD","EUR","GBP","CAD","AUD","PKR"]
		inr=money*0.28
		res.config(text=inr)
	elif select1=="PKR" and select2=="USD":
		usd=money*0.0033
		res.config(text=usd)
	elif select1=="PKR" and select2=="EUR":
		eur=money*0.0031
		res.config(text=eur)
	elif select1=="PKR" and select2=="GBP":
		gbp=money*0.0026
		res.config(text=gbp)
	elif select1=="PKR" and select2=="CAD":
		cad=money*0.0045
		res.config(text=cad)
	elif select1=="PKR" and select2=="AUD":
		aud=money*0.0052
		res.config(text=aud)

	else:
		res.config(text=money)

def switch():
	select1=menu1.get()
	select2=menu2.get()
	if select1=="Convert To" and select2=="Convert In":
		menu1.set(select1)
		menu2.set(select2)
	else:
		menu1.set(select2)
		menu2.set(select1)

root=Tk()	
root.geometry("500x400")
root.config(bg="orange")
root.title("Currency Converter")
root.resizable(False,False)
img = PhotoImage(file ="tampLogo.png")
root.iconphoto(True,img)
#bg = PhotoImage(file ="temp.png")
#label1 = Label( root, image = bg)
#label1.place(x=0,y=0)

lbl=Label(root,text="CURRENCY CONVERTER",font=("Arial 20 bold"),bg="red")
lbl.place(x=60,y=20)

menu1=StringVar()
menu1.set("INR")
choice1=["INR","USD","EUR","GBP","CAD","AUD","PKR"]
drop1= OptionMenu(root,menu1,*choice1)
drop1.place(x=20,y=100)
dir=Button(root,text="⇵",font=("Arial 15 bold"),height="2",width="4",bg="black",fg="white",command=switch)
dir.place(x=50,y=140)
menu2=StringVar()
menu2.set("INR")
choice2=["INR","USD","EUR","GBP","CAD","AUD","PKR"]
drop2= OptionMenu(root,menu2,*choice2)
drop2.place(x=20,y=220)

en1=Entry(root,font=("Arial 17 "),width="28",bg="white")
en1.place(x=120,y=100)

res=Label(root,font=("Arial 17 "),width="28",bg="white",fg="red")
res.place(x=120,y=220)

btn=Button(root,text="Convert",bg="black",font=("Calibery 20 bold"),fg="white",width="15",height="1",command=convTo)
btn.place(x=120,y=300)



root.mainloop()



