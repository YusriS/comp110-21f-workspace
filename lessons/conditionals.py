"""COnditional If else state"""
SECRET: int = 3
print("Im thinking of a number between one and five, What is it?")
guess: int = int(input("what is your guess? "))
if guess == SECRET: 
    print("You guessed correctly!! What are you psychic?")
    print("Have a wonderful day")
else:
    print("I'm sorry. I am afraid you are incorrect")
    if guess > SECRET:
        print("you guessed too high! Try again")
    else:
        print("you guessed to low!")
print("game over")