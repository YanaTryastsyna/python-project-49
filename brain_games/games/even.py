import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    number = random.randint(1, 100)
    answer = "yes" if number % 2 == 0 else "no"
    question = str(number)
    return question, answer