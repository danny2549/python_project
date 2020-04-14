#!/usr/bin/env python
# coding: utf-8

# In[6]:


from random import randint

player = input("Player, make your move: ").lower()
random_number = randint(0,2)

#computer logic str----------------------------------
if random_number ==0:
    computer ="rock"
elif random_number==1:
    computer ="paper"
elif random_number==2:
    computer ="scissors"
#computer logic end----------------------------------


if player ==computer:
    print("Its a draw")
#Rock str----------------------------------------------------
elif player =="rock":
    if computer =="scissors":
        print("Rock beats scissors, human wins")
    elif computer =="paper":
        print("Paper beats rock, the machines are rising")
#Rock end--------------------------------------------------------

#Paper str-------------------------------------------------------
elif player =="paper":
    if computer =="scissors":
        print("scissors beats paper, the machines are rising")
    elif computer =="rock":
        print("Paper beats rock, human wins")
#Paper end-------------------------------------------------------

#Scissors str-------------------------------------------------------
elif player =="scissors":
    if computer =="rock":
        print("rock beats scissors, machines win")
    elif computer =="paper":
        print("scissors cut paper, humans win!")
#Scissors end-------------------------------------------------------

#error message str-----------------------------------
else:
    print("check your spelling and please only use rock, paper, or scissors")
#error message end-----------------------------------


# In[ ]:


from random import randint
# print("Rock...")
# print("Paper...")
# print("Scissors...")

player = input("Player, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer plays {computer}" )

if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")	
else:
	print("Please enter a valid move!")

