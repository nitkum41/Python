"""
The computer will think of 3 digit number that has no repeating digits.
You will then guess a 3 digit number
The computer will then give back clues, the possible clues are:

Close: You've guessed a correct number but in the wrong position
Match: You've guessed a correct number in the correct position
Nope: You haven't guess any of the numbers correctly

Based on these clues you will guess again until you break the code with a
perfect match!

"""
import random
digits = [str(num) for num in range(10)]
random.shuffle(digits)
gen = digits[:3]
print(gen)

play = True
print("welcome code breaker ! let's see if you can guess my 3 digit number ! \n code has been generated,please guess a three digit number")


while(play):
    guess = input("What is your guess? ")
    print(guess)
    if int(guess)!=100*int(gen[0])+10*int(gen[1])+int(gen[2]):
        if guess[0]==gen[0] or guess[1]==gen [1] or guess[2]==gen[2]:
            print("Here is the result of your guess: \n CLOSE")
            continue
        elif guess[0] in gen or guess[1] in gen or guess[2] in gen:
            print("Here is the result of your guess: \n MATCH")
            continue
        else:
            print("Here is the result of your guess: \n NOPE")
            continue

    else:
        play=False
print('You have broken the code and the number is {}'.format(guess))
