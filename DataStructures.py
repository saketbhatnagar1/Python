# LIST DEMONSTRATIONS
print("LIST OPERATIONS")
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")

# Adding elements
my_list.append(6)
print(f"After append(6): {my_list}")

# Extending list
my_list.extend([7,8,92,92])
print(f"After extend([7, 8]): {my_list}")

# Inserting at a specific position
my_list.insert(2, 9)
print(f"After insert(2, 9): {my_list}")

# Removing elements removes the first occurance of the element
my_list.remove(92)
print(f"After remove(92): {my_list}")

# Popping last element
last_element = my_list.pop()
print(f"After pop(): {my_list}, popped element: {last_element}")

# Slicing
print(f"Sliced list (1:4): {my_list[1:4]}")

# List comprehension
squared = [x**2 for x in my_list]
print(f"Squared list comprehension: {squared}")

# Sorting list
my_list.sort(reverse=True)
print(f"Sorted list (descending): {my_list}\n")

# TUPLE DEMONSTRATIONS
print("TUPLE OPERATIONS")
my_tuple = (1, 2, 3, 4, 5)
print(f"Original tuple: {my_tuple}")

# Accessing elements
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")

# Slicing a tuple
print(f"Sliced tuple (1:4): {my_tuple[1:4]}")

# Tuples are immutable, so they can't be modified directly
concatenated_tuple = my_tuple + (6, 7)
print(f"Concatenated tuple: {concatenated_tuple}\n")

# DICTIONARY DEMONSTRATIONS
print("DICTIONARY OPERATIONS")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"Original dictionary: {my_dict}")

# Adding/updating a key-value pair
my_dict['d'] = 4
print(f"After adding 'd': {my_dict}")

# Accessing values
print(f"Value of key 'a': {my_dict['a']}")

# Removing a key-value pair
removed_value = my_dict.pop('b')
print(f"After pop('b'): {my_dict}, removed value: {removed_value}")

# Dictionary keys and values
print(f"Dictionary keys: {list(my_dict.keys())}")
print(f"Dictionary values: {list(my_dict.values())}")

# Merging two dictionaries
new_dict = {'e': 5, 'f': 6}
my_dict.update(new_dict)
print(f"After update with new_dict: {my_dict}\n")

# SET DEMONSTRATIONS
print("SET OPERATIONS")
my_set = {1, 2, 3, 4, 5}
print(f"Original set: {my_set}")

# Adding an element
my_set.add(6)
print(f"After add(6): {my_set}")

# Removing an element
my_set.remove(3)
print(f"After remove(3): {my_set}")

# Set operations: union, intersection, difference
set_b = {4, 5, 6, 7, 8}
print(f"Union of my_set and set_b: {my_set.union(set_b)}")
print(f"Intersection of my_set and set_b: {my_set.intersection(set_b)}")
print(f"Difference of my_set and set_b: {my_set.difference(set_b)}\n")

# FROZENSET DEMONSTRATIONS (immutable set)
print("FROZENSET OPERATIONS")
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(f"Original frozenset: {my_frozenset}")

# Frozenset operations (similar to set but immutable)
print(f"Union of frozenset and set_b: {my_frozenset.union(set_b)}")
print(f"Intersection of frozenset and set_b: {my_frozenset.intersection(set_b)}\n")

# DEQUE DEMONSTRATIONS (from collections)
from collections import deque

print("DEQUE OPERATIONS")
my_deque = deque([1, 2, 3, 4, 5])
print(f"Original deque: {my_deque}")

# Appending to both ends
my_deque.append(6)
my_deque.appendleft(0)
print(f"After append(6) and appendleft(0): {my_deque}")

# Popping from both ends
my_deque.pop()
my_deque.popleft()
print(f"After pop() and popleft(): {my_deque}\n")

# QUEUE DEMONSTRATIONS (using deque as queue)
from queue import Queue

print("QUEUE OPERATIONS")
q = Queue()
q.put(1)
q.put(2)
q.put(3)
print(f"Queue after put(1), put(2), put(3): {list(q.queue)}")

# Removing items from the queue
q.get()
print(f"Queue after get(): {list(q.queue)}\n")

# HEAP DEMONSTRATIONS (using heapq)
import heapq

print("HEAP OPERATIONS")
my_heap = [5, 7, 9, 1, 3]
heapq.heapify(my_heap)
print(f"Heapified list: {my_heap}")

# Pushing and popping from the heap
heapq.heappush(my_heap, 4)
print(f"After heappush(4): {my_heap}")
heapq.heappop(my_heap)
print(f"After heappop(): {my_heap}\n")

# NAMEDTUPLE DEMONSTRATION (from collections)
from collections import namedtuple

print("NAMEDTUPLE OPERATIONS")
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Namedtuple Point: {p}")
print(f"Access x: {p.x}, Access y: {p.y}\n")

# COUNTER DEMONSTRATIONS (from collections)
from collections import Counter

print("COUNTER OPERATIONS")
counter = Counter([1, 2, 2, 3, 4, 4, 4])
print(f"Original Counter: {counter}")
print(f"Most common elements: {counter.most_common(2)}")
counter.update([4, 5, 6])
print(f"Counter after update([4, 5, 6]): {counter}\n")

# STACK OPERATIONS (using list)
print("STACK OPERATIONS")
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(f"Stack after pushes: {stack}")
stack.pop()
print(f"Stack after pop: {stack}\n")

# Summary of all Data Structures and Operations
print("Summary of Data Structures demonstrated: Lists, Tuples, Dictionaries, Sets, Frozensets, Deques, Queues, Heaps, Namedtuples, Counters, and Stack.")
