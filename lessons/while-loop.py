"""While loop example"""
counter: int = 0
maximum: int = int(input("count up to but not including what number?"))
while counter < maximum:
    counter_squared: int = counter ** 2
    print("the square of " + str(counter) + "is" + str(counter_squared))
    counter = counter + 1
print("Done!")