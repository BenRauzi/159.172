import random

#There are some areas in this code I have not ENTIRELY followed the guidelines as the improvements I have made will increase either code readability or complexity
#Instructions allow for this

print("""
Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and out run the natives.
""") #multi-line print is a better solution than BOTH one print with mutliple newlines (\n) AND 4 print() statement


miles_travelled_camel = 0
miles_travelled_natives = -10 #natives start 10mi behind the camel. Closer than suggested to make the game more difficult
thirst = 0
camel_tiredness = 0
drinks_in_canteen = 3


while True: #loop will go infinitely until Broken. I have chosen to not use 'done' to reduce unnessecary comparisons
    print("""
A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop for the night.
E. Status check.
Q. Quit.
""")
    
    user_choice = input("Your choice? ")

    user_choice = user_choice.upper() #prevents needing to use .upper() in every if statement which is unnessecary complexity
        
    if user_choice == "Q":
        break #exits the loop

    elif user_choice == "E":
        print(f"\nMiles traveled:  {miles_travelled_camel}\nDrinks in canteen:  {drinks_in_canteen}\nThe natives are {abs(miles_travelled_camel - miles_travelled_natives)} miles behind you.")

    elif user_choice == "D":
        camel_tiredness = 0
        miles_travelled_natives += random.randint(7,14) #random.randint is inclusive of last item
        
        print("\nThe Camel is happy")

    elif user_choice == "C":
        distance_travelled = random.randint(10,17) #slightly lower than suggested to increase difficulty

        miles_travelled_camel += distance_travelled #we could move this logic to a function if we wanted to reduce code duplication
        thirst += 1
        camel_tiredness += random.randint(1,3)
        miles_travelled_natives += random.randint(7,14)

        print(f"\nYou traveled {distance_travelled} miles.")

    elif user_choice == "B":
        distance_travelled = random.randint(5,12)

        miles_travelled_camel += distance_travelled
        thirst += 1
        camel_tiredness += 1
        miles_travelled_natives += random.randint(7,14)

    elif user_choice == "A":
        if drinks_in_canteen > 0:
            thirst = 0
            drinks_in_canteen -= 1
            print("You take a swig of the cool refreshing water from your canteen")
        else:
            print("You have no drinks left in your canteen!")

    #blocks with breaks are placed above blocks without. This means we don't tell the user they are thirsty if they have already won/lost in the same turn
    #no need for elif because if one condition is true it will break, preventing the execution from reaching the next branch

    if thirst > 6: #if thirst is ABOVE 6 user dies of thirst
        print("You died of thirst")
        break

    if camel_tiredness > 8: #if tiredness is ABOVE 8 camel dies - because the camel is dead the user loses
        print("Your camel is dead.")
        break

    if miles_travelled_camel >= 200:
        print("You made it across the desert! You won!")
        break

    if miles_travelled_natives >= miles_travelled_camel:
        print("You were caught! You lose")
        print(f"You were {200 - miles_travelled_camel} miles from safety")
        break

    if thirst > 4: #if thirst is ABOVE 4 notify user
        print("You are thirsty")   
    
    if camel_tiredness >= 5:
        print("Your camel is getting tired.")
    
    if abs(miles_travelled_camel - miles_travelled_natives) < 15 and user_choice != "E": #because loop is broken if natives catch or pass the camel, this will not print when user is passed. No need to print on 'E'
        print("The natives are getting close!")

    if random.randrange(20) == 0 and (user_choice == "B" or user_choice == "D"): #1 in 20 chance of finding Oasis IF the user has moved   
        print("You found an oasis!")
        thirst = 0
        drinks_in_canteen = 3
        camel_tiredness = 0