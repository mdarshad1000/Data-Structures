from queue import Queue

# Queue implementation using `queue` module
q = Queue()

# Add element
q.put(10)
q.put(90)
q.put(50)

print(q)

# Remove element
q.get()
