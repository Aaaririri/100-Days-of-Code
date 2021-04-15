from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Interface
from html import unescape

question_bank = []
for question in question_data:

    question_difficulty = question["difficulty"]
    question_text = unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(q_text = question_text, q_answer = question_answer, q_difficulty = question_difficulty)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
interface = Interface(quiz)

