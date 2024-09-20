from tkinter import *
from tkinter.ttk import *

from datetime import *
import requests
import csv

## Hello Display

# A personal, pleasant informational display for Jac's living room.

## Version 1.2


# The screen is filled with a colorful frame. A dynamic greeting,
# the current day, date, time and weather info are displayed,
# as well as Jac's tutoring schedule for the day.
# Pressing "esc" ends the program thus closing the frame.

# Changelog:
#   - tried to clean up the weather emoji function
#   - lowered FONT_H, therefore changing the vertical spacing of display elements
#   - changed the low/high temps from 24-hr measurements to 12-hr measurements
#   - added functionality to read Jac's tutoring schedule from an csv and display today's students
#   - added schedule to the display and everything got moved around


# TODO: encapsulate?


# Constants
WIDTH = 1920
HEIGHT = 1080

FONT = "Ratox"
FONT_SIZE = 75
FONT_H = (FONT_SIZE * 135) // 100
SCHED_FONT = "Apercu Mono Pro"
SCHED_FONT_SIZE = FONT_SIZE

YLW = "#F7E79A"
BLU = "#3653D0"

GREETINGS = [
    "Hoot, hoot!",  # 12am -  3:59am
    "Early bird special!",  #  4am -  7:59am
    "Morning, sunshine!",  #  8am - 11:59am
    "Good afternoon!",  # 12pm -  3:59pm
    "Good evening!",  #  4pm -  7:59pm
    "Good night!",  #  8pm - 11:59pm
]

PATH_STR = "G:/Users/Jac/Desktop/OSSU/Personal/hello_display/resources/images/"


# Functions


def _right_now():
    return datetime.now()


