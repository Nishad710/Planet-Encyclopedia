# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 10:10:01 2021

@author: HP
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.config(bg="lightblue")


Mercury = ImageTk.PhotoImage(Image.open ("mercury.jpg"))
Venus = ImageTk.PhotoImage(Image.open ("venus.jpg"))
Earth = ImageTk.PhotoImage(Image.open ("earth.jpg"))
Mars = ImageTk.PhotoImage(Image.open("mars.jpg"))
Jupiter = ImageTk.PhotoImage(Image.open("jupiter.jpg"))
Saturn = ImageTk.PhotoImage(Image.open("saturn.jpg"))
Uranus = ImageTk.PhotoImage(Image.open("uranus.jpg"))
Neptune = ImageTk.PhotoImage(Image.open("neptune.jpg"))
Sun = ImageTk.PhotoImage(Image.open("sun.jpg"))
Pluto = ImageTk.PhotoImage(Image.open("pluto.jpg"))

label_planet = Label(root, text="Planet : ", bg="lightblue")
label_planet_name = Label(root,font=("courier",18,"bold"),bg="lightblue")
label_planet_image = Label(root,bg="gold2", highlightthickness=5, borderwidth=2,relief=SOLID)
label_planet_gravity_radius = Label(root,font=("castellar"), bg="lightblue")
label_planet_info = Label(root,font=("courier",10,"bold"), bg="lightblue", wrap=500)

planets = ["Sun","Mercury","Venus", "Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvariable=selectedval)

def PlanetInfo():
    planet = selectedval.get()
    if planet == "Mercury":
        label_planet_name['text'] = "Mercury"
        label_planet_image['image'] = Mercury
        label_planet_gravity_radius['text'] = "Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        label_planet_info['text'] = "Mercury is the smallest planet in our solar system. ... Along with Venus, Earth, and Mars, Mercury is one of the rocky planets. It has a solid surface that is covered with craters. It has no atmosphere, and it doesn't have any moons."
    elif planet == "Sun":
        label_planet_name['text'] = "Sun"
        label_planet_image['image'] = Sun
        label_planet_info['text'] = "The sun is a star, a hot ball of glowing gases at the heart of our solar system. Its influence extends far beyond the orbits of distant Neptune and Pluto. ... The temperature at the sun's core is about 27 million degrees Fahrenheit. Average diameter: 864,000 miles, about 109 times the size of the Earth,Gravity: 274 m/s² and Radius: 696,340 km"
    elif planet == "Pluto":
        label_planet_name['text'] = "Pluto"
        label_planet_image['image'] = Pluto
        label_planet_gravity_radius['text'] = "Gravity: 0.62 m/s² /n Radius: 1,188.3 km"
        label_planet_info['text'] = "Pluto is about 3.6 billion miles away from the Sun and has five moons. Pluto's atmosphere is thin and composed mostly of nitrogen, methane and carbon monoxide. Pluto and its largest moon, Charon, are so similar in size that they orbit each other like a double planet system."
    elif planet == "Mars":
        label_planet_name['text'] = "Mars"
        label_planet_image['image'] = Mars
        label_planet_info['text'] = "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury.Mars is a terrestrial planet with a thin atmosphere, with surface features reminiscent of the impact craters of the Moon and the valleys, deserts and polar ice caps of Earth,Gravity: 3.721 m/s² and Radius: 3,389.5 km"
    elif planet == "Venus":
        label_planet_name['text'] = "Venus"
        label_planet_image['image'] = Venus
        label_planet_info['text'] = "Venus is the second planet from the Sun, and is Earth's closest neighbor in the solar system. Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky. The planet is a little smaller than Earth, and is similar to Earth inside,Gravity : 8.87 m/s² and Radius : 6,051.8 km"
    elif planet == "Earth":
        label_planet_name['text'] = "Earth"
        label_planet_image['image'] = Earth
        label_planet_info['text'] = "Earth, our home planet, is a world unlike any other. The third planet from the sun, Earth is the only place in the known universe confirmed to host life. With a radius of 3,959 miles, Earth is the fifth largest planet in our solar system, and it's the only one known for sure to have liquid water on its surface,Gravity : 9.807 m/s² and Radius : 6,371 km"
    elif planet == "Jupiter":
        label_planet_name['text'] = "Jupiter"
        label_planet_image['image'] = Jupiter
        label_planet_gravity_radius['text'] = "Gravity: 24.79 m/s² /n Radius: 69,911 km"
        label_planet_info['text'] = "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined, but slightly less than one-thousandth the mass of the Sun"
    elif planet == "Saturn":
        label_planet_name['text'] = "Saturn"
        label_planet_image['image'] = Saturn
        label_planet_gravity_radius['text'] = "Gravity: 10.44 m/s² /n Radius: 58,232 km"
        label_planet_info['text'] = "Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth.It only has one-eighth the average density of Earth; however, with its larger volume, Saturn is over 95 times more massive,Gravity: 10.44 m/s² and Radius: 58,232 km"
    elif planet == "Uranus":
        label_planet_name['text'] = "Uranus"
        label_planet_image['image'] = Uranus
        label_planet_gravity_radius['text'] = "Gravity: 8.87 m/s² /n Radius: 25,362 km"
        label_planet_info['text'] = "Uranus is known as the sideways planet because it rotates on its side. ... Uranus was the first planet found using a telescope. Uranus is an Ice Giant planet and nearly four times larger than Earth. Uranus has 27 known moons, most of which are named after literary characters"
    elif planet == "Neptune":
        label_planet_name['text'] = "Neptune"
        label_planet_image['image'] = Neptune
        label_planet_gravity_radius['text'] = "Gravity: 11.15 m/s² /n Radius: 24,622 km"
        label_planet_info['text'] = "Neptune is the eighth and farthest known Solar planet from the Sun. In the Solar System, it is the fourth-largest planet by diameter, the third-most-massive planet, and the densest giant planet. It is 17 times the mass of Earth, slightly more massive than its near-twin Uranus"
dropdown.place(relx=0.5, rely=0.1 , anchor=CENTER)

   
btn = Button(root, text="Show Planet Info" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

label_planet.place(relx=0.2, rely=0.1 , anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
label_planet_gravity_radius.place(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()