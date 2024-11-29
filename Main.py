# Quiz Game

def new_game():
    guesses = []
    correct_guesses = 0
    ques_num = 1

    for key in question:
        print("-----------------------")
        print(key)
        for i in options[ques_num-1]:
            print(i)
        guess = input("Enter your answer: ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(question.get(key), guess)
        ques_num += 1

    display_score(correct_guesses, guesses)


# ---------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("Correct")
        return 1
    else:
        print("False")
        return 0


# ---------------------------
def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("Answers: ", end="")
    for i in question:
        print(question.get(i), end=", ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=", ")
    print()

    score = ((correct_guesses/len(question))*100)
    print(f"Score: {score}%")


# ---------------------------
def play_again():

    response = input("Again? (yes/no): ").lower()

    if response == "yes":
        return True
    else:
        return False


# ---------------------------
question = {"who created python: ": "B",
            "which animal is a rodent?: ": "A",
            "which continent is the largest: ": "C",
            "Which chef's favourite food is beef wellington: ": "D"
            }

options = [["A. Bjarne Stroustrup", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Brendan Eich"],
           ["A. Capybara", "B. Giraffe", "C. Hawk", "D. Pufferfish"],
           ["A. South America", "B. North America", "C. Asia", "D. Australia"],
           ["A. Jamie Oliver", "B. Guy Fieri", "C. Chef Wan", "D. Gordon Ramsey"]]

new_game()

while play_again():
    new_game()

print("See ya Chump")