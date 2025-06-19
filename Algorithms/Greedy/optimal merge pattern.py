# When we merge two sorted list then out time complexity is O(sum of elements in two arrays)
'''
  If we have A = [3, 8, 12, 20]
  and B = [5, 9, 11, 16]

  When we use two pointers then our time complexity will be length of A + length of B

  What if we have more than two lists?
  List ->  A B C D
  Sizes -> 6 5 2 3 

  Doing two way merging we get

  When we choose two smaller pairs of merging then we will get optimal merging
  pattern. 

  It can be seen in the paint alongside this python file.  

  ONE EXAMPLE: 
  List ->  x1  x2  x3  x4  x5
  Sizes -> 20  30  10  5   30

  We need to sort it to increasing pattern.
  x4 > x3 > x1 > x2 > x5
'''



