import tkinter as tk
import customtkinter as ctk


class Question(ctk.CTkFrame):
    def __init__(self, master, text="??"):
        self.question_text = text
        self.elements: list[tk.Widget] = []
        self.row_id = 1  # starting at row 1

        super().__init__(master)

        lb_question = ctk.CTkLabel(self, text=self.question_text, anchor="w")
        lb_question.grid(row=0, column=0, sticky="w")



    def add(self, element: tk.Widget):
        """
        Adds a new subelement to the question like a radio button or an entry
        """
        self.elements.append(element)
        element.grid(row=self.row_id, column=0)
        self.row_id += 1


    def show_correct(self) -> bool:
        ...

