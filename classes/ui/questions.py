"""
ELEKTRON © 2023
Written by melektron
www.elektron.work
22.05.23, 11:23


"""


from ._question import Question
import random as r
import tkinter as tk
from tkinter import messagebox
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


class QuestionStrongPassword(Question):
    def __init__(self, master):
        super().__init__(master, "Which password is strong?")

        self.add(ctk.CTkComboBox(
            self,
            values=("", "123456789", "gboquwbg48670OUHhughu#gq#", "abcdef", "Matteo")
        ))
        self.add(ctk.CTkButton(self, text="test check", command=self.show_correct))
    
    def show_correct(self) -> bool:
        if self.elements[0].get() == "Matteo":
            self.elements[0].configure(border_color="green")    
            messagebox.showinfo(self.question_text, "You are correct!")
            return True
        else:
            self.elements[0].configure(border_color="red")
            messagebox.showinfo(self.question_text, "You are wrong, you WEAK person")
            return False
            
class QuestionLoading(Question):
    """
    A special question that displays a progress bar for calculating results
    """
    def __init__(self, master):
        super().__init__(master, "Calculating results...")

        self._pb_progress = ctk.CTkProgressBar(self, orientation="horizontal")
        self._pb_progress.grid(row=self.row_id, column=0, padx=10, sticky="we")
        self.row_id += 1
    
    def run_progress(self):
        self._pb_progress.start()