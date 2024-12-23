from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque([])
        self.queue2 = deque([])

    def push(self, x: int) -> None:
        queue = self.queue1 if len(self.queue1) > 0 else self.queue2
        queue.append(x)

    def pop(self) -> int:
        queue = self.queue1 if len(self.queue1) > 0 else self.queue2
        queue_backup = self.queue1 if len(self.queue2) > 0 else self.queue2
        while len(queue) > 1:
            queue_backup.append(queue.popleft())
        return queue.popleft()

    def top(self) -> int:
        queue = self.queue1 if len(self.queue1) > 0 else self.queue2
        queue_backup = self.queue1 if len(self.queue2) > 0 else self.queue2
        while len(queue) > 1:
            queue_backup.append(queue.popleft())
        val = queue[0]
        queue_backup.append(queue.popleft())
        return val

    def empty(self) -> bool:
        queue = self.queue1 if len(self.queue1) > 0 else self.queue2
        return queue


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
print(obj.top())
print(obj.pop())
print(obj.empty())