"""
ELEKTRON © 2023
Written by melektron
www.elektron.work
22.05.23, 11:23


"""


from ._question import Question
import random as r
import tkinter as tk
import customtkinter as ctk

class QuestionMark(Question):
    def __init__(self, master):
        super().__init__(master, "What is your FSST Mark?")

        mark_value = tk.IntVar()
        mark_value.set(5)
        create_random_mark = lambda: mark_value.set(r.randint(1, 5))
        self.add(ctk.CTkRadioButton(self, variable=mark_value, text=1, value=1, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=mark_value, text=2, value=2, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=mark_value, text=3, value=3, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=mark_value, text=4, value=4, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=mark_value, text=5, value=5, command=create_random_mark))


class Questionasdf(Question):
    def __init__(self, master):
        super().__init__(master, "What is your FSST Mark?")

        mark_value = tk.IntVar()
        mark_value.set(5)
        create_random_mark = lambda: mark_value.set(r.randint(1, 5))
        self.add(ctk.CTkRadioButton(self, variable=mark_value, text=1, value=1, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=mark_value, text=2, value=2, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=mark_value, text=3, value=3, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=mark_value, text=4, value=4, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=mark_value, text=5, value=5, command=create_random_mark))