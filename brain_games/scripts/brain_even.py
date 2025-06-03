import random

def is_even(number):
    return number % 2 == 0

def generate_round():
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if is_even(number) else 'no'
    return question, answer

def play_even_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_needed = 3  
    correct_answers_count = 0
    
    while correct_answers_count < correct_answers_needed:
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").lower()

        if user_answer not in ('yes', 'no'):
            print('answer can only "yes" or "no"')
            continue

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")
        correct_answers_count += 1
    print(f"Congratulations, {name}!")

if __name__ == '__main__':
    play_even_game()



 
   

  