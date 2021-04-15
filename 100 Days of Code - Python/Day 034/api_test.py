import requests 
questions = requests.get("https://opentdb.com/api.php?amount=1&category=18&type=boolean")
questions.raise_for_status()
text = questions.json()
text_category = text["results"][0]["category"]
text_difficulty = text["results"][0]["difficulty"]
text_question = text["results"][0]["question"]
text_answer = text["results"][0]["correct_answer"]

