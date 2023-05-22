"""
ELEKTRON © 2023
Written by melektron
www.elektron.work
22.05.23, 11:23


"""


from ._question import Question
import random as r
import time as t
import tkinter as tk
import typing
from tkinter import messagebox
import customtkinter as ctk


class QuestionLoading(Question):
    """
    A special question that displays a progress bar for calculating results
    """
    def __init__(self, master):
        super().__init__(master, "Calculating results...")

        self._pb_progress = ctk.CTkProgressBar(self, orientation="horizontal", determinate_speed=0.5)
        self._pb_progress.grid(row=self.row_id, column=0, padx=10, sticky="we")
        self.row_id += 1
    
    def run_progress(self, then: typing.Callable):
        self._pb_progress.set(0)

        def stopfn():
            self._pb_progress.stop()
            then()
        
        self._pb_progress.start()
        self.after(2200, stopfn)


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
    
    def show_correct(self) -> bool:
        super().show_correct()
        correct = r.randint(0, 4)
        for element in self.elements:
            if str(element.cget("text")) == str(correct):
                element.configure(text_color="green")
            else:
                element.configure(text_color="red")


class QuestionStrongPassword(Question):
    def __init__(self, master):
        super().__init__(master, "Which password is strong?")

        self.add(ctk.CTkComboBox(
            self,
            values=("", "123456789", "gboquwbg48670OUHhughu#gq#", "abcdef", "Matteo")
        ))
    
    def show_correct(self) -> bool:
        super().show_correct()
        if self.elements[0].get() == "Matteo":
            self.elements[0].configure(border_color="green")    
            messagebox.showinfo(self.question_text, "You are correct!")
            return True
        else:
            self.elements[0].configure(border_color="red")
            messagebox.showinfo(self.question_text, "You are wrong, you WEAK person")
            return False
