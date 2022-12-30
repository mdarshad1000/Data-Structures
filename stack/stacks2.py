from collections import deque

# Stack implementation using collections modules
stack = deque()

print(stack)

# Add elements at last
stack.append(10)
stack.append(29)
stack.append(30)

print(stack)

# remove last element
stack.pop()

print(stack)

# check length of stack
print(len(stack))

# check if stack is empty or not
print(not stack) 