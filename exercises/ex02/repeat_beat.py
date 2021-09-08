"""Repeating a beat in a loop."""

__author__ = "730531303"

counter: int = 1
empty: str = ""
beat = input("What beat do you want to repeat? ")
rep = int(input("How many times do you want this repeated? "))
if rep > 0:
    while counter <= rep:
        if counter == rep:
            empty = empty + beat
        else:
            empty = empty + beat + " "
        counter = counter + 1
    print(empty)
else:
    print("no beat")