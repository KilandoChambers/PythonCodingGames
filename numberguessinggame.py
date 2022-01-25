#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
answer = random.randint(1, 100)

def game_update(number):
  global flag
  def assess():
    if number_guess == answer:
      return "correct"
    elif number_guess < answer:
      return "low"
    else:
      return "high"
  while flag < number:
    number_guess = int(input("Guess a number: "))
    loop_checker = assess()
    if loop_checker != "correct" and flag == number - 1:
      flag += 1
      print(f"Your guess was not correct. The correct answer was {answer}. Better luck next time.")
    elif loop_checker != "correct":
      flag += 1
      print(f"Your guess was too {loop_checker}! You have {number - flag} attempts left.")
    else:
      flag += 10
      print(f"Your guess was correct! The correct answer is {answer}. Good job!")
  
game_start = input("Welcome to the number guessing game!\nWould you like to choose the hard or easy level: ").lower()
flag = 0
if game_start == 'easy':
  game_update(10)
elif game_start == 'hard':
  game_update(5)
