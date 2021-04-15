class Question:

    def __init__(self, **kwargs):
        self.difficulty = kwargs.get('q_difficulty','None')
        self.text = kwargs.get('q_text','Not Found')
        self.answer =kwargs.get('q_answer','Not Found')
