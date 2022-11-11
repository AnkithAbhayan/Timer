from tkinter import *
from datetime import datetime
from gui import Gui

class Time:
    def __init__(self, date_string):
        array = date_string.split(":")

        for i in range(3-len(array)):
            array.insert(0, 00)

        self.hours, self.minutes, self.seconds = int(array[0]), int(array[1]), int(array[2])
        self.total = [self.hours, self.minutes, self.seconds]


    def CountdownOver(self):
        if self.hours + self.minutes + self.seconds <= 0:
            return True
        return False

    def SetCheckpoint(self):
        self.checkpoint = datetime.now().strftime("%S")

    def CheckpointChanged(self):
        if (datetime.now().strftime("%S")) != self.checkpoint:
            return 1
        return False

    def Check(self):
        if self.seconds <= 0:
            if self.minutes != 0:
                self.minutes -= 1
                self.seconds = 60
            
        if self.minutes <= 0 and self.seconds <= 0:
            if self.hours != 0:
                self.hours -= 1
                self.minutes = 59
                self.seconds = 60        

    def ShowTime(self, Window):
        temp_hours, temp_minutes, temp_seconds = self.hours, self.minutes, self.seconds
        if self.hours < 10:
            temp_hours = f"0{self.hours}"
        if self.minutes < 10:
            temp_minutes = f"0{self.minutes}"
        if self.seconds < 10:
            temp_seconds = f"0{self.seconds}"
        Window.myLabel["text"] = f"{temp_hours}:{temp_minutes}:{temp_seconds}"
        seconds_left = self.seconds + (self.minutes*60) + (self.hours*60*60)
        seconds_total = self.total[2] + (self.total[1]*60) + (self.total[0]*60*60)
        percent_done = str(((seconds_total-seconds_left)/seconds_total)*100)[0:4]
        if percent_done[-1] == ".":
            percent_done = percent_done[0:-1]
        if percent_done == "100":
            Window.percent_label["fg"] = "green"
        else:
            percent_done += "0"*(4-len(percent_done))
        Window.percent_label["text"] = f"{percent_done}% Done"