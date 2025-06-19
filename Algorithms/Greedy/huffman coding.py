'''
  Message: BCCABBDDAECCBBAEDDCC
  The main idea is "How to reduce a message length in bits"

  If we use regular 8 bits for each character given above then we have 
  20 * 8 = 160 bits.
  So lets say we have a message that is shown above. And lets say we would like to 
  encode it. Then 

  We can use 0/1 to have show two values.
  We can use _ _ (00, 01,  10, 11) to show 4 values.
  So for our example we need to use four bits _ _ _ (000, 001, 100, 111, 110) values. 

  See the paint example that is within this folder. 
  When you dont use all the bits and use only 3 bits then 
  each character length will be length of it ASCII values multiplied by the code
  ASCII value bits = 8 and there are 5 characters
  so all together it is 8 * 5 = 40 

  Characters = 8 * 5 = 40 and codes = 5 * 3 = 15 
  And altogether it is 55 bits

  Now, 
  That was for table and now for length of the string
  we have 
  length = 20 and it is multiplied by 3 bits each so 20 * 3 = 60 

  altogether it will be 55 + 60 bits which is 115 bits.

  In conclusion, we have 
  Reduced the size from 160 bits to 115 bits. 

  We can further use huffman coding to reduce this size and this is how. 

  Huffman says that we can use the count of the characters to our advantage. 
  See another paint file that is within this folder for visuals.

  To make the tree we sort the characters based on its count. 
  So in this case E, A, D, B and C would be the order.
  And we do the optimal merge pattern approach. 

  And we write 0's to the left of the tree and 1's to the right of the tree. 

  Now for code we just write the path from the root node to the leaf containing that character. 
  If we use huffman coding then we will have 
  Length of the message in bits = each character's code bit * frequency = 45 bits
  Table size = Character bits = 8 * 5 = 40 PLUS code bits = 12 bits

  So all together we have 45 bits + 40 bits + 12 bits = 97 bits
'''