import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain 
        
        self.window = tk.Tk()
        self.window.title("ComputerQuizz")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        
        self.score_label = tk.Label( text = "score: 0", fg = "white", bg = THEME_COLOR, font = ("Ariel", 12, "italic"))
        self.score_label.grid(row = 0, column = 1)
        
        self.canvas = tk.Canvas(width = 300, height = 250, bg = "white")
        self.question_text = self.canvas.create_text(150, 125,width = 280, text = "Question", fill = THEME_COLOR, font = ("Ariel", 20, "italic"))
        self.canvas.grid(row = 1, column = 0, columnspan = 2)
        
        self.get_next_question() 
        
        
        ti = tk.PhotoImage(file = "Day 034/quizz/images/true.png")
        fi = tk.PhotoImage(file = "Day 034/quizz/images/false.png")
        self.true_button = tk.Button(image = ti, highlightthickness = 0, bg = THEME_COLOR, command = self.true_check)
        self.true_button.grid(row = 2, column = 1)
        self.false_button = tk.Button(image = fi, highlightthickness = 0, bg = THEME_COLOR, command = self.false_check)
        self.false_button.grid(row = 2, column = 0)
        
    
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()    
            self.canvas.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas.itemconfig(self.question_text,text = "End of The Game")
            
    def set_score(self):
        score_text = self.quiz.get_score()
        self.score_label.config(text = f"Score{score_text}")
        
    def true_check(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)
        self.set_score()
            
    def false_check(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)
        self.set_score() 
    
            
