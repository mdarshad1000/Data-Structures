from queue import PriorityQueue

# Priority queue implementation using queue module
# It takes lowest value as highest priority
q = PriorityQueue()


# Add elements
q.put(12)
q.put(82)
q.put(23)
q.put(67)
q.put(10)

print(q)

# Remove element
q.get()