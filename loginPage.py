from tkinter import *
from tkinter import Tk,ttk
from tkinter import messagebox
def ckpass():
 name=n1.get()
 password=str(n2.get())
 
 if name=="admin" and password=="admin":
  messagebox.showinfo("Login","Welcome  Admin!")
 elif name==credentials[0] and password==credentials[1]:
  messagebox.showinfo("Login","welcome Back "+credentials[0])
 else:
  messagebox.showwarning("Error","Check Username or Password")
def nwindow():
 lbl1=Label(root,text="Name*",font=("Poppins 12 "),bg="gray",fg="black")
 lbl1.place(x=15,y=150)
 
 lbl1=Label(root,text="welcome "+credentials[0],height=1,anchor=NW,bg="lightblue",fg="black",font=("poppins 12"))
 lbl1.place(x=15,y=150)


def ckpass():
 name=n1.get()
 password=str(n2.get())
 if name=="admin" and password=="admin":
  messagebox.showinfo("Login","Welcome Admin!")
 elif name==credentials[0] and password==credentials[1]:
  messagebox.showinfo("Login","welcome Back "+credentials[0])
  
  for widget in root.winfo_children():
   widget.destroy()
  for widget in root.winfo_children():
   widget.destroy()
  nwindow()
 else:
  messagebox.showwarning("Error","Invalid username or password")





 
root=Tk()
root.title("")
root.geometry("500x400")
root.resizable(False,False)
root.configure(bg="gray")
credentials=["Prabha","123"]
'''
frameup=Frame(root,width="300",height="50",bg="blue")
frameup.grid(row=0,column=0)
framedown=Frame(root,width="300",height="50",bg="blue")
framedown.grid(row=5,column=10)
'''
lbl=Label(root,text="LOGIN",fg="black",font=("Arial 30"),bg="gray")
lbl.place(x=10,y=25)
lab1=Label(root,bg="lightblue",width="65")
lab1.place(x=15,y=80)
lbl1=Label(root,text="Name*",font=("Poppins 12 "),bg="gray",fg="black")
lbl1.place(x=15,y=150)
n1=Entry(root,width="42",justify="left",font=("",15),highlightthickness=1)
n1.place(x=15,y=180)
lbl2=Label(root,text="Password*",font=("Poppins 12 "),height="1",bg="gray",fg="black",anchor=NW)
lbl2.place(x=15,y=230)
n2=Entry(root,width="42",justify="left",font=("",15),highlightthickness=1)
n2.place(x=15,y=260)
btn=Button(root,text="Login",bg="lightblue",width="66",height=2,font=("Ivy 9 bold"),command=ckpass)
btn.place(x=15,y=320)

root.mainloop()
