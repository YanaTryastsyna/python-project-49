import random

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_round():
    
    number1 = random.randint(1, 100)  # NOSONAR
    number2 = random.randint(1, 100)  # NOSONAR
    question = f"{number1} {number2}"
    answer = str(gcd(number1, number2))
    return question, answer

    