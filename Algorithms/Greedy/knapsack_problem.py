'''
  We are given weights and profits of N items, in the form of {profit, weight}, we need to put these items in a knapsack
  of capacity W to get the maximum total profit in the knapsack.

  Illustration: 
    arr[] = {{100, 20}, {60, 10}, {120, 30}} and W = 50 
    So first we sort the array in descending order using (profit/weight) ratio. The sorted array will be 
    {{60, 10}, {100, 20}, {120, 30}} 

    Now, the thing that we need to do is at each iteration
    1) Check if the weight is less than the total W.
    2) If it is add the whole item and the total profit. 
    3) If it is not then we need to multiply the fractional ratio that is calculated like this (Total W / that weight) * profit then add this value

    Thats it
'''


def partition(arr: list, start: int, end: int) -> int: 
  pivotElement = arr[end]
  profit_pivot = pivotElement[0]
  weight_pivot = pivotElement[1]
  ratio_pivot = profit_pivot / weight_pivot  
  pivotIndex = start 

  for i in range(start, end): 
    item = arr[i]
    profit = item[0]
    weight = item[1]
    ratio = profit / weight 
    if (ratio > ratio_pivot):
      arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i]
      pivotIndex += 1
    
  arr[pivotIndex], arr[end] = arr[end], arr[pivotIndex]
  return pivotIndex

def sort_profit_weight(arr: list, start: int, end: int) -> None:
  if (start < end): 
    pi =  partition(arr, start, end)
    sort_profit_weight(arr, start, pi - 1)
    sort_profit_weight(arr, pi + 1, end)
  

def fractional_knapsack(W: int, arr: list) -> int:
  sort_profit_weight(arr, 0, len(arr) - 1)

  total_profit = 0

  for item in arr: 
    # checking if the weight of an item is greater than the total weight or not
    weight =  item[1]
    profit = item[0] 
    if (weight < W): 
      total_profit += profit 
      W = W - weight 
    else: 
      total_profit += (W / weight) * profit 
      break 
  
  return total_profit

array1 = [(100, 20), (60, 10), (120, 30)]
capacity = 50
print(fractional_knapsack(capacity, array1))
  