# translate


from tkinter import *
import googletrans
from googletrans import Translator

def translate():
    ent= text1.get(1.0,END)
    st=menu.get()
    st1=menu1.get()
    t = Translator()
    tt = t.translate(ent, src=st, dest=st1)
    res.config(text=tt.text)

root=Tk()
root.title("Translate")
root.geometry("500x500")
root.resizable(False,False)
root.config(bg="yellow")


lbl=Label(root,text="TRANSLATOR",font=("Calibri 20 bold"),fg="blue")
lbl.place(x=170,y=10)

language=googletrans.LANGUAGES
langv=list(language.values())
lang1=language.keys()
# lang1 = {"English", "Hindi"}
# langv = {"English", "Hindi"}
menu=StringVar()
menu.set("Select")
drop=OptionMenu(root,menu,*langv)
drop.place(x=250,y=50,width=200)

lbl1=Label(root,text="Text",font=("Calibri 15"),bg="black",fg="white")
lbl1.place(x=30,y=50)
text1=Text(root,font=("Arial 15"),height="3",width="28",border="1",bg="lightblue")
text1.place(x=30,y=100)
lbl2=Label(root,text="Translate",font=("Calibri 15"),bg="black",fg="white")
lbl2.place(x=30,y=230)

menu1=StringVar()
menu1.set("Select")
drop1=OptionMenu(root, menu1, *langv)
drop1.place(x=250,y=230,width=200)

btn=Button(root,text="Translate",font=("Arial 15 bold"),fg="White",bg="black",command=translate)
btn.place(x=365,y=115)
res=Label(root,font=("Arial 15"),fg="blue",bg="lightgray",width="35",height="7")
res.place(x=50,y=280)
root.mainloop()