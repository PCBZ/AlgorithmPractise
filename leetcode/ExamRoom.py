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
            if start == -1:
                mid = start + 1
            else:
                mid = (start + end) // 2
            dist = end - mid if start == -1 else mid - start
            if dist > longest:
                longest = dist
                insert_idx = i
                idx = mid
            start = end
        end = self.n
        mid = end - 1
        if mid - start > longest:
            longest = mid - start
            insert_idx = len(self.seats)
            idx = mid
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
