import tkinter as tk
from tkinter import ttk
import API
from PIL import ImageTk

root = tk.Tk()
bgColor = "#3d6466"

root.title("Weather Checker App")
# root.eval("tk::PlaceWindow . center")
x=root.winfo_screenwidth()//2
y=int(root.winfo_screenheight() *0.05)

root.geometry('430x932+' + str(x) + '+' + str(y))

frame1 = tk.Frame(root, width=430, height=932, bg=bgColor)
frame1.grid(row=1, column=0)
frame1.pack_propagate(False)

logoImage = ImageTk.PhotoImage(file="logo.png")

logoWidget = tk.Label(frame1, image=logoImage, bg=bgColor)
logoWidget.place(relx=0.5,
                 rely=0.15,
                 anchor='n'
                 )
logoWidget.image = logoImage
# logoWidget.pack()

textLabel =  tk.Label(frame1, 
         text="Enter Your Zipcode:", 
         bg=bgColor, 
         fg="white",
         font=("TKMenuFont", 14)
         )
textLabel.place(relx=0.5,
                rely=0.35,
                anchor='n')

input = tk.Entry(frame1, width=20, font=('TKMenuFont', 14))
input.place(relx=0.5,
            rely=0.4,
            anchor='n')

weatherInfoCity = tk.Label(frame1, 
                       text="", 
                       bg=bgColor, 
                       fg='white', 
                       font=('TKMenuFont', 16))

weatherInfo = tk.Label(frame1, 
                       text="", 
                       bg=bgColor, 
                       fg='white', 
                       font=('TKMenuFont', 14))

def getWeather():
    result = API.call(input.get())

    loc = result['name']
    desc = result['weather'][0]['description']
    temp = result['main']['temp']

    loc = loc.title()
    desc = desc.title()

    weatherInfoCity.config(text=loc)
    weatherInfo.config(text='Current Temperature: ' + str(temp) + 'F' + '\n' + desc)

goButton = tk.Button(frame1, 
                     text="Get Weather!", 
                     cursor="hand2", 
                     bg="#3d5a66", 
                     font=('TKHeaderFont', 16),
                     fg="white",
                     activebackground="#3d5aee",
                     command=getWeather)

goButton.place(relx=0.5,
            rely=0.55,
            anchor='n')

weatherInfoCity.place(relx=0.5,
                  rely=0.65,
                  anchor='n')

weatherInfo.place(relx=0.5,
                  rely=0.70,
                  anchor='n')

root.mainloop()