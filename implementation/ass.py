from queue import PriorityQueue

q = PriorityQueue()

class test:
    def __init__(self) -> None:
        self.val = 10
        self.next = 10

q.put((1, test()))
q.put((1, test()))

print(q.get())