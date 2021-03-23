class QuizBrain:
    def __init__(self, question_list = []):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return current_question


    def start(self):
        is_true = True
        while is_true:
            question = self.next_question()
            print(f"Q.{self.question_number}: {question.get_text()} (True/False): ")
            player_answer  = input().title()
            if question.get_answer() == player_answer:
                print("Right answer")
                self.score += 1
                print(f"Your current score is: {self.score}")
            else:
                print(f"Wrong answer the right answer was {question.get_answer()}")
                print(f"Your final score is: {self.score}")
                is_true = False
            if self.question_number == len(self.question_list):
                print("You completed the chalenge!!!")
                print(f"Your final score is: {self.score}")
                is_true = False
    