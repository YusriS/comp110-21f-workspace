"""relational operators program practice."""
__author__ = "730531303"
left_hand_side: str = input("What is the left side value? ")
right_hand_side: str = input("What is the right side value? ")
lhs = int(left_hand_side) 
rhs = int(right_hand_side)
print(str(str(left_hand_side) + " < " + str(right_hand_side) + " is ") + str(bool(lhs < rhs)))
print(str(str(left_hand_side) + " >= " + str(right_hand_side) + " is ") + str(bool(lhs >= rhs)))
print(str(str(left_hand_side) + " == " + str(right_hand_side) + " is ") + str(bool(lhs == rhs)))
print(str(str(left_hand_side) + " != " + str(right_hand_side) + " is ") + str(bool(lhs != rhs)))