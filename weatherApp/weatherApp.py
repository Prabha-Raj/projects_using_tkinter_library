#Weather App


from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import math


root=Tk()
root.title("Weather App")
root.geometry("900x500+40+40")
root.resizable(False,False)
root.config(bg="lightgray")

def images(description1):
    if description1=='Haze':
        img="img/haze.png"
    elif description1=='Clear':
        img="img/clear.png"
    elif description1=='Clouds':
        img="img/clouds.png"
    elif description1=='Drizzle':
        img="img/drizzle.png"
    elif description1=='Mist':
        img="img/mist.png"
    elif description1=='Rain':
        img="img/rain.png"
    elif description1=='Snow':
        img="img/snow.png"
    else:
        img="img/logo.png"
    Logo_image1=PhotoImage(file=img).subsample(3)
    logo1=Label(root,image=Logo_image1,bg="lightgray")
    logo1.place(x=650,y=40)
    
def getWeather():
	city=textfield.get()
	geolocator= Nominatim(user_agent="geoapiExercises")
	print(city)
	location= geolocator.geocode(city)
	obj= TimezoneFinder()
	result= obj.timezone_at(lng=location.longitude,lat=location.latitude)
	print(result)
	

	home=pytz.timezone(result)
	local_time=datetime.now(home)
	current_time=local_time.strftime("%I:%M:%S %p")
	
	clock.config(text=current_time)
	name.config(text="CURRENT WEATHER")
	

	#Weather
	#const apiUrl="https://api.openweathermap.org/data/2.5/weather?units=metric&q=";
	#const apikey="7bd851f41aa8d4d1220642c55cf519d2";
	#3daaea7453fe79d045024245ab60ed32
	
	
	api="https://api.openweathermap.org/data/2.5/weather?units=metric&q="+city+"&appid=7bd851f41aa8d4d1220642c55cf519d2"
	print(api)
	json_data=requests.get(api).json()
	print(json_data)
	condition=json_data['weather'][0]['main']
	print(condition)
	description1= json_data['weather'][0]['description']
	print(description1)
	temp= math.floor(json_data['main']['temp'])
	feels_like=math.floor(json_data['main']['feels_like'])
	pressure= json_data['main']['pressure']
	humidity= json_data['main']['humidity']
	wind = json_data['wind']['speed']
	t.config(text=(temp,"°"))
	c.config(text=(condition,"|","FEELS","LIKE",str(feels_like),"°"))

	w.config(text=str(wind)+" km/h")
	h.config(text=str(humidity)+" %")
	d.config(text=description1)
	p.config(text=pressure)
	
	images(condition)


#Search box
search_image=PhotoImage(file="img/search.png")
myimage=Label(image=search_image,bg="lightgray")
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins 25 bold"),bg="#404040",border=2,fg="white")
textfield.place(x=53,y=38)
textfield.focus()


Search_icon=PhotoImage(file="img/search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=33)


#logo
Logo_image=PhotoImage(file="img/logo.png")
logo=Label(image=Logo_image,bg="lightgray")
logo.place(x=150,y=100)



#bottom box

Frame_image=PhotoImage(file="img/box.png")
frame_myimage=Label(root,image=Frame_image,bg="lightgray")
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

name=Label(root,font=("arial 15 bold"),bg="lightgray")
name.place(x=30,y=100)
clock=Label(root,font="Healvtica 20",bg="lightgray")
clock.place(x=30,y=130)


#label
label1=Label(root,text="WIND",font=("Helvetica 15 bold"),fg="white",bg="#1ab5ef")
label1.place(x=140,y=400)

wind_image=PhotoImage(file="img/wind.png").subsample(2)
label11=Label(root,image=wind_image,font=("Helvetica 15 bold"),fg="white",bg="#1ab5ef")
label11.place(x=85,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica 15 bold"),fg="white",bg="#1ab5ef")
label2.place(x=300,y=400)
humidity_image=PhotoImage(file="img/humidity.png").subsample(2)
label21=Label(root,image=humidity_image,font=("Helvetica 15 bold"),fg="white",bg="#1ab5ef")
label21.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica 15 bold"),fg="white",bg="#1ab5ef")
label3.place(x=440,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica 15 bold"),fg="white",bg="#1ab5ef")
label4.place(x=695,y=400)

t=Label(font="arial 70 bold",fg="#ee666d",bg="lightgray")
t.place(x=400,y=150)
c=Label(font="arial 15 bold",bg="lightgray")
c.place(x=400,y=250)

w=Label(text="....",font="arial 20 bold",bg="#1ab5ef")
w.place(x=120,y=440)
h=Label(text="....",font="arial 20 bold",bg="#1ab5ef")
h.place(x=320,y=440)
d=Label(text="....",font="arial 20 bold",bg="#1ab5ef")
d.place(x=440,y=440)
p=Label(text="....",font="arial 20 bold",bg="#1ab5ef")
p.place(x=720,y=440)





root.mainloop()