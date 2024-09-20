from tkinter import *
from tkinter.ttk import *

import datetime
from random import choice

## Hello Display

# A personal, pleasant informational display for Jac's living room.

## Version 1.0

# The screen is filled with a colorful frame. A dynamic greeting,
# the current day, date, time. and random emoji are displayed on-screen
# Pressing "esc" ends the program thus closing the frame.

# Changelog:
#   - there are now some stars in the bg
#   - added day and date
#   - added a randomized emoji (from small set)

# Current bugs:
#   - A small frame around the screen


# Constants
WIDTH = 1920
HEIGHT = 1080

CLOCK_W = 608
CLOCK_H = 165

FONT = "Ratox"
FONT_SIZE = 100
FONT_H = 135  # pixel height of FONT_SIZE sized FONT

GREETINGS = [
    "Hoot, hoot!",
    "Early bird special!",
    "Good morning!",
    "Good afternoon!",
    "Good evening!",
    "Good night!",
]

PATH_STR = "G:/Users/Jac/Desktop/OSSU/Personal/hello_display/resources/images/"


# Functions


def right_now():
    return datetime.datetime.now()


# Based on the current time, change the text of the greeting
def greet():
    canvas.itemconfig(greeting, text=GREETINGS[right_now().hour // 4])
    canvas.after(1000, greet)


def date_display():
    canvas.itemconfig(date, text=right_now().strftime("%A, %B %d"))
    canvas.after(5000, date_display)


def time():
    canvas.itemconfig(clock, text=right_now().strftime("%I:%M:%S %p"))
    canvas.after(250, time)


def randomize_emoji():
    canvas.itemconfig(emoji, image=choice(ALL_EMJS))
    canvas.after(5000, randomize_emoji)


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

e_unicorn = PhotoImage(file=PATH_STR + "emojis/unicorn.png")

### Weather
e_sun = PhotoImage(file=PATH_STR + "emojis/sun.png")
e_crescent_moon = PhotoImage(file=PATH_STR + "emojis/crescent_moon.png")
e_sun_behind_cloud = PhotoImage(file=PATH_STR + "emojis/sun_behind_cloud.png")
e_cloud = PhotoImage(file=PATH_STR + "emojis/cloud.png")
e_cloud_with_rain = PhotoImage(file=PATH_STR + "emojis/cloud_with_rain.png")
e_wind_face = PhotoImage(file=PATH_STR + "emojis/wind_face.png")

ALL_EMJS = [
    e_unicorn,
    e_sun,
    e_crescent_moon,
    e_sun_behind_cloud,
    e_cloud,
    e_cloud_with_rain,
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
    HEIGHT / 2 - FONT_H - 50,
    text="Hello!",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill="#F7E79A",
)


# Date
date = canvas.create_text(
    WIDTH / 2,
    HEIGHT / 2 - 50,
    text="Timey, Wimey Ballth",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill="#F7E79A",
)


# Clock
clock = canvas.create_text(
    WIDTH / 2,
    HEIGHT / 2 + FONT_H - 30,
    text="CL: O'CK",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill="#3653D0",
)

# Emoji
emoji = canvas.create_image(
    WIDTH / 2,
    HEIGHT / 2 + 2 * FONT_H,
    image=e_unicorn,
    anchor="center",
)

# Assign esc key to quit()
root.bind("<Escape>", quit)


# Mainloop
greet()
date_display()
time()
randomize_emoji()
root.mainloop()
