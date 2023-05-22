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
            values=("P@ssw0rd!91", "gboquwbg48670OUHhughu#gq#", "M4tt30#Re1ter", "Matteo")
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
            
class QuestionSmartPerson(Question): 
    def __init__(self, master):
        super().__init__(master, "Are you smart?")

        self.add(ctk.CTkLabel(self, text="Rate yourself on a scale 1 to 10!"))
        self.add(ctk.CTkSlider(self,from_=0,to=10,command=self.slider_change,number_of_steps=10))


    def slider_change(self,value): 
        self.elements[0].configure(text=str(int(value)))
