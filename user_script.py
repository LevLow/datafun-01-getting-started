""" I am going to attempt to apply the ideas for this assignment art experience
 """

import webbrowser 
print()
print("Welcome to Python Art Emporium!")
print()
username1 = input("What would you like to be called during this transaction?") 
print()
print('Greetings' + username1 + ', it is a pleasure meeting you!')
print()
print('We are inerested in knowing a little about your experince with art. Please answer the questions below.')
print()
#get user data
age = input ("How old are you?" )
art = input("How many pieces of art do you own? ")
print()
museum = input("How many art museums have you been to? ")
print()
future_art = input("How many pieces of art would you like to buy? ")
print()

#convert to numbers
age1 = int(age)
art1 = float(art)
museum1 = float(museum)
futureart1 = float(future_art)

#find sum
sum = art1 + museum1 + futureart1

#find average

average = round( sum / 3, 2)

#find product 

product = art1 * museum1 * futureart1

#find smallest 

smallest = min(art1, museum1, futureart1)

#find largest

largest = max(art1, museum1, futureart1)

#find range

range = largest - smallest

# print the results
print("I am going to do some math and coding stuff \
     with the nubmers you gave me. Just go with it," + username1 + ". Thanks.")
print()
print(f"The sum is {sum}.")
print(type(sum))
print(f"The average is {average}.")
print(type(average))
print(f"The product is {product}.")
print(type(product))
print(f"The smallest is {smallest}.")
print(type(smallest))
print(f"The largest is {largest}.")
print(type(largest))
print(f"The range is {range}.")
print(type(range))
print("There, that wasn't so bad, was it?")
print()
# conditions and branching

comment1 = "You are quite the travler!"
comment2 = "You are quite the collector!"
comment3 = "You will have a huge collection one day!"

if art1 > museum1:
    print(comment2)
elif museum1 > futureart1:
    print(comment1)
elif futureart1 > art1:
    print(comment3)

#add something funny

str_response = input("Would you like to read a comic about art? (y/n) ")

if str_response == "y":
    webbrowser.open ("https://xkcd.com/2018")
elif str_response == 'n':
    print ("Lighten up" + username1 + " we are trying to have fun here.")









