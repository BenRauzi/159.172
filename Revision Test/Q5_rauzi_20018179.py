import random

#I've taken a slightly different approach for minimising conditions than suggested

choices  = { #key beats value
    1: 3, #rock beats scissors
    2: 1, #paper beats rock
    3: 2  #scissors beat paper
}

while True: #while I could use 'while not done', because there is only a single exit point of 'break' this appears cleaner
    user_choice = int(input("Rock (1), Paper (2) or Scissors (3): "))

    program_choice = random.randint(1,3)

    if user_choice == program_choice:
        print("Draw!")
    elif choices[user_choice] == program_choice: #if the choices[user_choice] is the same as program choice (in choices, the key beats the value) then they win.
        print("You Win!")
    else: # Because draws are handled already you lose if the above isn't true ^^
        print("You Lose")

    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "n":
        break