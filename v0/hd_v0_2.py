from tkinter import *
from tkinter import ttk


## Hello Display

# A personal, pleasant informational display for Jac's living room.

## Version 0.2

# The screen is filled with a colorful frame with the word "hello" in yellow hue center screen.
# Pressing "esc" ends the program thus closing the frame.

# Changelog:
#   - fixed the position of "hello"
#   - added colorful "sunrise" background
#   - the now yellow "hello" successfully sits on the background
#       without a containing rectangle (i.e. transparency works)

# Current bugs:
#   - There seems to be a small frame around the screen

# Notes
#   - changed code structure from:
#       root -> mainframe -> BG (Label) -> "hello" (Label)
#     to:
#       root -> canvas (then canvas draws bg and "hello")
#           * this makes the code easier and cleaner,
#             with the added benefit of removing the
#             gross "padx/pady" code from before!!

# Constants
WIDTH = 1920
HEIGHT = 1080

FONT = "Ratox"
# "hello" in Ratox font size 70 is 246 x 82 pixels
HELLO_WIDTH = 246
HELLO_HEIGHT = 82

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


# Stylist
stylist = ttk.Style()
stylist.configure("Black.TFrame", background="black")
stylist.configure(
    "WhiteText.TLabel", font=(FONT, 70), background="black", foreground="white"
)
# from photoshop: desired yellow = #F7E79A
stylist.configure(
    "SunsetText.TLabel", font=(FONT, 70), background="black", foreground="#F7E79A"
)


# Canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.grid()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Canvas creates Background
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=sunrise, anchor="center")


# Canvas creates "hello" w/ transparency
canvas.create_text(
    WIDTH / 2,
    HEIGHT / 2,
    text="hello",
    anchor="center",
    justify="center",
    font=(FONT, 70),
    fill="#F7E79A",
)


# Assign esc key to quit()
root.bind("<Escape>", quit)


# Mainloop
root.mainloop()
