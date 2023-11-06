rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
import math

player_1 = int(input("What's your choice? type 0 for rock, 1 for paper, or 2 for scissors. "))

computer = math.floor(random.random() * 3)


if player_1 == 0:
  print(rock)
  print("Rock!")
elif player_1 == 1:
  print(paper)
  print("Paper!")
elif player_1 == 2:
  print(scissors)
  print("Scissors!")  

if computer == 0:
  print(rock)
  print("Rock!")
elif computer == 1:
  print(paper)
  print("Paper!")
elif computer == 2:
  print(scissors)
  print("Scissors!")

if player_1 == computer:
  print("It's a tie!")
elif player_1 == 0 and computer == 1:
  print("You lose!")
elif player_1 == 0 and computer == 2:
  print("You win!") 
elif player_1 == 1 and computer == 0:
  print("You win!") 
elif player_1 == 1 and computer == 2:
  print("You lose!") 
elif player_1 == 2 and computer == 0:
  print("You lose!") 
elif player_1 == 2 and computer == 1:
  print("You win!")