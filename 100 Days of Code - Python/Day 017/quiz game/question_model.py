class Question:
    def __init__(self, text = "", answer = ""):
        self.text = text
        self.answer = answer


    def set_text(self, new_text):
        self.text = new_text
        

    def get_text(self):
        return self.text


    def set_answer(self, new_answer):
        self.answer = new_answer


    def get_answer(self):
        return self.answer