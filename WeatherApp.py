from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Current Weather Observation")
#root.iconbitmap()
root.geometry("600x100")

def zipLookUp():
    #zip.get()
    #zipLabel = Label(root, text=zip.get())
    #zipLabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() +"&distance=5&API_KEY=BDBCD984-C253-4F15-A8A8-AC9F75020C36")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = str(api[0]['AQI'])
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0c0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background = weather_color)

        myLabel = Label(root, text= city + " Air Quality " + quality + " " + category, font = ("Helvetica",20), background=weather_color)
        myLabel.grid(row=1,column=0,columnspan=2)

    except Exception as e:
        api = "Error..."


zip = Entry(root)
zip.grid(row=0, column=0,stick=W+E+N+S) 

zipButton = Button(root, text="Look Up Zip Code", command = zipLookUp)
zipButton.grid(row=0, column=1, stick=W+E+N+S)

root.mainloop()
