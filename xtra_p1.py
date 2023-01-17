"""
Name: Levi Lowther  Date: 17Jan2023 Purpose: To make a playable game that is totally not Rock Paper Scissors. 
 When I first cloned this repo to my computer and started making my way through all of the files, I saw this little game 
 that we were going to get to play with and started working on it. But quickly realized that I had many other things I 
 should work on before the extra credit. 

"""

import random

# Change the name below to a name of your choice

name = "Jeeves"

# Fix the code below to print the name using an f-string

print()
print("Hello, I'm " + name + ", your gamebot.")
print("Let's play an animal guessing game!")
print("There are 3 animals: wolf, eagle, snake (a Python of course).")
print("The wolf scares the eagle.")
print("The eagle grabs the snake.")
print("The snake bites the wolf.")
print("I'll pick one and you pick one and we'll see who wins.")
print()

# Right now, the user choses wolf everytime.
# Modify the code so the user is asked to
# enter wolf, eagle, or snake.
# Hint: use the input() function

user_choice = input("Choose one: wolf, eagle, or snake.")

# Now the bot will pick one
buddy_choice = random.choice(["wolf", "eagle", "snake"])

# Report the choices
print()
print(f"You said {user_choice}.")
print(f"I said {buddy_choice}.")
print()


# Now we need to compare the choices and determine the winner
# Complete the logic to
# compare the choices and print who won
# In Python, indentation is important!
# we started with the tied outcome which eliminated several options. I was left with evaluating the rest of the outcomes. 

if user_choice == buddy_choice:
    print("We tied!")
elif user_choice == "wolf":
    if buddy_choice == "snake":
        print("My snake bit your wolf! I win!")
    else:
        print("Your wolf scared my eagle! You win!") 
elif user_choice == "snake":
    if buddy_choice == "wolf":
        print("Your snake bit my wolf! You win!") 
    else:
        print("My eagle grabbed your snake! I win!")           
elif user_choice == "eagle":
    if buddy_choice == "snake":
        print("Your eagle grabbed my snake! You win!")
    else:
        print("My wolf scared your eagle. I win!")    
# When you finish,
# right-click on the code and select "Format Document"

# Run the code, and play the game a few times.
# Copy the output from the terminal and paste it into 
# a new file named xtra_p1out.txt.
