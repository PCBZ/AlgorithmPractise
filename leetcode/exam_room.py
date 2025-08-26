"""
LeetCode Problem #855: Exam Room

URL: https://leetcode.com/problems/exam-room/

Design an exam room that simulates student seating. Students are seated
to maximize the distance to the closest student.
"""


class ExamRoom:
    """
    Design an exam room where students are seated to maximize distance.

    In an exam room, there are n seats in a single row numbered 0 to n-1.
    When a student enters the room, they must sit in the seat that maximizes
    the distance to the closest person.
    """

    def __init__(self, n: int):
        """
        Initialize the exam room.
        
        Args:
            n: Number of seats in the room (0 to n-1)
        """
        self.seats = []
        self.room_size = n

    def seat(self) -> int:
        """
        Seat a student to maximize distance to closest person.

        Returns:
            The seat number where the student is seated
        """
        if not self.seats:
            self.seats.insert(0, 0)
            return 0

        start = -1
        longest = 0
        seat_index, insert_index = -1, -1

        for i, end in enumerate(self.seats):
            candidate = start + 1 if start == -1 else (start + end) // 2
            dist = end - candidate if start == -1 else candidate - start
            if dist > longest:
                longest = dist
                insert_index = i
                seat_index = candidate
            start = end

        end = self.room_size
        candidate = end - 1
        if candidate - start > longest:
            longest = candidate - start
            insert_index = len(self.seats)
            seat_index = candidate

        self.seats.insert(insert_index, seat_index)
        return seat_index

    def leave(self, seat_position: int) -> None:
        """
        Remove a student from the specified seat.

        Args:
            seat_position: The seat number to vacate
        """
        self.seats.remove(seat_position)


if __name__ == "__main__":
    # Example usage of the ExamRoom class
    room_size = 10
    exam_room = ExamRoom(room_size)
    print(exam_room.seat())
    print(exam_room.seat())
    print(exam_room.seat())
    exam_room.leave(0)
    exam_room.leave(4)
    print(exam_room.seat())
    print(exam_room.seat())
    print(exam_room.seat())
    print(exam_room.seat())
    print(exam_room.seat())
    print(exam_room.seat())
    print(exam_room.seat())
    print(exam_room.seat())
    print(exam_room.seat())
    exam_room.leave(0)
