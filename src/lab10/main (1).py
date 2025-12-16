from src.lab10.linked_list import SinglyLinkedList
from src.lab10.structures import Stack, Queue


obj = SinglyLinkedList()
obj.append(1)       # 1
obj.append(2)       # 1 -> 2
obj.prepend(3)      # 3 -> 1 -> 2
obj.insert(1, 4)    # 3 -> 4 -> 1 -> 2
obj.remove_at(2)    # 3 -> 4 -> 2
print("LinkedList contents:")
print(repr(obj))



obj = Stack()
obj.push(1)
obj.push(2)
obj.push(3)
print("Stack contents:")
while not obj.is_empty():
    print(obj.pop())


obj = Queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
print("Queue contents:")
while not obj.is_empty():
    print(obj.dequeue())