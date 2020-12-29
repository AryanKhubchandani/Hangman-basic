import random


# Variables

animals = []
fruits = [] 
sports = []
guessed = []
guesslist = []
category = ''
play = True
cont = "Y"
attempts = 6


# Making lists for different catergories

a = open("animals.txt")

for line in a:
  stripped_line1 = line.strip()
  animals.append(stripped_line1)

f = open("fruits.txt")

for line in f:
  stripped_line2 = line.strip()
  fruits.append(stripped_line2)
  
s = open("sports.txt")

for line in s:
  stripped_line3 = line.strip()
  sports.append(stripped_line3)
# Work Space

print("Hello, let's play Hangman!")

while True:
    
    while True:
        
        # Check for category
        
        if category.upper() == 'A':
            word = random.choice(animals)
            break
        
        elif category.upper() == 'F':
            word = random.choice(fruits)
            break
        
        elif category.upper() == 'S':
            word = random.choice(sports)
            break
        
        else:
            category = input("Please select a valid category: A for Animals / F for Fruits / S for Sports \nX to exit \n")
        
        if category.upper() == 'X':
            print("See you later!")  
            play = False
            break

    # Main loop
    
    if play:
        
        wordlist = list(word.upper())
        
        # The word to be guessed
        def printg():
            print("\nYour word is: " + ' '.join(guesslist))

        for i in wordlist:
             guesslist.append('_')
        printg()

        # Taking input from the user
        while True:

            print("\nGuess a letter: ")
            letter = input()
            letter = letter.upper()
            
            if not letter.isalpha():
                print("You have given a wrong input, please use a letter")

            if letter.upper() in guessed:
                print("You have already guessed this letter, try a different letter")
            
            # Checking whether the guess is correct  
            
            else:
                guessed.append(letter.upper())
                
                if letter.upper() in wordlist:
                    print(letter.upper(),"is in the word!")
                    
                    if attempts> 0:
                        print("You have",attempts, "guesses left!")
                        
                        for i in range(len(wordlist)):
                            
                            if letter.upper() == wordlist[i]:
                                index = i
                                guesslist[index] = letter.upper()
                                printg()
                                
                else:
                    print("Wrong guess,", letter.upper(), "is not in the word.")
                    attempts -= 1
                    if attempts> 0:
                        print("You have",attempts, "guesses left!")
                        printg()

            # Check for Win/Lose
            
            guessedword = ''.join(guesslist)
            
            if guessedword.upper() == word.upper():
                print("\nYou guessed the word!")
                break
            
            elif attempts == 0:
                print("\nOops, you're out of guesses!")
                print("The word was: ", word.upper())
                break
        
        # Continuing the game
        
        cont = input("Press Y to play again, X to quit\n")
        if cont.upper() == 'Y':
            category = input("Please select a valid category: A for Animals / F for Fruits / S for Sports \nX to exit \n")
            guesslist = []
            guessed = []
            play = True
            attempts = 6
            
        elif cont.upper() == 'X':
            print("\nThank You for playing.")
            break
        
    else:
        break