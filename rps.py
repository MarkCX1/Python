import random

#using random to decide the guess
c = random.randint(0, 2)
guess = int(input("scissor (0), rock (1), paper (2): "))
comp = ""
player = ""
isWon = False


#from the input we decide what the user has chosen and what it is defined as.
if c == 0:
    comp = "scissor"
elif c == 1:
    comp = "rock"
else:
    comp = "paper"

if guess == 0:
    player = "scissor"
elif guess == 1:
    player = "rock"
else:
    player = "paper"

#If statements deciding wether you have won or lost the game
if guess == c:
    print("The computer is", comp, ". You are", player, ". It's a draw")
elif guess == 0 and c == 2:
    print("The computer is", comp, ". You are", player, ". You won")
elif c == 0 and guess == 2:
    print("The computer is", comp, ". You are", player, ". You lose")
elif guess > c and (guess != 0 and c != 2):
    print("The computer is", comp, ". You are", player, ". You won")
elif guess < c and (c != 0 and guess != 2):
    print("The computer is", comp, ". You are", player, ". You lose")