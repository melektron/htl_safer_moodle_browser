#! .venv/bin/python

import tkinter as tk
import tkinter.messagebox as msg
import customtkinter as ctk
import random as r
import classes.ui.questions as q
from classes.ui import Question, FONT_HEADER

main_window: ctk.CTk
real_close_flag = False

questions: list[Question] = None
current_question: Question = None
question_index: int = 0



def real_close(e=None):
    main_window.destroy()
    print("closed")

def normal_close():
    msg.showinfo("!!!!", "fu, you won't get rid of me")


def show_question(new_question: Question):
    global current_question
    if current_question is new_question:
        return
    if current_question is not None:
        current_question.grid_forget()
    current_question = new_question
    current_question.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10)

def next_button_cb(bback: ctk.CTkButton, bnext: ctk.CTkButton):
    global question_index
    old_index = question_index
    if question_index >= len(questions) - 1:
        print("check")
    else:
        question_index += 1
        show_question(questions[question_index])
        # if we have reached the end, change the button to "Submit"
        if question_index == len(questions) - 1:
            bnext.configure(text="Submit", fg_color="green", hover_color="dark green")
        if old_index == 0:
            bback.configure(state="normal")


def back_button_cb(bback: ctk.CTkButton, bnext: ctk.CTkButton):
    global question_index
    old_index = question_index
    if question_index > 0:
        question_index -= 1
        show_question(questions[question_index])
        # if we have reached the first question, disable the back button
        if question_index == 0:
            bback.configure(state="disabled")
        # if we were at the last question before, set the button back to the default state
        if old_index == len(questions) - 1:
            bnext.configure(text="Next", fg_color="blue", hover_color="dark blue")


def main():
    global main_window, questions

    main_window = ctk.CTk()
    main_window.geometry("600x250")
    main_window.title(".")
    main_window.grid_columnconfigure(0, weight=1)
    main_window.grid_columnconfigure(1, weight=1)
    main_window.grid_rowconfigure(2, weight=1)

    # pressing o will actually close the window
    main_window.bind("o", real_close)

    # closing the window the normal way will do wired stuff
    main_window.protocol("WM_DELETE_WINDOW", normal_close)

    # Title
    lb_exam_title = ctk.CTkLabel(main_window, text="Solve this simple exam", font=FONT_HEADER)
    lb_exam_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Question area
    questions = [
        q.QuestionMark(main_window),
        q.QuestionMark(main_window),
        q.QuestionStrongPassword(main_window),
        q.QuestionMark(main_window),
    ]

    show_question(questions[question_index])

    # back button
    bt_back = ctk.CTkButton(main_window, text="Back", state="disabled", command=lambda: back_button_cb(bt_back, bt_next))
    bt_back.grid(row=2, column=0, pady=10, sticky="s")

    # next button
    bt_next = ctk.CTkButton(main_window, text="Next", command=lambda: next_button_cb(bt_back, bt_next))
    bt_next.grid(row=2, column=1, pady=10, sticky="s")



    main_window.mainloop()







if __name__ == "__main__":
    main()