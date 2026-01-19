import requests
import json
import tkinter as tk
from PIL import Image, ImageTk

out=""

def getWeather():
    API_LOCATE = "696e2e404c470223308291dovcc1547"

    url_locate = "https://geocode.maps.co/search?"
    address = input_box.get()
    params = {"q":address,
            "api_key":API_LOCATE}
    data = requests.get(url_locate,params=params)
    data = data.json()
    try:
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])

        url_1 = "https://api.open-meteo.com/v1/forecast?"
        params_1 = {"latitude":lat,
                    "longitude":lon,
                    "current":"temperature_2m,rain,precipitation,is_day,snowfall"
                    }

        weather = requests.get(url_1,params=params_1)
        weather = weather.json()
        printWeather(weather)
    except IndexError:
        global out
        out = "Invalid Location"
        display.config(text=out)

def printWeather(weather):
    global bg_color, pic

    if weather["current"]["is_day"] == 0:
        bg_color = "midnight blue"
        pil_image = Image.open("night-mode.png").convert("RGBA").resize((75, 75), Image.Resampling.LANCZOS)
        pic = ImageTk.PhotoImage(pil_image)
        picLabel.config(image=pic)
    else:
        bg_color = "sky blue"
        pil_image = Image.open("sun-cloud.png").convert("RGBA").resize((50, 50), Image.Resampling.LANCZOS)
        pic = ImageTk.PhotoImage(pil_image)
        picLabel.config(image=pic)

    out = f"Temperature now: {weather['current']['temperature_2m']}\nRain Today: {weather['current']['rain']}\nSnow Today:{weather['current']['snowfall']}"
    display.config(text=out, bg=bg_color)
    canvas.config(bg=bg_color)
    input_box.config(bg="white")
    head.config(bg=bg_color)
    picLabel.config(bg=bg_color)
    title_frame.config(bg=bg_color)
    root.configure(bg=bg_color)

def clear_placeholder(event):
    if input_box.get() == "Enter your address...":
        input_box.delete(0, tk.END)
        input_box.config(fg="black")

#GUI
font = "Bauhaus 93"
bg_color = "sky blue"

root = tk.Tk()
root.geometry("500x500")
root.configure(background=bg_color)
title_frame = tk.Frame(root, bg=bg_color)
title_frame.pack(padx=30, pady=30)

head = tk.Label(title_frame, font=(font, 35), bg=bg_color, fg="white", text="Weather App")
head.pack(side="left")

pil_image = Image.open("sun-cloud.png")
pil_image = pil_image.convert("RGBA")
pil_image = pil_image.resize((50, 50), Image.Resampling.LANCZOS)
pic = ImageTk.PhotoImage(pil_image)
picLabel = tk.Label(title_frame, image=pic, bg=bg_color)
picLabel.pack(side="left", padx=20)

input_box = tk.Entry(root,bg="light sky blue",font=("Britannic Bold",25),fg="grey")
input_box.insert(0, "Enter your address...")
input_box.bind("<FocusIn>", clear_placeholder)
input_box.pack(padx=10,pady=10)

enter = tk.Button(root,bg="white",text="Press to get Weather",width=200,font=("Fixedsys",20),fg=bg_color,command=getWeather)
enter.pack(pady=10)

canvas = tk.Canvas(root,bg=bg_color,border=0)
canvas.pack(fill="both", expand=True)

display = tk.Label(canvas,text=out,bg ='sky blue',font=("Britannic Bold",20),fg="white")
display.pack(padx=5,pady=5)

print(input_box.get())

root.mainloop()
