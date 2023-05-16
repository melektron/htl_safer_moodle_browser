import tkinter as tk
import tkinter.messagebox as msg
import random as r
from question import Question

main_window: tk.Tk
real_close_flag = False

def real_close(e=None):
    main_window.destroy()
    print("closed")

def normal_close():
    msg.showinfo("!!!!", "fu, you won't get rid of me")







def main():
    global main_window

    main_window = tk.Tk()
    main_window.title(".")
    main_window.grid_columnconfigure(0, weight=1)

    # pressing o will actually close the window
    main_window.bind("o", real_close)

    # closing the window the normal way will do wired stuff
    main_window.protocol("WM_DELETE_WINDOW", normal_close)


    # Title
    lb_exam_title = tk.Label(main_window, text="Solve this simple exam")
    lb_exam_title.grid(row=0, column=0)


    # first question
    question = Question(main_window, "What is our FSST mark?")
    question.grid(row=1, column=0)
    mark_value = tk.IntVar()
    mark_value.set(5)
    create_random_mark = lambda: mark_value.set(r.randint(1, 5))
    question.add(tk.Radiobutton(question, variable=mark_value, text=1, value=1, command=create_random_mark))
    question.add(tk.Radiobutton(question, variable=mark_value, text=2, value=2, command=create_random_mark))
    question.add(tk.Radiobutton(question, variable=mark_value, text=3, value=3, command=create_random_mark))
    question.add(tk.Radiobutton(question, variable=mark_value, text=4, value=4, command=create_random_mark))
    question.add(tk.Radiobutton(question, variable=mark_value, text=5, value=5, command=create_random_mark))



    # cursed radio buttons
    lb_exam_title = tk.Label(main_window, text="Solve this simple exam")
    lb_exam_title.grid(row=0, column=0, columnspan=3)





    






    main_window.mainloop()







if __name__ == "__main__":
    main()