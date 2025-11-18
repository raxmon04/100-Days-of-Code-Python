from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.timer_label = Label(text="Time: 10", bg=THEME_COLOR, fg="white")
        self.timer_label.grid(row=0, column=0)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #Buttons
        true_image = PhotoImage(file="/mnt/d/Git/python/034_GUIQuizApp/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="/mnt/d/Git/python/034_GUIQuizApp/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.time_left = 10
            self.countdown()
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        try:
            self.window.after_cancel(self.timer)
        except AttributeError:
            pass
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        try:
            self.window.after_cancel(self.timer)
        except AttributeError:
            pass
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def countdown(self):
        if self.time_left <= 3:
            self.timer_label.config(fg="red")
        else:
            self.timer_label.config(fg="white")
        if self.time_left > 0:
            self.timer_label.config(text=f"Time: {self.time_left}s")
            self.time_left -= 1
            self.timer = self.window.after(1000, self.countdown)
        else:
            self.give_feedback(False)
