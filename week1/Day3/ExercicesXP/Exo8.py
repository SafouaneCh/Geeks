
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


# 1. Ask questions and check answers
def ask_questions():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for item in data:
        answer = input(item["question"] + " ")
        
        if answer.strip().lower() == item["answer"].lower():
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect!")
            incorrect_answers += 1

            wrong_answers.append({
                "question": item["question"],
                "your_answer": answer,
                "correct_answer": item["answer"]
            })

    return correct_answers, incorrect_answers, wrong_answers


# 2 and 3. Display results and wrong answers
def show_results(correct, incorrect, wrong_answers):
    print("\n--- Quiz Results ---")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

    if incorrect > 0:
        print("\nHere are the questions you answered incorrectly:")

        for item in wrong_answers:
            print(f"\nQuestion: {item['question']}")
            print(f"Your answer: {item['your_answer']}")
            print(f"Correct answer: {item['correct_answer']}")

    if incorrect == 0:
        print("\nExcellent! You got every answer right!")
    elif incorrect <= 3:
        print("\nGood effort! Keep learning about Star Wars.")
    else:
        print("\nYou had more than 3 wrong answers.")


# Run the quiz and offer a replay
def main():
    while True:
        correct, incorrect, wrong_answers = ask_questions()
        show_results(correct, incorrect, wrong_answers)

        if incorrect > 3:
            play_again = input("\nWould you like to play again? (yes/no): ")

            if play_again.strip().lower() in ["yes", "y"]:
                print("\nLet's play again!\n")
            else:
                print("Thanks for playing!")
                break
        else:
            print("Thanks for playing!")
            break


main()