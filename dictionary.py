#Dictinary by using tkinter 

from tkinter import *
def search():
	word=ent.get()
	word=word.upper()
	dict={
	"OOPS":"Object Oriented Programing System",
	"JS":"JavaScript",
	"OOPL":"Object Oriented Programming Language",
	"OBPL":"Object Base Programming Language",
	"HTML":"Hyper Text Markup Language",
	"CSS":"Cashcading Stylesheet",
	"PHP":"Hyper Text Processor",
	"HTTP":"Hyper Text Transfer Protocol",
	"HTTPS":"Hyper Text Transfer Protocol Secure",
	"AI":"Artificial Intelligence",	
	"ML":"Machine Learning",
	"GUI":"Graphical User Interface",
	"WWW":"World Wide Web",
	"CUI":"Character User Interface",
	"IOT":"Internet Of Things",
	"IP":"Internet Protocol",
	"API":"Application Programming Interface",
	"GF":"Gobar Fekne Wali"
	}
	if word in dict:
		res.config(text=dict[word])
	else:
		res.config(text="Not Found")


root=Tk()
root.geometry("500x400+300+100")
root.resizable(False,False)
root.title("Oxford Dictinary")
root.config(bg="yellow")
lbl1=Label(root,text="OXFORD DICTIONARY",bg="black",fg="white",fon=("Calibri 20 bold"),width="40")
lbl1.pack()
lbl2=Label(root,text="Enter  Word  that you want to Search",font=("Calibri 10 bold"),bg="cyan",fg="red",)
lbl2.place(x=150,y=80)

ent=Entry(root,font=("Calibri 10 bold"),bg="lightblue",fg="black",border="5" ,width="29")
ent.place(x=150,y=120)
btn=Button(root,font=("Calibri 17 bold"),text="SEARCH",bg="black",fg="white",width="10",command=search)
btn.place(x=190,y=190)

res=Label(root,font=("Calibri 15 bold"),bg="lightblue",fg="red",width="35")
res.place(x=90,y=300)

root.mainloop()