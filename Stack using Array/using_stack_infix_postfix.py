stack = [] # using list as a stack data structure 

priority = {
    '+': 1, 
    '-': 1, 
    '*': 2, 
    '/': 2, 
    '^': 3
}

infix_expression = "((3 * 5) + (4 / 3) - 4)"
postfix_expression = ""

for char in infix_expression:
    if char.isdigit():
        postfix_expression += char 
    elif char == "(":
        stack.append(char) 
        # if it is a closing parenthesis need to pop everything out until we see the opening
    elif char == ")":
        while len(stack) > 0 and stack[-1] != "(":
            postfix_expression += stack.pop()
        stack.pop()
    elif char == " ":
        continue 
    else:
        while len(stack) > 0 and stack[-1] != "(" and priority[char] <= priority[stack[-1]]:
            postfix_expression += stack.pop()
        stack.append(char) 
            
# adding all the items from stack to the expressions
while len(stack) > 0:
    element = stack.pop()
    postfix_expression += element 

print(postfix_expression)