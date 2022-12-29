"""
1. Linear Data Structure
2. Open at both the ends
3. Back/tail/rear - end part of the queue
4. Front/Head - Start of the queue
5. Insertion and Deletion is done at both the end
6. FIFO / LILO methodology (First In First Out)
7. Adding element - ENQUEUE
8. Removing element - DEQUEUE
9. Used in printing things
"""

# Queue implementation using list
queue = []

# Add element at the last
queue.append(10)
queue.append(14)
queue.append(19)

print(queue)

# Remove the first element
queue.pop(0)

print(queue)



