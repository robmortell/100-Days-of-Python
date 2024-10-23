##############################

#Write your code below this line 👇

from time import sleep

print(len("Rob"))
print(len("Helena"))
print(len("Holly"))
print(len("Jack"))

# Here, you simply have to tell python to print the length, or amount of characters inside the quote marks for len

##############################

# You can also use an input with len

# Write your code below this line 👇

from time import sleep
print("The amount of characters in your name is ",(len(input("What is your name...? "))))

# Here, what I struggled to figure out was the comma. I was closing out the first statement with a closing bracket.
# But instead it seems that I needed to use a comma after "The amount of characters in your name is "