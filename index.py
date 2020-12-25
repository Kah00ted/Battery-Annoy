# Imports
import psutil
import sys
import time
import ctypes
import tkinter as tk

# function returning time in hh:mm:ss 
def convertTime(seconds): 
	minutes, seconds = divmod(seconds, 60) 
	hours, minutes = divmod(minutes, 60) 
	return "%d:%02d:%02d" % (hours, minutes, seconds) 

def doDaPop(message, fullScreen):
    window = tk.Tk()
    window.title('BATT WARN')
    if(fullScreen == True):
        window.attributes('-fullscreen', True)
    else:
        window.geometry(f'{window.winfo_screenwidth()}x40')
        window.attributes("-topmost", True)
    tk.Label(text=message, font=("Default", 30)).pack()
    tk.mainloop()
# Get batt details
battery = psutil.sensors_battery() 

if (battery == None): #If there isnt a batt detected
    print("Your PC doesn't have a battery installed")
    doDaPop("Your PC doesn't have a battery installed", False)
    sys.exit()

#def Mbox(title, text, style):
    #return ctypes.windll.user32.MessageBoxW(0, text, title, style)

asked = False
stage = 0

def checkBatt():

    global stage
    global asked

    #redefine batt var with current stats
    battery = psutil.sensors_battery()

    percent = int(battery.percent)

    print(percent)

    if(battery.power_plugged == True):
        print("plugged in")
        if(asked == True):
            print("Thank you. You had me worried there!")
            doDaPop("Thank you. You had me worried there!", False)
        asked = False
        stage = 0
    elif(percent <= 5):
        asked = True
        if (stage != 5):
            stage = 5
            print("HEY!!! IM DYING HERE!!")
            doDaPop("HEY!!! IM DYING HERE!!", True)
    elif (percent <= 10):
        asked = True
        if (stage != 10):
            stage = 10
            print("Plug in your damn computer!!")
            doDaPop("Plug in your damn computer!!", False)
    elif (percent <= 15):
        asked = True
        if (stage != 15):
            stage = 15
            print("Were at 15% please plug me in.")
            doDaPop("Were at 15% please plug me in.", False)
    elif (percent <= 20):
        asked = True
        if (stage != 20):
            stage = 20
            print("Hey You. Your running a little low on juice")
            doDaPop("Hey You. Your running a little low on juice", False)
        


        #print('Hey You. Your running a little low on juice')
    
    # Mbox('Hey You', 'Your running a little low on juice', 0)

def runLoop():
    while True:
        checkBatt()
        time.sleep(60*2)

runLoop()