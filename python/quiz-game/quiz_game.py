score = 0


def ask_question(question, choices, correct_answer, correct_message, score):
    print(question)
    print(choices)

    answer = input("Your answer: ")

    if answer.strip().lower() == correct_answer.lower():
        score += 1
        print("Correct!")
    else:
        print(correct_message)

    print("Score:", score, "/ 5")
    print()

    return score


print("Welcome to the Quiz Game!\n")

score = ask_question(
    "Which planet is known as the Red Planet?",
    """A) Venus
B) Mars
C) Jupiter
D) Saturn""",
    "b",
    "Incorrect. The correct answer is B) Mars.",
    score
)

score = ask_question(
    "What is the largest ocean on Earth?",
    """A) Atlantic Ocean
B) Indian Ocean
C) Arctic Ocean
D) Pacific Ocean""",
    "d",
    "Incorrect. The correct answer is D) Pacific Ocean.",
    score
)

score = ask_question(
    "Who wrote the play 'Romeo and Juliet'?",
    """A) William Shakespeare
B) Charles Dickens
C) Jane Austen
D) Mark Twain""",
    "a",
    "Incorrect. The correct answer is A) William Shakespeare.",
    score
)

score = ask_question(
    "What is the capital of France?",
    """A) London
B) Berlin
C) Rome
D) Paris""",
    "d",
    "Incorrect. The correct answer is D) Paris.",
    score
)

score = ask_question(
    "What is the chemical symbol for water?",
    """A) H2O
B) CO2
C) NaCl
D) O2""",
    "a",
    "Incorrect. The correct answer is A) H2O.",
    score
)

print("Quiz completed!")
print("Your final score is:", score, "/ 5")

if score == 5:
    print("Perfect score! 🎉")
elif score >= 4:
    print("Great job!")
elif score >= 3:
    print("Good work!")
else:
    print("Keep practicing!")
