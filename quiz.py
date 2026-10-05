questions = ("Whats your name? ", "Whats your age? ", "Whats your class? ")
correct_answers = ("Huzaifa", "20", "BSCS")
score = 0

for question, answer in zip(questions, correct_answers):
    guess = input(question + "(q to quit) ").strip().lower()

    if guess == "q":
        break

    if guess == answer.lower():
        score += 1

print(f"Your score is: {score}/{len(questions)}")