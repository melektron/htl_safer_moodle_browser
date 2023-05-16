import tkinter as tk


class Question(tk.Frame):
    def __init__(self, master, text="??"):
        self.question_text = text
        self.elements = []

        super().__init__(master)

        lb_question = tk.Label(self, text=self.question_text, anchor="w")
        lb_question.pack()

    def add(self, element: tk.Widget):
        self.elements.append(element)
        element.pack()

