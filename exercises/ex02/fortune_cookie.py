"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730531303"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune = randint(0, 10)
if fortune > 5:
    print("You will achieve an A on your next exam")
else:
    print("You will meet a new friend in an unlikely place")

print("Now, go spread positive vibes!")