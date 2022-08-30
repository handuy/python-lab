class EmptyStackErr(Exception):
    pass

class ArrayStack:
    # init constructor gán 1 empty list [] cho private attribute _data
    def __init__(self):
        self._data = []

    # private method __len__ trả về len(self._data)
    def __len__(self):
        return len(self._data)

    # method is_empty check if len(self._data) == 0
    def is_empty(self):
        return len(self._data) == 0

    # method is_empty check if len(self._data) == 0
    def get(self):
        return self._data

    # method push thêm phần tử vào stack (append vào list)
    def push(self, item):
        self._data.append(item)

    # method top trả về phần tử trên cùng của stack (list[-1])
    def top(self):
        if self.is_empty():
            raise EmptyStackErr("Empty stack")
        return self._data[-1]

    # method pop lấy phần tử trên cùng của stack (pop khỏi list)
    def pop(self):
        if self.is_empty():
            raise EmptyStackErr("Empty stack")
        return self._data.pop()