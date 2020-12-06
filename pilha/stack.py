class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        if self.items == []:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.empty():
            return self.items[-1]
        else:
            return None

    def add(self, item):
        self.items.append(item)

    def remove(self):
        self.items.pop()

