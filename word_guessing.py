import random

name = input("What is your name? ")

print("Goodluck, " + name + "!")

words = ["rainbow", "computer", "science", "programming", "python", "mathematics", "player", "condition", "reverse", "water", "board", "geeks"]

#function will choose one random word from this list of words
word = random.choice(words)
print(word)

print("Let's play Guess The Word. Input a letter.")

guesses = ""

#number of turns
turns = 8

while turns > 0:
    #var to count number of times a user fails
    failed = 0

    #all characters from the input word taking one at a time
    for char in word:
        #comparing the input character with the character in guesses
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            #for every failure, 1 will be incremented in failed count
            failed += 1
    if failed == 0:
        #user will win the game if failure is 0 and print 'You Win!'
        print("\nYou win!")
        #print the correct word
        print("The word is:", word)
        break
    #if user inputs the wrong character then it will ask user to enter another alphabet
    print()
    guess = input("\nguess a character: ").lower()
    #check if the guesses letter has already been guessed
    if guess in guesses:
        print("You've already guessed that letter. Try again.")
        continue
    #every input character will be stored in guesses
    guesses += guess
    #check input with the character in word
    if guess not in word:
        turns -= 1
        #if character doesnt match the word then 'Wrong' will be given as output
        print("Wrong")
        #This will print the number of turns left for the user
        print("You have", turns, "more guesses")

        if turns == 0:
            print("\nYou Lose!")
            print("The word was:", word)