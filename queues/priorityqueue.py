"""
 PRIORITY QUEUE:
 1. Each element is associated with a priority ans is served accordingly
 2. If priority is same, they are served according to their order in queue
"""

# Lets take high value = high priority

q = []

q.append(13)
q.append(43)
q.append(4)
q.sort()

print(q)

# Remove element acc to priority
q.pop()
print(q)
