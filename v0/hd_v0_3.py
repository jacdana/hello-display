from tkinter import *
from tkinter.ttk import *

from time import strftime

## Hello Display

# A personal, pleasant informational display for Jac's living room.

## Version 0.3

# The screen is filled with a colorful frame. A (static) greeting
# and the current time are displayed on-screen
# Pressing "esc" ends the program thus closing the frame.

# Changelog:
#   - slightly increased font size (70 -> 100)
#   - changed greeting to "Hello!\nThe time is now"
#   - added a functioning clock below the greeting

# Current bugs:
#   - A small frame around the screen


# Constants
WIDTH = 1920
HEIGHT = 1080

CLOCK_W = 608
CLOCK_H = 165

FONT = "Ratox"


# Functions
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
    text="Hello!\nThe time is now",
    anchor="center",
    justify="center",
    font=(FONT, 100),
    fill="#F7E79A",
)


# Clock
clock = canvas.create_text(
    WIDTH / 2,
    HEIGHT / 2 + CLOCK_H / 2,
    text="CLOCK",
    anchor="center",
    justify="center",
    font=(FONT, 100),
    fill="#3653D0",
)

# Assign esc key to quit()
root.bind("<Escape>", quit)


# Mainloop
time()
root.mainloop()
