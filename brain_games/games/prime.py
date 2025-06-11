import random

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return "no"
        
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_round():
    # Cryptographic security is not required here
    question = random.randint(1, 100) # nosec B311
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer


