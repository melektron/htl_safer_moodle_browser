#! .venv/bin/python

import classes.ui.questions as q
from classes.ui import AppWindow

main_window: AppWindow = None

def main():
    global main_window
    main_window = AppWindow()
    main_window.set_questions(
        q.QuestionMark(main_window),
        q.QuestionMark(main_window),
        q.QuestionStrongPassword(main_window),
        q.QuestionMark(main_window)
    )
    main_window.mainloop()

if __name__ == "__main__":
    main()