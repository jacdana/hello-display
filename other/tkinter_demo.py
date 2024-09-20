from tkinter import *
from tkinter import ttk

# Code needed when pressing button "Calculate"
# why *args?
def calculate(*args):
    try:
        value = float(feet.get())
        meters_est = int(0.3048 * value * 10000.0 + 0.5)/10000.0
        meters.set(f"{meters_est:.3f}")
    except ValueError:
        pass

# Root window
root = Tk()
root.title("Feet to Meters")

# Main frame (parent = root)
mainframe = ttk.Frame(root, padding="3 12 3 12") #Left Top Right Bot
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # col, row = 0 makes it fill the whole root?
root.columnconfigure(0, weight=1) # the frame should resize to fit the window
root.rowconfigure(0, weight=1)

# "Feet" entry box (parent = mainframe)
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) # we can assign these objects variable names...
feet_entry.grid(column=2, row=1, sticky=(W, E))

# "Meters" decimal value output string (parent = mainframe)
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E)) # ...but we don't have to

# "Calculate" button (parent = mainframe)
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# Static text (parent = mainframe for all)
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Padding Shortcut
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# cursor starts in the "feet" entry box
feet_entry.focus()

# assign a hot key (return executes calculate)
root.bind("<Return>", calculate)

# Finally, we need to tell Tk to enter its event loop, 
# which is necessary for everything to appear onscreen 
# and allow users to interact with it.
root.mainloop()