# Based on the current time, change the text of the greeting
def greet():
    canvas.itemconfig(greeting, text=GREETINGS[_right_now().hour // 4])
    canvas.after(5000, greet)


def date_display():
    canvas.itemconfig(today, text=_right_now().strftime("%A, %B %d"))
    canvas.after(5000, date_display)


def clock_time():
    canvas.itemconfig(clock, text=_right_now().strftime("%I:%M:%S %p"))
    canvas.after(250, clock_time)


def weather():

    weather_json_periods = requests.get(
        "https://api.weather.gov/gridpoints/SGX/39,71/forecast/hourly"
    ).json()["properties"]["periods"]
    this_period = weather_json_periods[0]

    # for testing:
    # this_period = {"temperature":1314,"shortForecast":"Bubbly"}

    def _update_current_temp():
        canvas.itemconfig(temp_current, text=str(this_period["temperature"]) + "º")

    def _update_low_high():
        low = this_period["temperature"]
        high = low
        for i in range(1, 12):
            temp = weather_json_periods[i]["temperature"]
            if temp < low:
                low = temp
            elif temp > high:
                high = temp
        canvas.itemconfig(temp_low, text=f"{low}º")
        canvas.itemconfig(temp_high, text=f"{high}º")

    def _weather_emoji():

        def _simplify_weather(wthr_str):
            if "Thunderstorms" in wthr_str:
                return "thunder"
            elif "Rain" in wthr_str:
                return "rain"
            elif (wthr_str == "Mostly Cloudy") or (wthr_str == "Cloudy"):
                return "cloud"
            elif (wthr_str == "Partly Sunny") or (wthr_str == "Partly Cloudy"):
                return "part_cloud"
            elif ("Sunny" in wthr_str) or ("Clear" in wthr_str):
                return "clear"
            elif "Fog" in wthr_str:
                return "fog"
            else:
                return "not_found"

        match _simplify_weather(this_period["shortForecast"]):
            case "thunder":
                return e_cloud_with_lightning_and_rain
            case "rain":
                return e_cloud_with_rain
            case "cloud":
                return e_cloud
            case "part_cloud":
                if 6 <= _right_now().hour < 18:
                    return e_sun_behind_cloud
                else:
                    return e_cloud
            case "clear":
                if 6 <= _right_now().hour < 18:
                    return e_sun
                else:
                    return e_crescent_moon
            case "fog":
                return e_wind_face
            case _:
                return e_see_no_evil_monkey

    _update_current_temp()
    _update_low_high()
    canvas.itemconfig(emoji, image=_weather_emoji())
    canvas.after(60000, weather)


def schedule():

    this_moment = _right_now()
    # for testing:
    # this_moment = datetime(2024, 4, 3, 12, 12)

    def _sort_by_type(sesh):
        match sesh["type"]:
            case "recurring":
                return 0
            case "one-time":
                return 1
            case "cancelation":
                return 2

    def _weekday_str(day_int):
        match day_int:
            case 0:
                return "Monday"
            case 1:
                return "Tuesday"
            case 2:
                return "Wednesday"
            case 3:
                return "Thursday"
            case 4:
                return "Friday"
            case 5:
                return "Saturday"
            case 6:
                return "Sunday"

    todays_sched = []

    for sesh in sorted(jacs_schedule, key=_sort_by_type):
        if sesh["type"] == "recurring" and sesh["day"] == _weekday_str(
            this_moment.weekday()
        ):
            todays_sched.append(sesh)
        elif (
            sesh["type"] == "cancelation"
            and sesh["date"]
            == f"{this_moment.month}/{this_moment.day}/{this_moment.year}"
        ):
            for i in range(len(todays_sched)):
                if todays_sched[i]["name"] == sesh["name"]:
                    del todays_sched[i]
                    break
        elif (
            sesh["type"] == "one-time"
            and sesh["date"]
            == f"{this_moment.month}/{this_moment.day}/{this_moment.year}"
        ):
            todays_sched.append(sesh)

    sched_str = ""
    for session in sorted(todays_sched, key=lambda session: session["start"]):
        sched_str += f"{session['start']} - {session['end']}   {session['name']}\n"

    canvas.itemconfig(sched, text=sched_str)
    canvas.after(600000, schedule)


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
    WIDTH / 2,
    HEIGHT / 4 - FONT_H - 75,
    text="Hello!",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill=YLW,
)


# Date
today = canvas.create_text(
    WIDTH / 2,
    HEIGHT / 4 - 75,
    text="Timey, Wimey Ballth",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill=YLW,
)


# Clock
clock = canvas.create_text(
    WIDTH / 2,
    HEIGHT / 4 + FONT_H - 75,
    text="CL: O'CK",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill=BLU,
)

# Emoji (currently representing the current weather)
emoji = canvas.create_image(
    WIDTH * 1 / 5 - 70,
    HEIGHT / 2 - 3 * FONT_H // 2,
    image=e_unicorn,
    anchor="center",
)

# Temperature
## Current
temp_current = canvas.create_text(
    WIDTH * 1 / 5 - 50,
    HEIGHT / 2 + FONT_H // 2,
    text="CTº",
    anchor="center",
    justify="center",
    font=(FONT, 2 * FONT_SIZE),
    fill=YLW,
)

## Low
temp_low = canvas.create_text(
    WIDTH * 1 / 5 - 200,
    HEIGHT / 2 + 3 * FONT_H // 2 + 50,
    text="LOº",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill=BLU,
)

## High
temp_high = canvas.create_text(
    WIDTH * 1 / 5 + 50,
    HEIGHT / 2 + 3 * FONT_H // 2 + 50,
    text="HGº",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill=BLU,
)


## Jac's Schedule
sched_title = canvas.create_text(
    WIDTH * 3 // 5,
    HEIGHT / 2 - 3 * FONT_H // 2 + 20,
    text="Jac's Schedule",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE * 3 // 5),
    fill=YLW,
)

sched = canvas.create_text(
    WIDTH * 3 // 10,
    HEIGHT / 2 - FONT_H + 20,
    text="WHAT? NOTHING",
    anchor="nw",
    justify="left",
    font=(FONT, FONT_SIZE * 3 // 5),
    fill=BLU,
)

# Assign esc key to quit()
root.bind("<Escape>", quit)


# Mainloop
jacs_schedule = []  # will be a list of dicts, each dict representing one session
with open(
    "G:/Users/Jac/Desktop/OSSU/Personal/hello_display/resources/jacs_schedule.csv"
) as schedule_csv:
    Rozs_desk = csv.DictReader(schedule_csv)
    for work in Rozs_desk:
        jacs_schedule.append(
            {
                "type": work["Type"],
                "name": work["Name"],
                "day": work["Day"],
                "date": work["Date"],
                "start": work["Start"],
                "end": work["End"],
            }
        )
greet()
date_display()
clock_time()
weather()
schedule()
root.mainloop()
