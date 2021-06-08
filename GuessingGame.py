import random

# this is the variables

#number is the computer generated value
number = random.randrange(1,50)

#guesses = the number inputted by the user
guess = int(input("Guess a number between 1 and 50: "))

#while the number entered by the user does not equal the number picked by the
#computer
while guess != number :

  #if the guess is less that the number tell the user to guess higher
  # and offer them another guess
  if guess<number:
    print("You need to guess Higher")
    guess = int(input("\nGuess a number between 1 and 50: "))

   # else the number has to be higher than the number selected and therefore
   #the user is prompted to guess lower and offered another guess
  else:
    print("You need to guess Lower")
    guess = int(input("\nGuess a number between 1 and 50: "))

# if the number is equal to the guess, tell the user they guessed the number.
print("You guessed the number!")
