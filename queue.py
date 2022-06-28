#initialize a new deque
from collections import deque

queue = deque()
# Add 2 to the end of the  deque
queue.append(2)
# Add 4 to the front of the deque
queue.appendleft(4)
# Look at the end of the deque and print it
print(queue[-1])

# Look at the front of the deque and print it
print(queue[0])
# Remove the end of the deque

queue.pop()
# Remove the front of the deque
queue.popleft()

# pythons collections.deque is a double-ended queue which means you can push
# and pop an element from either end in constant time

q = deque()
# enqueue: q.append, O(1)
# dequeue: q.popleft(), O(1)
# size: len(q), O(1)
# most queues most often in breath-first search
#  cover monotonic deque where elements are sorted inside the deque
#  that is useful in solving some advanced coding problems