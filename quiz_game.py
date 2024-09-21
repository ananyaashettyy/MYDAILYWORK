import random

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "correct": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "correct": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "choices": ["A) Charles Dickens", "B) William Shakespeare", "C) J.K. Rowling", "D) Leo Tolstoy"],
        "correct": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"],
        "correct": "C"
    },
    {
        "question": "What is the square root of 64?",
        "choices": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "correct": "C"
    }
]

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions.")
    print("Choose the correct answer by typing A, B, C, or D.")
    print("Let's begin!\n")

def present_questions(questions):
    score = 0
    random.shuffle(questions)  

    for idx, q in enumerate(questions):
        print(f"Question {idx + 1}: {q['question']}")
        for choice in q["choices"]:
            print(choice)

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q["correct"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q['correct']}.\n")

    return score

def display_final_score(score, total_questions):
    print(f"Your final score is: {score}/{total_questions}")
    if score == total_questions:
        print("Excellent! You got all the answers correct.")
    elif score >= total_questions // 2:
        print("Good job! You did well.")
    else:
        print("Better luck next time! Keep practicing.\n")


def play_quiz_game():
    display_welcome_message()
    play_again = True

    while play_again:
        score = present_questions(quiz_questions)
        display_final_score(score, len(quiz_questions))

        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            play_again = False
            print("Thank you for playing! Goodbye.")

if __name__ == "__main__":
    play_quiz_game()
