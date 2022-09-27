import random
import os

from word_list import word_list
from logo import stages, logo

# clear screen 
def clear():
  os.system('clear')

# randomize word to play
word_list_item_array = [x for x in random.choice(word_list)]

# display each character after guess
display = []

for c in range(len(word_list_item_array)):
  display += "_"

# check game end or not variable
end_of_game = False

# lives of player
lives = 6

# player guess character
while end_of_game == False:
  user_guess = input("Guess a letter: ")

  clear()

  # check guess word is contained in word or not
  for index, word in enumerate(word_list_item_array):
    if user_guess == word:
      display[index] = user_guess
      
  # if guess word is not be contained in word, live - 1
  if user_guess not in word_list_item_array:
    print(f"You guessed {user_guess}, that's not in the word. You lose a life")
    lives -= 1

    # if user has no life, end game
    if lives == 0:
      end_of_game = True
      print("YOU LOSE")
      print(logo)
  
  if lives != 0:
    print(display)
  print(stages[lives])
  
  # if user win game
  if "_" not in display:
    end_of_game = True
    print("YOU WIN!")
    print(logo)
