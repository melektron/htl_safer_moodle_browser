import tkinter as tk
import customtkinter as ctk


class Question(ctk.CTkFrame):
    def __init__(self, master, text="??"):
        self._question_text: str = text
        self._elements: list[tk.Widget] = []
        self._row_id = 1  # starting at row 1

        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self._lb_question = ctk.CTkLabel(self, text=self._question_text, anchor="w")
        self._lb_question.grid(row=0, column=0, sticky="w", pady=10, padx=10)
        # spacer at the end
        self._lb_spacer = ctk.CTkLabel(self, text="")
        self._lb_spacer.grid(row=20, column=0) # large row number that is probably never needed


    def add(self, element: tk.Widget):
        """
        Adds a new subelement to the question like a radio button or an entry
        """
        self._elements.append(element)
        element.grid(row=self._row_id, column=0, pady=5, padx=5, sticky="w")
        self._row_id += 1


    def show_correct(self) -> bool:
        ...

