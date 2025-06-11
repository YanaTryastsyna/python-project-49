import random

GAME_RULES = 'What is the result of the expression?'


def generate_round():
    # Cryptographic security is not required here
    number1 = random.randint(1, 100) # nosec B311
    number2 = random.randint(1, 100) # nosec B311

    operators = ['+', '-', '*'] 
    random_operator = random.choice(operators) # nosec B311

    question = f"{number1} {random_operator} {number2}"
    if random_operator == '+':
        answer = number1 + number2
    elif random_operator == '-':
        answer = number1 - number2
    else: 
        answer = number1 * number2

    return question, str(answer)