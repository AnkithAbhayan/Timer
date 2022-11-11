from tkinter import *
import threading
import tkinter.font as tkFont
import core
import pathlib
import os
from time import sleep

class Gui_Functions:
    def clear_all(Window):
        Window.hours_entry.delete(0, END)
        Window.minutes_entry.delete(0, END)
        Window.seconds_entry.delete(0, END)

    def restart(Window):
        fullpath = str(pathlib.Path(__file__).parent.absolute()) + "/main.py"
        Window.root.destroy()
        os.system(f"start pythonw {fullpath}")
        sys.exit()

    def countdown(timestamp, Window):
        Window.myLabel["font"] = tkFont.Font(family="Fira Code", size=27)
        for i in [3,2,1]:
            Window.myLabel["text"] = f"starting in {i}.."
            sleep(1)
        Window.myLabel["font"] = Window.my_font
        Window.myLabel["text"] = timestamp
        Window.myLabel["fg"] = "green"
        MyClient = core.Time(timestamp)
        MyClient.SetCheckpoint()
        while not MyClient.CountdownOver():
            if change_value:=MyClient.CheckpointChanged():
                MyClient.Check()
                MyClient.seconds -= change_value
                MyClient.SetCheckpoint()
                MyClient.ShowTime(Window)

    def startcountdown(Window):
        hours = Window.hours_entry.get()
        minutes = Window.minutes_entry.get()
        seconds = Window.seconds_entry.get()
        if not hours:
            hours = 0
        if not minutes:
            minutes = 0
        if not seconds:
            seconds = 0 
        
        if int(minutes) > 60:
            minutes = 60
        if int(seconds) > 60:
            seconds = 60
        countdown_func = threading.Thread(target=lambda: Gui_Functions.countdown(f"{hours}:{minutes}:{seconds}", Window), daemon=True)
        countdown_func.start()

    def mode_change(Window):
        get_colour = {
            "Dark Mode": {
                "fg": "white",
                "bg": "black",
                "mode_title": "Light Mode"
            },
            "Light Mode": {
                "fg": "black",
                "bg": "white",
                "mode_title": "Dark Mode"
            }
        }

        current_mode = get_colour[Window.mode_change_button["text"]]

        Window.mode_change_button["text"] = current_mode["mode_title"]


        Window.root["bg"] = current_mode["bg"]
        Window.myLabel["bg"] = current_mode["bg"]

        Window.hours_label["fg"] = current_mode["fg"]
        Window.hours_label["bg"] = current_mode["bg"]

        Window.hours_entry["fg"] = current_mode["fg"]
        Window.hours_entry["bg"] = current_mode["bg"]

        Window.minutes_label["fg"] = current_mode["fg"]
        Window.minutes_label["bg"] = current_mode["bg"]

        Window.minutes_entry["fg"] = current_mode["fg"]
        Window.minutes_entry["bg"] = current_mode["bg"]


        Window.seconds_label["fg"] = current_mode["fg"]
        Window.seconds_label["bg"] = current_mode["bg"]

        Window.seconds_entry["fg"] = current_mode["fg"]
        Window.seconds_entry["bg"] = current_mode["bg"]

        Window.start_button["bg"] = current_mode["bg"]
        Window.reset_button["bg"] = current_mode["bg"]

        Window.clear_all_button["bg"] = current_mode["bg"]
        Window.clear_all_button["fg"] = current_mode["fg"]

        Window.mode_change_button["fg"] = current_mode["fg"]
        Window.mode_change_button["bg"] = current_mode["bg"]

        Window.percent_label["fg"] = current_mode["fg"]
        Window.percent_label["bg"] = current_mode["bg"]
