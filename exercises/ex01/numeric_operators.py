"""Program practice with numeric operators."""
__author__ = "730531303"
left_hand_side: str = input("What is the left side value? ")
right_hand_side: str = input("What is the right side value? ")
lhs = int(left_hand_side) 
rhs = int(right_hand_side)
print(str(lhs) + " ** " + str(rhs) + " is " + str((int(left_hand_side) ** int(right_hand_side))))
print(str(lhs) + " / " + str(rhs) + " is " + str((int(left_hand_side) / int(right_hand_side))))
print(str(lhs) + " // " + str(rhs) + " is " + str(int(left_hand_side) // int(right_hand_side)))
print(str(lhs) + " % " + str(rhs) + " is " + str(int(left_hand_side) % int(right_hand_side)))