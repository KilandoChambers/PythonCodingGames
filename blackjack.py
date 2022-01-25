import random


play_blackjack = input("Would you like to play a game of blackjack? Type 'y' for yes and 'n' for no. ")
play_blackjack = play_blackjack.lower()

#give the initial information at beginning of game
def information():
  print(f"  Your cards: {dictionary_player[0]}. Your current score: {dictionary_player[1]}.\n  The computers first card is {dictionary_computer[0][0]}.")

#update player on information in game
def reveal():
  print(f"  Your cards: {dictionary_player[0]}. Your final score: {dictionary_player[1]}.\n  Computer's cards: {dictionary_computer[0]}. Computer's final score: {dictionary_computer[1]}.")

#assess whether player has one or lost the game at end
def assess():
    if dictionary_computer[1] == 21 or dictionary_computer[1] < 21 and dictionary_computer[1] > dictionary_player[1]:
      print("You lose!")
    elif dictionary_computer[1] == dictionary_player[1]:
      print("Tie!")
    else:
      print("You win!")

#modifying 11 to 1 if sum is greater than 21
def modification(opponent):
  hand = opponent[0]
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  hand.append(random.choice(cards))
  for i in list(range((len(hand)))):
    if hand[i] == 11 and sum(hand) > 21:
      hand[i] = 1
  total = sum(hand)
  return hand, total

#determines if player wants to continue
def flag():
  response = input("Would you like to draw another card or pass your turn? Hit or Pass: ").lower()
  return response

#adding card to player's hand
def card_hand():
  if game_status == 1:
    player_hand = []
    computer_hand = []
    player_total = 0
    computer_total = 0
    for i in list(range(0,2)):
      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
      player_hand.append(random.choice(cards))
      computer_hand.append(random.choice(cards))
    computer_total += sum(computer_hand)
    player_total += sum(player_hand)
    return player_hand, player_total, computer_hand, computer_total
  elif response == 'hit':
    player_mod = modification(dictionary_player)
    return player_mod
  elif response == 'pass':
    computer_mod = modification(dictionary_computer)
    return computer_mod 

#total script for game
if play_blackjack == 'y':
  ####-------
  #beginning game with first two cards
  from art import logo
  print(logo)
  game_status = 1
  dictionary_player = card_hand()
  game_status -= 1
  dictionary_computer = dictionary_player[2:4]
  if dictionary_computer[1] == 21:
    reveal()
    print("You lose!")
  elif dictionary_computer[1] != 21 and dictionary_player[1] == 21:
    reveal()
    print("You win!")
  ####----
  #choosing to continue game
  else:
    information()
    response = flag()
    x = 'True'
    y= 'True'
    if response == 'hit':
      while x == 'True':
        dictionary_player = card_hand()
        if dictionary_player[1] > 21:
          reveal()
          print("You Lose!")
          x = 'False'
          y = 'False'
        elif dictionary_player[1] == 21:
          reveal()
          print("You win!")
          x = 'False'
          y = 'False'
        else:
          information()
          response = flag()
          if response != 'hit':
            x = 'False'
      while y == 'True':
        if dictionary_computer[1] < 17:
          dictionary_computer = card_hand()
        elif dictionary_computer[1] >= 17:
          reveal()
          assess()
          y = 'False'     
    elif response == 'pass' and dictionary_computer[1] <= 16:
      while y == 'True':
        dictionary_computer = card_hand()
        if dictionary_computer[1] >= 17:
          reveal()
          assess()
          y = 'False'
    else:
      reveal()
      assess()
elif play_blackjack != 'y' and play_blackjack != 'n':
  print("Invalid input. Try again!")
else:
  print("Bye!")
