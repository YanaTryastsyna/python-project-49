import random

GAME_RULES = 'What is the result of the expression?'


def generate_round():
    number1 = random.randint(1, 100)  # NOSONAR
    number2 = random.randint(1, 100)  # NOSONAR

    operators = ['+', '-', '*'] 
    random_operator = random.choice(operators)  # NOSONAR

    question = f"{number1} {random_operator} {number2}"
    if random_operator == '+':
        answer = number1 + number2
    elif random_operator == '-':
        answer = number1 - number2
    else: 
        answer = number1 * number2

    return question, str(answer)