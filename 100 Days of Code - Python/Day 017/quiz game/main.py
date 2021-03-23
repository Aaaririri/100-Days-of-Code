"""
Starting code from:
https://replit.com/@appbrewery/quiz-game-start
"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
q = question_data
for dicts in q:
    question_bank.append(Question(dicts["text"], dicts["answer"]))
    
q_brain = QuizBrain(question_bank)
q_brain.start()



