# python quiz game
questions = ("Which city is known as the 'Pink City' of India?: ",
             "What is the national animal of India?: ",
             "Who was the first Prime Minister of independent India?: ",
             "In which year did India gain independence from British rule?: ",
             "What is the name of the famous monument built by Shah Jahan in memory of his wife?: ")

options = (("A. Udaipur","B. Jaipur","C. Jodhpur","D. Bikaner"),
           ("A. Elephant","B. Peacock","C. Lion","D. Tiger"),
           ("A. Mahatma Gandhi","B. Jawaharlal Nehru","C. Sardar Patel","D. Dr. B.R. Ambedkar"),
           ("A. 1945","B. 1950","C. 1947","D. 1930"),
           ("A. Qutub Minar","B. India Gate","C. Charminar","D. Taj Mahal"))


answers = ("B", "D", "B", "C", "D",)
guesses = []
score = 0
question_num = 0

for question in questions:

    print("------------------------------------------")
    print(question) 
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
              
        
    question_num += 1


print("------------------------------------------")
print("                RESULTS                   ")
print("------------------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")


































