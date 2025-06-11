import random

GAME_RULES = 'What number is missing in the progression?'


def generate_round():

    start = random.randint(1, 100)  # NOSONAR
    step = random.randint(1, 10)  # NOSONAR
    length = random.randint(5, 15)  # NOSONAR

    progression = [start + step * i for i in range(length)]

    hidden_index = random.randint(0, length - 1)  # NOSONAR
    answer = progression[hidden_index]
    progression[hidden_index] = ".."

    question = ' '.join([str(item) for item in progression])
    return question, str(answer)





