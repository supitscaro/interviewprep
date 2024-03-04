class Stack:
    def __init__(self) -> None:
        self._index = []

    def __len__(self):
        return len(self._index)

    def push(self, item):
        self._index.insert(0, item)

    def pop(self):
        if len(self) == 0:
            raise Exception("The stack is empty.")
        return self._index.pop(0)

    def peek(self):
        if len(self) == 0:
            raise Exception("The stack is empty.")
        return self._index[0]

    def __str__(self) -> str:
        return str(self._index)
