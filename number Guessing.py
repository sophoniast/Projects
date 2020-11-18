import random

print("Welcome to Guess The Number!")
print("The rules are simple. I will think of a number and you try to guess it.")

number = random.randint(1,10)

isGuessRight = False

while not isGuessRight:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == number:
            print(f"You guessed {guess}. That is right! you win!")
            isGuessRight = True
        else:
            print(f"You guessed {guess}.Sorry, that isn't it. Try Again")
    except:
        print("please enter a proper integer")