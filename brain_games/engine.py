from brain_games.cli import welcome_user


def engine_games(game_rules, generate_round): 
    name = welcome_user()
    print(game_rules)

    correct_answers_needed = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_needed:
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer != str(correct_answer):
            print(
        f"'{user_answer}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'"
    )
            print(f"Let's try again, {name}!")
            return
    
        print("Correct!")
        correct_answers_count += 1
    
    print(f"Congratulations, {name}!")
