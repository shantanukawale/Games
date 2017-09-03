import random
guessesTaken = 0
 
print('Hello! What is your name?')
myName = raw_input()
 
number = random.randint(1, 1000)
print('Well, ' + myName + ', I am thinking of a number between 1 and 1000.')
guessesRemaining=10
while guessesTaken < 10:
        print('Take a guess.')
	if guessesRemaining>1:
		print('You have '+ str(guessesRemaining) +' guesses remaining.') # There are four spaces in front of print.
        else:
		print('You have '+ str(guessesRemaining) +' guess remaining.')
	guess = raw_input()
        guess = int(guess)
	guessesRemaining=guessesRemaining-1

        guessesTaken = guessesTaken + 1

        if guess < number:
            print('Your guess is too low.')

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)