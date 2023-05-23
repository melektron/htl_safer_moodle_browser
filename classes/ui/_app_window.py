
import tkinter.messagebox as msg
import customtkinter as ctk

from ._question import Question
from . import questions as q
from . import _styles as styles


class AppWindow(ctk.CTk):
    question_area: ctk.CTkScrollableFrame = None
    _questions: tuple[Question]
    _current_question: Question = None
    _current_question_index: int = 0


    def __init__(self):
        super().__init__()
        self.title("Safer Moodle Browser 2.0")

        # implement the annoying exit functionality
        # closing the window the normal way will do wired stuff
        self.protocol("WM_DELETE_WINDOW", self._close_window_hook)
        # pressing o will actually close the window
        self.bind("o", self._real_close_window)

        # configure the window layout
        # column 0 and 1 needed for bottom buttons
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # last row contains the buttons and they should always extend to the bottom
        self.grid_rowconfigure(2, weight=1)

        # == UI Elements
        # Title
        self._lb_exam_title = ctk.CTkLabel(self, text="Solve this simple exam", font=styles.FONT_HEADER)
        self._lb_exam_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Question area 
        self.question_area = ctk.CTkScrollableFrame(self, width=600, height=250)
        self.question_area.grid_columnconfigure(0, weight=1)
        self.question_area.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        
        # Back button
        self._bt_back = ctk.CTkButton(self, text="Back", state="disabled", command=self._back_button_cb)
        self._bt_back.grid(row=2, column=0, pady=10, sticky="s")

        # Next/Submit button
        self._bt_next = ctk.CTkButton(self, text="Next", command=self._next_button_cb)
        self._bt_next.grid(row=2, column=1, pady=10, sticky="s")

    
    def set_questions(self, *questions: Question):
        """
        Sets the list of questions to be asked
        """
        self._questions = questions
        self._show_question(self._questions[self._current_question_index]) # shows first question by default


    def _close_window_hook(self):
        """
        Method that does weird stuff when the user tries to close
        a window normally
        """
        msg.showinfo("Nonono", "Unfortunately, Safer Moodle Browser 2.0's extensive safety system has blocked the action you are trying to do.")


    def _real_close_window(self, e=None):
        """
        Method that actually closes the window
        """
        self.destroy()


    def _show_question(self, new_question: Question):
        """
        Shows a question in the question area, removing the one 
        previously there in case there was any
        """
        if self._current_question is new_question:
            return
        if self._current_question is not None:
            self._current_question.grid_forget()
        self._current_question = new_question
        self._current_question.grid(row=0, column=0, sticky="nsew", padx=10)


    def _show_question_answers(self):
        """
        Shows all questions and their answers
        """
        # hide the current question
        if self._current_question is not None:
            self._current_question.grid_forget()
        
        # instead add all the questions
        for row in range(len(self._questions)):
            self._questions[row].grid(row=row, column=0, sticky="nsew", padx=10)

        # make window larger
        self.question_area.configure(height=600)
        
        # show all the answers
        for question in self._questions:
            question.show_correct()
        

    def _next_button_cb(self):
        old_index = self._current_question_index
        # already at last question, check for correctness
        if self._current_question_index >= len(self._questions) - 1:
            self._submit()
        # go to next question
        else:
            self._current_question_index += 1
            self._show_question(self._questions[self._current_question_index])
            # if we have reached the end, change the next button to "Submit"
            if self._current_question_index == len(self._questions) - 1:
                self._bt_next.configure(text="Submit", fg_color="green", hover_color="dark green")
            # if we used to be at the initial index, turn on the back button
            if old_index == 0:
                self._bt_back.configure(state="normal")


    def _back_button_cb(self):
        old_index = self._current_question_index
        # if we aren't already on the first question
        if self._current_question_index > 0:
            self._current_question_index -= 1
            self._show_question(self._questions[self._current_question_index])
            # if we have reached the first question, disable the back button
            if self._current_question_index == 0:
                self._bt_back.configure(state="disabled")
            # if we were at the last question before, set the button back to the default state
            if old_index == len(self._questions) - 1:
                self._bt_next.configure(
                    text="Next", 
                    fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"], 
                    hover_color=ctk.ThemeManager.theme["CTkButton"]["hover_color"]
                )
    

    def _submit(self):
        """
        Processes the submit button. This shows all questions in a scrollable
        frame and displays their solutions using their show_correct() methods
        """
        # first remove the buttons
        self._bt_back.grid_forget()
        self._bt_next.grid_forget()
        # change the title
        self._lb_exam_title.configure(text="Exam results")
        # change space allocation
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(1, weight=1)
        
        # place the fake progress bar and start it
        progress_question = q.QuestionLoading(self.question_area)
        self._show_question(progress_question)
        progress_question._run_progress(then=self._show_question_answers)






