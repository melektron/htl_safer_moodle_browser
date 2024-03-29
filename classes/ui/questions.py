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
        self._pb_progress.grid(row=self._row_id, column=0, padx=10, sticky="we")
        self._row_id += 1
    
    def _run_progress(self, then: typing.Callable):
        self._pb_progress.set(0)

        def stopfn():
            self._pb_progress.stop()
            then()
        
        self._pb_progress.start()
        self.after(2200, stopfn)


class QuestionMark(Question):
    def __init__(self, master):
        super().__init__(master, "What is your FSST Mark?")

        self.mark_value = tk.IntVar()
        self.mark_value.set(5)
        create_random_mark = lambda: self.mark_value.set(r.randint(1, 5))
        self.add(ctk.CTkRadioButton(self, variable=self.mark_value, text=1, value=1, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=self.mark_value, text=2, value=2, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=self.mark_value, text=3, value=3, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=self.mark_value, text=4, value=4, command=create_random_mark))
        self.add(ctk.CTkRadioButton(self, variable=self.mark_value, text=5, value=5, command=create_random_mark))
    
    def show_correct(self) -> bool:
        super().show_correct()
        correct = r.randint(0, 4)
        for element in self._elements:
            if str(element.cget("text")) == str(correct):
                element.configure(text_color="green")
            else:
                element.configure(text_color="red")


class QuestionStrongPassword(Question):
    def __init__(self, master):
        super().__init__(master, "Which password is strong?")

        self.add(ctk.CTkComboBox(
            self,
            values=("P@ssw0rd!91", "gboquwbg48670OUHhughu#gq#", "M4tt30#Re1ter", "Matteo")
        ))
    
    def show_correct(self) -> bool:
        super().show_correct()
        if self._elements[0].get() == "Matteo":
            self._elements[0].configure(border_color="green")    
            return True
        else:
            self._elements[0].configure(border_color="red")
            return False


class QuestionSmartPerson(Question): 
    def __init__(self, master):
        super().__init__(master, "Are you smart?")

        self.add(ctk.CTkLabel(self, text="Rate yourself on a scale 1 to 10!"))
        self.add(ctk.CTkSlider(self,from_=0,to=10,command=self._slider_change,number_of_steps=10))


    def _slider_change(self,value): 
        self._elements[0].configure(text=str(int(value)))

    def show_correct(self):
        super().show_correct()
        correct=r.randint(0,10)

        if correct==self._elements[1].get():     
            self._elements[0].configure(text_color="green")
        else: 
            self._elements[0].configure(text_color="red")
        
        self.add(ctk.CTkLabel(self, text="Correct Answer: "+str(correct),text_color="green"))
        


class QuestionGoingToSchool(Question): 
    def __init__(self, master):
        super().__init__(master, "When do you like going to school?")

        self.add(ctk.CTkCheckBox(self, text="Monday", command=self._liked_weekdays))
        self.add(ctk.CTkCheckBox(self, text="Tuesday", command=self._liked_weekdays))
        self.add(ctk.CTkCheckBox(self, text="Wednesday", command=self._liked_weekdays))
        self.add(ctk.CTkCheckBox(self, text="Thursday", command=self._liked_weekdays))
        self.add(ctk.CTkCheckBox(self, text="Friday", command=self._liked_weekdays))
        self.add(ctk.CTkCheckBox(self, text="Saturday", command=self._liked_weekdays))
        self.add(ctk.CTkCheckBox(self, text="Sunday", command=self._liked_weekdays))

    def _liked_weekdays(self): 
        for checkbox in self._elements:
            checkbox.deselect()
        messagebox.showinfo("Liar", "Stop lying!!! \nWe all know, that that's not true")

    def show_correct(self):
        super().show_correct()
        for i in range(5):
            self._elements[i].configure(border_color="red")    
            
        self._elements[5].configure(border_color="green")
        self._elements[6].configure(border_color="green")
        
        

class QuestionButtonJump(Question): 
    def __init__(self, master):
        super().__init__(master, "Press the button!!!")
        self.grid_rowconfigure(self._row_id, weight=1)
        self._counter = 0

        self._jumping_button_frame=ctk.CTkFrame(self)
        self._jumping_button_frame.grid(sticky="NESW", row=self._row_id, column=0)
        self._row_id += 1
        self._jumping_button_frame.grid_columnconfigure((0, 1, 2, 3), weight=1, minsize=150)
        self._jumping_button_frame.grid_rowconfigure((0, 1, 2, 3), weight=1, minsize=40)
        self._jumping_button=ctk.CTkButton(self._jumping_button_frame, text="Click ME", command=self._jump)
        self._jumping_button.grid()
        self._jumping_button.bind("<Enter>",command=self._maybe_jump)


    def _jump(self): 
        row_config = r.randint(0,3)
        column_config = r.randint(0,3)
        self._jumping_button.grid_configure(row=row_config,column=column_config)
        self._counter += 1

    def _maybe_jump(self, e): 
        chance = r.randint(0, 1)
        if chance == 1: 
            self._jump() 

    def show_correct(self):
        super().show_correct()
        
        self.add(ctk.CTkLabel(self, text="Hit counter: "+str(self._counter)))

        if self._counter >= 10: 
            self._elements[0].configure(text_color="green")
        else: 
            self._elements[0].configure(text_color="red")