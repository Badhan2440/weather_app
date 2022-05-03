from tkinter import *  # for GUI
from configparser import ConfigParser
from tkinter import messagebox

# popup error message bos
import requests


url_api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file = "weather.key"
file_a = ConfigParser()  # read out the api from file
file_a.read(api_file)
api_key = file_a["api_key"]["key"]


def weather_find(city):
    final = requests.get(url_api.format(city, api_key))
    if final:
        json_file = final.json()
        city = json_file["name"]
        country_name = json_file["sys"]["country"]
        key_temp = json_file["main"]["temp"]
        c_temp = key_temp - 273.15
        f_temp = (key_temp - 273.15) * 9 / 5 + 32
        weather_disp = json_file["weather"][0]["main"]
        result = (city, country_name, c_temp, f_temp, weather_disp)
        return result
    else:
        return None


def print_weather():
    city = search_city.get()
    weather = weather_find(city)
    if weather:
        location_entry["text"] = "{},{}".format(weather[0], weather[1])
        temperature_entry["text"] = "{:.2f} C, {:.2f} F".format(weather[2], weather[3])
        weather_entry["text"] = weather[4]

    else:
        messagebox.showerror("Error", "Please enter a valid city name")


# making tkinter  display window
root = Tk()
root.title("Weather app")
root.config(background="black")
root.geometry("700x600")


# making enter city name box
search_city = StringVar()
entry_city = Entry(root, textvariable=search_city, fg="red", font=("Arial", 30, "bold"))
entry_city.pack()  # pack function to show all design in tkinter window


# making search button
search_button = Button(
    root,
    text="Search weather",
    width=20,
    bg="red",
    fg="white",
    font=("Arial", 20, "bold"),
    command=print_weather,
)
search_button.pack()


# location of the particular city will appear
location_entry = Label(root, text="", font=("Arial", 35, "bold"), bg="orange")
location_entry.pack()


# Showing temperature
temperature_entry = Label(root, text="", font=("Arial", 25, "bold"), bg="green")
temperature_entry.pack()


# showing weather
weather_entry = Label(root, text="", font=("Arial", 30, "bold"), bg="blue")
weather_entry.pack()


root.mainloop()
