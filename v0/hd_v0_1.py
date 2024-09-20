from tkinter import *
from tkinter import ttk

## Hello Display

# A personal, pleasant informational display for Jac's living room.

## Version 0.1

# The screen is filled with a black frame with the word "hello" in white center screen.
# Pressing "esc" ends the program thus closing the frame.

# Changelog:
#   -added "hello"

# Constants
WIDTH = 1920
HEIGHT = 1080

FONT = "Ratox"

# Root window (fullscreen)
root = Tk()
root.attributes("-fullscreen", True)

# Stylist
stylist = ttk.Style()
stylist.configure("Black.TFrame", background="black")
# stylist.configure('Sunrise.TFrame', ...)
stylist.configure(
    "WhiteText.TLabel", font=(FONT, 70), background="black", foreground="white"
)
# stylist.configure('Sunrise.TLabel', ...)


# Main frame
mainframe = ttk.Frame(root)
mainframe["style"] = "Black.TFrame"
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)  # I need this to stretch it to full screen
root.rowconfigure(0, weight=1)

# Greeting Widget
greet = ttk.Label(
    mainframe, text="hello", justify="center", style="WhiteText.TLabel", anchor="center"
)
greet.grid()
greet.grid_configure(
    padx=(WIDTH / 2) - 120, pady=(HEIGHT / 2) - 120
)  # a little ugly but it works


# Assign esc key to quit()
root.bind("<Escape>", quit)


# Mainloop
root.mainloop()
