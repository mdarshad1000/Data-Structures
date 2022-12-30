from collections import deque

# Queue implementation using collection module
queue = deque()

# Add element
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)

print(queue)

# Remove element
queue.pop()

print(queue)

# or we can use a combination of `popleft` and `append`