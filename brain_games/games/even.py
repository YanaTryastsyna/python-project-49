import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
     # Cryptographic security is not required here
    number = random.randint(1, 100)# nosec B311
    answer = "yes" if number % 2 == 0 else "no"
    question = str(number)
    return question, answer