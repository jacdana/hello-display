from tkinter import *
from tkinter.ttk import *

from time import *

## Hello Display

# A personal, pleasant informational display for Jac's living room.

## Version 0.4

# The screen is filled with a colorful frame. A dynamic greeting
# and the current time are displayed on-screen
# Pressing "esc" ends the program thus closing the frame.

# Changelog:
#   - changed the greeting to be dynamic.
#       - 12am -  4am : Hoot, hoot!
#       -  4am -  8am : Early bird special!
#       -  8am - 12pm : Good morning!
#       - 12pm -  4pm : Good afternoon!
#       -  4pm -  8pm : Good evening!
#       -  8pm - 12am : Good night!
#   - added a functioning clock below the greeting

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

# Functions


# Based on the current time, change the text of the greeting
def greet():
    canvas.itemconfig(greeting, text=GREETINGS[localtime().tm_hour // 4])
    canvas.after(1000, greet)


def time():
    canvas.itemconfig(clock, text=strftime("%I:%M:%S %p"))
    canvas.after(250, time)


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


# Background image
sunrise = PhotoImage(
    file="G:/Users/Jac/Desktop/OSSU/Personal/hello_display/resources/images/sunrise_bg.png"
)


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
    HEIGHT / 2 - CLOCK_H,
    text="Hello!",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill="#F7E79A",
)


# Clock
clock = canvas.create_text(
    WIDTH / 2,
    HEIGHT / 2 + CLOCK_H / 2,
    text="CLOCK",
    anchor="center",
    justify="center",
    font=(FONT, FONT_SIZE),
    fill="#3653D0",
)

# Assign esc key to quit()
root.bind("<Escape>", quit)


# Mainloop
greet()
time()
root.mainloop()
