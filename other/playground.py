# # Import tkinter library
# from tkinter import *

# # Create an instance of tkinter frame or window
# win = Tk()

# # Set the geometry of tkinter frame
# win.geometry("750x250")

# # Create a Text widget
# text= Label(win, text=" Hello\nWelcome to Tutorialspoint.com!",font=('Century Schoolbook', 20, 'italic bold'))
# text.pack(pady=30)

# win.attributes('-fullscreen',True)

# win.mainloop()


# # Finding all the options for a given widget
# import tkinter as tk
# import tkinter.ttk as ttk

# def stylename_elements_options(stylename):
#     '''Function to expose the options of every element associated to a widget
#        stylename.'''
#     try:
#         # Get widget elements
#         style = ttk.Style()
#         layout = str(style.layout(stylename))
#         print('Stylename = {}'.format(stylename))
#         print('Layout    = {}'.format(layout))
#         elements=[]
#         for n, x in enumerate(layout):
#             if x=='(':
#                 element=""
#                 for y in layout[n+2:]:
#                     if y != ',':
#                         element=element+str(y)
#                     else:
#                         elements.append(element[:-1])
#                         break
#         print('\nElement(s) = {}\n'.format(elements))

#         # Get options of widget elements
#         for element in elements:
#             print('{0:30} options: {1}'.format(
#                 element, style.element_options(element)))

#     except tk.TclError:
#         print('_tkinter.TclError: "{0}" in function'
#               'widget_elements_options({0}) is not a recognised stylename.'
#               .format(stylename))

# stylename_elements_options('TLabel')


## For listing the available fonts on this computer
# from tkinter import Tk, font
# root = Tk()
# for f in font.families():
#     print(f)


# # make a simple drawing pad w/ canvas
# from tkinter import *
# from tkinter import ttk

# def savePosn(event):
#     global lastx, lasty
#     lastx, lasty = event.x, event.y

# def addLine(event):
#     canvas.create_line((lastx, lasty, event.x, event.y))
#     savePosn(event)

# root = Tk()
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# canvas = Canvas(root)
# canvas.grid(column=0, row=0, sticky=(N, W, E, S))
# canvas.bind("<Button-1>", savePosn)
# canvas.bind("<B1-Motion>", addLine)

# root.mainloop()


# # Clock using label
# # importing whole module
# from tkinter import *
# from tkinter.ttk import *

# # importing strftime function to
# # retrieve system's time
# from time import strftime

# # creating tkinter window
# root = Tk()
# root.title('Clock')

# # This function is used to
# # display time on the label

# def time():
#     string = strftime('%H:%M:%S %p')
#     lbl.config(text=string)
#     lbl.after(1000, time)


# # Styling the label widget so that clock
# # will look more attractive
# lbl = Label(root, font=('calibri', 40, 'bold'),
#             background='purple',
#             foreground='white')

# # Placing clock at the centre
# # of the tkinter window
# lbl.pack(anchor='center')
# time()

# mainloop()

# from datetime import *

# print(type(datetime.now().time))


# https://api.weather.gov/points/33.9167,-117.9001

# https://api.weather.gov/gridpoints/SGX/39,71/forecast
# https://api.weather.gov/gridpoints/SGX/39,71/forecast/hourly


## API/json practice
# import json
# import requests

# weather_json = requests.get("https://api.weather.gov/gridpoints/SGX/39,71/forecast/hourly").json()

# print(weather_json)
# print(json.dumps(weather_json,indent=2)[:1000]) #better way to display the data
# print(weather_json.keys())

# print(weather_json["properties"]["periods"][0]["shortForecast"])
# print(weather_json["properties"]["periods"][0]["startTime"])
# print(weather_json["properties"]["periods"][0]["temperature"])

# import json
# import requests

# weather_json_periods = requests.get("https://api.weather.gov/gridpoints/SGX/39,71/forecast/hourly").json()["properties"]["periods"]

# short_forecasts = []
# for i in range (150):
#     sf = weather_json_periods[i]["shortForecast"]
#     if sf not in short_forecasts:
#         short_forecasts.append(sf)
# print(*short_forecasts,sep="\n")


## csv practice
# import csv

# schedule = []

# with open(
#     "G:/Users/Jac/Desktop/OSSU/Personal/hello_display/resources/jacs_schedule.csv"
# ) as jacs_schedule:
#     Rozs_desk = csv.DictReader(jacs_schedule)
#     for work in Rozs_desk:
#         schedule.append(
#             {
#                 "type": work["Type"],
#                 "name": work["Name"],
#                 "day": work["Day"],
#                 "date": work["Date"],
#                 "start": work["Start"],
#                 "end": work["End"],
#             }
#         )


# def sort_by_type(sesh):
#     match sesh["type"]:
#         case "recurring":
#             return 0
#         case "one-time":
#             return 1
#         case "cancelation":
#             return 2



# for sesh in sorted(schedule,key=sort_by_type):
#     if sesh["type"] == "recurring":
#         print(f"Jac usually sees {sesh["name"]} on {sesh["day"]}s from {sesh["start"]} to {sesh["end"]}")
#     elif sesh["type"] == "one-time":
#         print(f"On {sesh["day"]}, {sesh["date"]} Jac will meet with {sesh["name"]} from {sesh["start"]} to {sesh["end"]}")
#     else:
#         print(f"{sesh["name"]}'s usual meeting on {sesh["day"]}, {sesh["date"]} has been canceled.")

from datetime import *

print(datetime.now().month)