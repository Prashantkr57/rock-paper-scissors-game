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

choice = int(
    input(
        "What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if choice == 0:
    print(rock)

elif choice == 1:
    print(paper)

elif choice == 2:
    print(rock)

com_choice = random.randint(0, 3)
print("Computer Chose:")
if com_choice == 0:
    print(rock)

elif com_choice == 1:
    print(paper)

elif com_choice == 2:
    print(rock)

if (choice == 0 and com_choice == 2) or (choice == 1 and com_choice == 0) or (choice == 2 and com_choice == 1):
  print("You Won")

else:
  print("You Lose")