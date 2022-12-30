"""
 1. Ordered collection of item
 2. Last In First Out principle (LIFO)
 3. Example is Undo-Redo operation
 4. Can be used to reverse a string
 5. Infix to Prefix
 6. Infix to Postfix
 7. Postfix to Infix
 8. Prefix to Infix
 9. Used in Tower of Hanoi
"""

# Stacks implementation in python using list
stack = []

# Add element at the last 
stack.append(10)
stack.append(2)
stack.append(30)

print(stack)

# remove last element
stack.pop()

print(stack)

# check length of stack
print(len(stack))

# check if stack is empty or not
print(not stack)


