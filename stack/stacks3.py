from queue import LifoQueue

# Stack implementation using Queue module
stack = LifoQueue()

# Add elements at the end 
stack.put(10)
stack.put(14)
stack.put(15)

print(stack)

# Remove the last element
stack.get()