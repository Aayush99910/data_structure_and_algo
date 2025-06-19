# It is the opposite of left shift.
# The main thing that is opposite is that when you do a right shift:
# - Zeros are added to the left side (for positive numbers).
# - Bits on the right are discarded (they fall off).
# - The decimal value is divided by 2 for each shift.
#
# Note: This behavior is for positive numbers.
# For negative numbers, Python preserves the sign by filling in 1s on the left.
# It performs floor division (e.g., -3 >> 1 becomes -2, not -1).

"""
Ex 13: Write a Python code snippet to perform a right bitwise shift operation on 12 by 3
positions, and print the result in both decimal and binary formats, each in a different line.
"""
value = 12 
shift = 3 
result = value >> shift 

print("Original integer:", value)
print("Binary of 4:", format(value, '08b'))
print(f"After left shift by {shift}:", format(result, '08b'))
print("Resulting integer:", result)


"""
Ethan, an autonomous vehicle engineer at DriveTech Inc., needs to reduce the speed of a
vehicle using binary data. Each right shift represents halving the current speed.
Requirement:
Write a Python function that halves the vehicle's speed by shifting the binary representation of
the speed to the right.
"""

def reduce_speed(binary_speed: str) -> str:
    halved_speed = int(binary_speed, 2) >> 1 
    return bin(halved_speed)


print(reduce_speed("1010")) # Output: "0b101"