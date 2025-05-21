class ExamRoom:

    def __init__(self, n: int):
        self.seats = []
        self.n = n

    def seat(self) -> int:
        if not self.seats:
            self.seats.insert(0, 0)
            return 0

        start = -1
        longest = 0
        idx, insert_idx = -1, -1
        for i in range(len(self.seats)):
            end = self.seats[i]
            candidate = start + 1 if start == -1 else (start + end) // 2
            dist = end - candidate if start == -1 else candidate - start
            if dist > longest:
                longest = dist
                insert_idx = i
                idx = candidate
            start = end
        end = self.n
        candidate = end - 1
        if candidate - start > longest:
            longest = candidate - start
            insert_idx = len(self.seats)
            idx = candidate
        start = end
        
        self.seats.insert(insert_idx, idx)
        return idx

    def leave(self, p: int) -> None:
        self.seats.remove(p)
        

if __name__ == "__main__":
    n = 10
    obj = ExamRoom(n)
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    obj.leave(0)
    obj.leave(4)
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    print(obj.seat())
    obj.leave(0)
