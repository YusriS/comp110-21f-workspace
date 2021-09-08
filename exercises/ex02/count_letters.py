"""Counting letters in a string."""

__author__ = "730531303"


letter = input("What letter do you want to seach for? ")
word = input("Enter a word: ")
length = len(word) 
count: int = 0
number: int = 0
while count < length:
    if word[count] == letter:
        number = number + 1
    else:
        number = number
    count = count + 1
print(number)    