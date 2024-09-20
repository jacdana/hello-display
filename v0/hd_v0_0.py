from tkinter import *
from tkinter import ttk

## Hello Display

# A personal, pleasant informational display for Jac's living room.

## Version 0.0

# After running the program, the screen is filled with a black frame.
# Pressing "esc" ends the program thus closing the frame.


# Root window (fullscreen)
root = Tk()
root.attributes("-fullscreen", True)

# Stylist
stylist = ttk.Style()
stylist.configure("Black.TFrame", background="black")


# Main frame
mainframe = ttk.Frame(root)
mainframe["style"] = "Black.TFrame"
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Assign esc key to quit()
root.bind("<Escape>", quit)


# Mainloop
root.mainloop()
