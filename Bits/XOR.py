"""
Ex 2: Write a program that takes two binary strings, bin1 and bin2, as input and performs a
bitwise ^ operation on them. The program should directly output the result of the bitwise ^
operation as a binary string without converting the inputs to decimal integers.
"""

def bitwise_xor(binary_string_1: str, binary_string_2: str) -> str: 
    result = ""

    i = len(binary_string_1) - 1
    j = len(binary_string_2) - 1
    
    while i >= 0 or j >= 0:
        bit1 = int(binary_string_1[i]) if i >= 0 else 0 
        bit2 = int(binary_string_2[j]) if j >= 0 else 0 

        result = str(bit1 ^ bit2) + result 
        i -= 1
        j -= 1

    return result 


# testing 
def main(): 
    bin1 = "1101001"
    bin2 = "1011001"
    print("Bitwise XOR of", bin1, "and", bin2, "is:", bitwise_xor(bin1,bin2)) # should output "Bitwise XOR of 1101001 and 1011001 is: 0110000"


if __name__ == "__main__":
    main() 
