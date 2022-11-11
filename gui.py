import tkinter.font as tkFont
from tkinter import *
from gui_functions import Gui_Functions

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.title("Countdown Timer by Ankith")

        self.my_font = tkFont.Font(family="Fira Code", size=40)
        self.my_small_font = tkFont.Font(family="Fira Code", size=10)
        self.my_medium_font = tkFont.Font(family="Fira Code", size=12)

        self.myLabel = Label(self.root, font=self.my_font, text=f"00:00:00", fg="grey")
        self.myLabel.grid(row=0, column=0, columnspan=3)

        self.hours_label = Label(self.root, font=self.my_small_font, width=12, text="Hours:")
        self.hours_label.grid(row=1, column=0)

        self.hours_entry = Entry(self.root, width=16, borderwidth=2)
        self.hours_entry.grid(row=1, column=1, sticky="W")
        self.hours_entry.insert(0, "00")

        self.minutes_label = Label(self.root, font=self.my_small_font, width=12, text="Minutes:")
        self.minutes_label.grid(row=2, column=0)
        self.minutes_entry = Entry(self.root, width=16, borderwidth=2)
        self.minutes_entry.grid(row=2, column=1, sticky="W")
        self.minutes_entry.insert(0, "10")

        self.seconds_label = Label(self.root, font=self.my_small_font, width=12, text="Seconds:")
        self.seconds_label.grid(row=3, column=0)
        self.seconds_entry = Entry(self.root, width=16, borderwidth=2)
        self.seconds_entry.grid(row=3, column=1, sticky="W")
        self.seconds_entry.insert(0, "00")

        self.start_button = Button(self.root, font=tkFont.Font(family="Fira Code", size=10), text="Start!", width=20, fg="green" , command=lambda: Gui_Functions.startcountdown(self))
        self.start_button.grid(row=4, column=0, columnspan=3)
        self.reset_button = Button(self.root, font=tkFont.Font(family="Fira Code", size=10), text="Reset", width=20, fg="orange", command=lambda: Gui_Functions.restart(self))
        self.reset_button.grid(row=5, column=0,  columnspan=3)

        self.percent_label = Label(self.root, font=self.my_medium_font, text="")
        self.percent_label.grid(row=1, column=2)
        self.clear_all_button = Button(self.root, font=tkFont.Font(family="Fira Code", size=8), command=lambda: Gui_Functions.clear_all(self), text="Clear All")
        self.clear_all_button.grid(row=2, column=2)
        self.mode_change_button = Button(self.root, font=tkFont.Font(family="Fira Code", size=8), text="Dark Mode", command=lambda: Gui_Functions.mode_change(self), pady=5)
        self.mode_change_button.grid(row=3, column=2)
        self.root.mainloop()