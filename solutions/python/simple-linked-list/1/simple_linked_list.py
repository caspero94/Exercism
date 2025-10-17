class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value
        
    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self.head_node = None
        for value in values:
            self.push(value)

    def __iter__(self):
        current = self.head_node
        while current:
            yield current.value()
            current = current.next()
    
    def __len__(self):
        current = self.head_node
        count = 0
        while current:
            count += 1
            current = current.next()
        return count

    def head(self):
        if not self.head_node:
            raise EmptyListException("The list is empty.")
        return self.head_node

    def push(self, value):
        new_node = Node(value)
        new_node._next = self.head_node
        self.head_node = new_node

    def pop(self):
        if not self.head_node:
            raise EmptyListException("The list is empty.")
        value = self.head_node.value()
        self.head_node = self.head_node.next()
        return value

    def reversed(self):
        reversed_list = LinkedList([])
        current = self.head_node
        while current:
            reversed_list.push(current.value())
            current = current.next()
        return reversed_list


class EmptyListException(Exception):
    pass
