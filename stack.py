class Stack:
    """Класс, реализующий структуру данных Стек (LIFO)."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Попытка просмотра пустого стека")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)