import requests 
questions = requests.get("https://opentdb.com/api.php?amount=15&category=18&type=boolean")
questions.raise_for_status()
data = questions.json()["results"]
question_data = data