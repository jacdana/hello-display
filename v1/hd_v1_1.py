from tkinter import *
from tkinter.ttk import *

import datetime
from random import choice
import requests

## Hello Display

# A personal, pleasant informational display for Jac's living room.

## Version 1.1

# The screen is filled with a colorful frame. A dynamic greeting,
# the current day, date, time and weather info are displayed on-screen
# Pressing "esc" ends the program thus closing the frame.

# Changelog:
#   - using NWS API, added current/low/high temps
#   - replaced the randomized emoji with one based on forecast
#   - adjusted layout to accomodate new content

# Current bugs:
#   - A small frame around the screen

# TODO: encapsulate?


# Constants
WIDTH = 1920
HEIGHT = 1080

FONT = "Ratox"
FONT_SIZE = 75
FONT_H = 135  # pixel height of FONT_SIZE sized 100

YLW = "#F7E79A"
BLU = "#3653D0"

GREETINGS = [
    "Hoot, hoot!",  # 12am -  3:59am
    "Early bird special!",  #  4am -  7:59am
    "Good morning!",  #  8am - 11:59am
    "Good afternoon!",  # 12pm -  3:59pm
    "Good evening!",  #  4pm -  7:59pm
    "Good night!",  #  8pm - 11:59pm
]

PATH_STR = "G:/Users/Jac/Desktop/OSSU/Personal/hello_display/resources/images/"


# Functions


def _right_now():
    return datetime.datetime.now()


# Based on the current time, change the text of the greeting
def greet():
    canvas.itemconfig(greeting, text=GREETINGS[_right_now().hour // 4])
    canvas.after(1000, greet)


def date_display():
    canvas.itemconfig(date, text=_right_now().strftime("%A, %B %d"))
    canvas.after(5000, date_display)


def time():
    canvas.itemconfig(clock, text=_right_now().strftime("%I:%M:%S %p"))
    canvas.after(250, time)


def weather():

    weather_json_periods = requests.get(
        "https://api.weather.gov/gridpoints/SGX/39,71/forecast/hourly"
    ).json()["properties"]["periods"]
    this_period = weather_json_periods[0]

    def _update_current_temp():
        canvas.itemconfig(temp_current, text=str(this_period["temperature"]) + "º")

    def _update_low_high():
        minimum = this_period["temperature"]
        maximum = minimum
        for i in range(1, 24):
            temp = weather_json_periods[i]["temperature"]
            if temp < minimum:
                minimum = temp
            elif temp > maximum:
                maximum = temp
        canvas.itemconfig(temp_low, text=f"{minimum}º")
        canvas.itemconfig(temp_high, text=f"{maximum}º")

    def _weather_emoji():
        sf = this_period["shortForecast"]
        match sf:
            case (
                "Showers And Thunderstorms Likely" | "Chance Showers And Thunderstorms"
            ):
                return e_cloud_with_lightning_and_rain
            case "Slight Chance Rain Showers":
                return e_cloud_with_rain
            case "Mostly Cloudy" | "Cloudy":
                return e_cloud
            case "Partly Sunny" | "Partly Cloudy":
                if 6 <= _right_now().hour < 18:
                    return e_sun_behind_cloud
                else:
                    return e_cloud
            case "Mostly Sunny" | "Sunny" | "Mostly Clear":
                if 6 <= _right_now().hour < 18:
                    return e_sun
                else:
                    return e_crescent_moon
            case "Patchy Fog":
                return e_wind_face
            case _:
                return e_see_no_evil_monkey

    _update_current_temp()
    _update_low_high()
    canvas.itemconfig(emoji, image=_weather_emoji())
    canvas.after(60000, weather)


# Root window (fullscreen)
root = Tk()

# root.attributes('-fullscreen',True)
# I'm facing issues with the geoemetry of things, and I'm
# not sure about the rules of the fullscreen method.
# I'm going to remove it for now and replace it with
# three lines of code that manually set the geometery of
# root to the hard-wired width and height of my screen.
root.geometry(f"{WIDTH}x{HEIGHT}")

# These lines get rid of the window elements to
# give the complete full-screen experience.
root.update_idletasks()
root.overrideredirect(True)

# Images (which must be defined after root())
sunrise = PhotoImage(file=PATH_STR + "sunrise_bg.png")

## Emojis
# possible additions: merperson, :D, ^^', XD,

e_unicorn = PhotoImage(file=PATH_STR + "emojis/unicorn.png")  # e_ = emoji PhotoImage
e_see_no_evil_monkey = PhotoImage(file=PATH_STR + "emojis/see-no-evil_monkey.png")

### Weather
e_sun = PhotoImage(file=PATH_STR + "emojis/sun.png")
e_crescent_moon = PhotoImage(file=PATH_STR + "emojis/crescent_moon.png")
e_sun_behind_cloud = PhotoImage(file=PATH_STR + "emojis/sun_behind_cloud.png")
e_cloud = PhotoImage(file=PATH_STR + "emojis/cloud.png")
e_cloud_with_rain = PhotoImage(file=PATH_STR + "emojis/cloud_with_rain.png")
e_cloud_with_lightning_and_rain = PhotoImage(
    file=PATH_STR + "emojis/cloud_with_lightning_and_rain.png"
)
e_wind_face = PhotoImage(file=PATH_STR + "emojis/wind_face.png")

ALL_EMJS = [
    e_unicorn,
    e_see_no_evil_monkey,
    e_sun,
    e_crescent_moon,
    e_sun_behind_cloud,
    e_cloud,
    e_cloud_with_rain,
    e_cloud_with_lightning_and_rain,
    e_wind_face,
]


# Canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, background="limegreen")
canvas.grid()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Background
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=sunrise, anchor="center")


# Greeting
greeting = canvas.create_text(
    WIDTH / 3,
    HEIGHT / 2 - FONT_H,
    text="Hello!",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill=YLW,
)


# Date
date = canvas.create_text(
    WIDTH / 3,
    HEIGHT / 2,
    text="Timey, Wimey Ballth",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill=YLW,
)


# Clock
clock = canvas.create_text(
    WIDTH / 3,
    HEIGHT / 2 + FONT_H + 20,
    text="CL: O'CK",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill=BLU,
)

# Emoji
emoji = canvas.create_image(
    WIDTH * 4 / 5 - 35,
    HEIGHT / 2 - 2 * FONT_H,
    image=e_unicorn,
    anchor="center",
)

# Temperature
## Current
temp_current = canvas.create_text(
    WIDTH * 4 / 5,
    HEIGHT / 2 - FONT_H / 2,
    text="CTº",
    anchor="center",
    justify="center",
    font=(FONT, 2 * FONT_SIZE),
    fill=YLW,
)

## Low
temp_low = canvas.create_text(
    WIDTH * 4 / 5 - 150,
    HEIGHT / 2 + FONT_H + 20,
    text="LOº",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill=BLU,
)

## High
temp_high = canvas.create_text(
    WIDTH * 4 / 5 + 100,
    HEIGHT / 2 + FONT_H + 20,
    text="HGº",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill=BLU,
)

# Assign esc key to quit()
root.bind("<Escape>", quit)


# Mainloop
greet()
date_display()
time()
weather()
root.mainloop()
