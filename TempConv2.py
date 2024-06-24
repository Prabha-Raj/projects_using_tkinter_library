#Temp conve using tkinter dropdown

from tkinter import *

def convTo():
	select1=menu1.get()
	select2=menu2.get()
	temp=eval(en1.get())
	if select1=="-Celsius --" and select2=="Fahrenheit":
		f=(((temp*9)/5)+32)
		res.config(text=f)
	elif select1=="Fahrenheit" and select2=="-Celsius --":
		c=(((temp-32)*5)/9)
		res.config(text=c)
	else:
		res.config(text=temp)

def switch():
	select1=menu1.get()
	select2=menu2.get()
	if select1=="-Celsius --" and select2=="Fahrenheit":
		menu1.set("Fahrenheit")
		menu2.set("-Celsius --")
	elif select1=="Fahrenheit" and select2=="-Celsius --":
		menu2.set("Fahrenheit")
		menu1.set("-Celsius --")
	elif select1=="Fahrenheit" and select2=="Fahrenheit":
		menu2.set("Fahrenheit")
		menu1.set("Fahrenheit")
	elif select1=="-Celsius --" and select2=="-Celsius --":
		menu2.set("-Celsius --")
		menu1.set("-Celsius --")
	else:
		menu1.set(select1)
		menu2.set(select2)

root=Tk()	
root.geometry("500x400")
root.config(bg="orange")
root.title("Temprature Converter")
root.resizable(False,False)
img = PhotoImage(file ="tampLogo.png")
root.iconphoto(True,img)
#bg = PhotoImage(file ="temp.png")
#label1 = Label( root, image = bg)
#label1.place(x=0,y=0)

lbl=Label(root,text="TEMPRATURE CONVERTER",font=("Arial 20 bold"),bg="red")
lbl.place(x=60,y=20)

menu1=StringVar()
menu1.set("Convert To")
drop1= OptionMenu(root,menu1,"- Celsius --","Fahrenheit")
drop1.place(x=20,y=100)

dir=Button(root,text="⇵",font=("Arial 15 bold"),height="2",width="4",bg="black",fg="white",command=switch)
dir.place(x=50,y=140)
menu2=StringVar()
menu2.set("Convert In")

drop2= OptionMenu(root,menu2,"Fahrenheit","-Celsius --")
drop2.place(x=20,y=220)

en1=Entry(root,font=("Arial 17 "),width="28",bg="white")
en1.place(x=120,y=100)

res=Label(root,font=("Arial 17 "),width="28",bg="white",fg="red")
res.place(x=120,y=220)

btn=Button(root,text="Convert",bg="black",font=("Calibery 20 bold"),fg="white",width="15",height="1",command=convTo)
btn.place(x=120,y=300)



root.mainloop()

