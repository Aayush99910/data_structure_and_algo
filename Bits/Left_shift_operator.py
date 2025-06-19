# When we do left shift to a bit then we are shifting by that x position and 
# adding zeroes on the right 
# we discard if the shifted bit in the left overflows 
# in integer each bit shift is multiplication of 2

# 4 << 3 
# 00000100 then it will be 00100000 
# and in integer it is 4 * 2 * 2 * 2
value = 4 
shift = 3 
result = value << shift 

print("Original integer:", value)
print("Binary of 4:", format(value, '08b'))
print(f"After left shift by {shift}:", format(result, '08b'))
print("Resulting integer:", result)


"""
Ex 1: Write a Python code snippet to perform a left bitwise shift operation on 12 by 3
positions, and print the result in both decimal and binary formats, each in a different line.
"""

def left_shift(value: int, shift: int) -> None: 
    result = value << shift 

    print("Decimal: ", result)
    print("Binary: ", format(result, '08b'))

left_shift(12, 3)


"""
Jack, an engineer at AutoSense Inc., is amplifying sensor signals for autonomous systems.
He uses the left shift operator to multiply the signals, ensuring stronger and more accurate readings.
Requirement:
Write a Python function that shifts the binary sensor data to the left to amplify the signal.
"""

def amplify_sensor_signal(sensor_data: str, shift: int) -> str: 
    sensor_data_int = int(sensor_data, 2)
    result = sensor_data_int << shift 
    return bin(result)

print(amplify_sensor_signal("110", 3)) # Output: "0b110000"

