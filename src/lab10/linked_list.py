class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"[{self.value}]"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # ошибка: размер не обновляется
        self._size = 0

    def append(self, value):
        """Добавить элемент в конец списка"""
        self._size += 1
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return

        self.tail.next = new_node
        self.tail = self.tail.next
        

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        self._size += 1
        new_node = Node(value, next=self.head)
        if self.head is None:
            self.tail = new_node
        self.head = new_node
        

    def remove_at(self, idx):
        """Удаление по индексу — неполная реализация, есть ошибки"""
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of range")

        if idx == 0:
            if self._size == 1:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
            self._size -= 1
            return


        current = self.head
        for _ in range(idx - 1):
            current = current.next
        if self.tail == current.next:
            self.tail = current

        current.next = current.next.next
        self._size -= 1


    def insert(self, idx, value):
        """Вставка по индексу — неполная реализация, есть ошибки"""
        if idx < 0 or idx > self._size:
            raise IndexError("Index out of range")

        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size


    
    def __repr__(self):
        """
          [A] -> [B] -> [C] -> None
        """
        current = self.head
        str = ""
        for _ in range(self._size):
            str += f"{current.value} -> "
            current = current.next
        return str + "None"