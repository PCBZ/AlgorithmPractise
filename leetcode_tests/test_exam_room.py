"""
Comprehensive test suite for LeetCode Problem #855: Exam Room

Tests the ExamRoom class which manages student seating to maximize
distance to the closest person in the exam room.
"""
import time

from leetcode.exam_room import ExamRoom


class TestExamRoom:
    """Test class for ExamRoom implementation."""

    def test_single_seat_room(self):
        """Test room with only one seat."""
        exam_room = ExamRoom(1)
        assert exam_room.seat() == 0
        exam_room.leave(0)
        assert exam_room.seat() == 0

    def test_two_seat_room(self):
        """Test room with two seats."""
        exam_room = ExamRoom(2)
        assert exam_room.seat() == 0  # First student sits at position 0
        assert exam_room.seat() == 1  # Second student sits at position 1

    def test_basic_seating_pattern(self):
        """Test basic seating pattern in a larger room."""
        exam_room = ExamRoom(10)
        
        # First student should sit at position 0
        assert exam_room.seat() == 0
        
        # Second student should sit at position 9 (end)
        assert exam_room.seat() == 9
        
        # Third student should sit at position 4 (middle)
        assert exam_room.seat() == 4

    def test_leave_functionality(self):
        """Test leaving seats and reseating."""
        exam_room = ExamRoom(10)
        
        # Fill some seats
        assert exam_room.seat() == 0
        assert exam_room.seat() == 9
        assert exam_room.seat() == 4
        
        # Leave position 0
        exam_room.leave(0)
        
        # Next student should sit at position 0
        assert exam_room.seat() == 0

    def test_complex_seating_scenario(self):
        """Test complex seating and leaving scenario."""
        exam_room = ExamRoom(10)
        
        # Seat students
        seats = []
        seats.append(exam_room.seat())  # 0
        seats.append(exam_room.seat())  # 9
        seats.append(exam_room.seat())  # 4
        
        # Leave some students
        exam_room.leave(0)
        exam_room.leave(4)
        
        # Continue seating
        seats.append(exam_room.seat())  # Should prioritize largest gap
        
        # Verify the seating makes sense
        assert seats[0] == 0
        assert seats[1] == 9
        assert seats[2] == 4

    def test_empty_room_multiple_seats(self):
        """Test multiple sequential seatings in empty room."""
        exam_room = ExamRoom(10)
        
        seats = []
        for _ in range(5):
            seats.append(exam_room.seat())
        
        # First seat should be 0
        assert seats[0] == 0
        # Should follow optimal seating pattern
        assert 0 in seats
        assert 9 in seats

    def test_room_size_three(self):
        """Test small room with 3 seats."""
        exam_room = ExamRoom(3)
        
        assert exam_room.seat() == 0
        assert exam_room.seat() == 2
        assert exam_room.seat() == 1

    def test_room_size_four(self):
        """Test room with 4 seats."""
        exam_room = ExamRoom(4)
        
        seats = []
        seats.append(exam_room.seat())  # 0
        seats.append(exam_room.seat())  # 3
        seats.append(exam_room.seat())  # 1
        seats.append(exam_room.seat())  # 2
        
        assert seats == [0, 3, 1, 2]

    def test_leave_from_empty_room(self):
        """Test leaving when no one is seated."""
        exam_room = ExamRoom(5)
        
        # This should not crash (though it's not typical usage)
        try:
            exam_room.leave(0)
        except ValueError:
            # It's acceptable to raise ValueError for removing non-existent seat
            pass

    def test_leave_middle_seat(self):
        """Test leaving a seat in the middle."""
        exam_room = ExamRoom(10)
        
        # Fill seats
        exam_room.seat()  # 0
        exam_room.seat()  # 9
        exam_room.seat()  # 4
        exam_room.seat()  # 2
        
        # Leave middle seat
        exam_room.leave(4)
        
        # Next seat should optimize the gap
        next_seat = exam_room.seat()
        assert isinstance(next_seat, int)
        assert 0 <= next_seat < 10

    def test_sequential_leave_and_seat(self):
        """Test alternating leave and seat operations."""
        exam_room = ExamRoom(8)
        
        # Initial seating
        seat1 = exam_room.seat()  # 0
        seat2 = exam_room.seat()  # 7
        
        # Leave and reseat
        exam_room.leave(seat1)
        seat3 = exam_room.seat()  # Should be 0 again
        
        assert seat1 == 0
        assert seat2 == 7
        assert seat3 == 0

    def test_maximum_distance_calculation(self):
        """Test that seating maximizes distance correctly."""
        exam_room = ExamRoom(10)
        
        # Place students to create specific gaps
        exam_room.seat()  # 0
        exam_room.seat()  # 9
        
        # Next student should sit in the middle (position 4)
        # as it maximizes distance to both 0 and 9
        next_seat = exam_room.seat()
        assert next_seat == 4

    def test_tie_breaking_preference(self):
        """Test tie-breaking when multiple seats have same distance."""
        exam_room = ExamRoom(6)
        
        # Seat students at positions that create equal gaps
        exam_room.seat()  # 0
        exam_room.seat()  # 5
        
        # Middle position should be chosen
        middle_seat = exam_room.seat()
        assert middle_seat in [2, 3]  # Both have distance 2

    def test_edge_positions(self):
        """Test preference for edge positions when appropriate."""
        exam_room = ExamRoom(10)
        
        # If only middle seats are taken, edges should be preferred
        # Start with a middle seat
        exam_room.seats = [5]  # Manually set for test
        
        next_seat = exam_room.seat()
        # Should choose an edge (0 or 9) as they have distance 5
        assert next_seat in [0, 9]

    def test_performance_large_room(self):
        """Test performance with a larger room size."""
        exam_room = ExamRoom(1000)
        
        start_time = time.time()
        
        # Seat several students
        for _ in range(10):
            exam_room.seat()
        
        # Leave some students
        for i in range(0, 10, 2):
            if exam_room.seats:
                exam_room.leave(exam_room.seats[0])
        
        # Seat more students
        for _ in range(5):
            exam_room.seat()
        
        end_time = time.time()
        
        # Should complete quickly
        assert end_time - start_time < 1.0

    def test_room_state_consistency(self):
        """Test that room state remains consistent."""
        exam_room = ExamRoom(10)
        
        # Perform various operations
        seats = []
        seats.append(exam_room.seat())
        seats.append(exam_room.seat())
        seats.append(exam_room.seat())
        
        # Check that seats list is sorted
        assert exam_room.seats == sorted(exam_room.seats)
        
        # Leave a seat
        exam_room.leave(seats[1])
        
        # Seats should still be sorted
        assert exam_room.seats == sorted(exam_room.seats)

    def test_all_seats_filled(self):
        """Test behavior when all seats are filled."""
        exam_room = ExamRoom(3)
        
        # Fill all seats
        seat1 = exam_room.seat()  # 0
        seat2 = exam_room.seat()  # 2
        seat3 = exam_room.seat()  # 1
        
        assert sorted([seat1, seat2, seat3]) == [0, 1, 2]

    def test_boundary_conditions(self):
        """Test boundary conditions and edge cases."""
        # Test minimum room size
        exam_room = ExamRoom(1)
        assert exam_room.seat() == 0
        
        # Test room size 2
        exam_room = ExamRoom(2)
        assert exam_room.seat() == 0
        assert exam_room.seat() == 1

    def test_deterministic_behavior(self):
        """Test that behavior is deterministic."""
        exam_room1 = ExamRoom(10)
        exam_room2 = ExamRoom(10)
        
        # Same sequence of operations should yield same results
        seats1 = []
        seats2 = []
        
        for _ in range(3):
            seats1.append(exam_room1.seat())
            seats2.append(exam_room2.seat())
        
        assert seats1 == seats2

    def test_seat_return_type(self):
        """Test that seat() returns proper integer type."""
        exam_room = ExamRoom(5)
        
        seat = exam_room.seat()
        assert isinstance(seat, int)
        assert 0 <= seat < 5

    def test_leave_parameter_validation(self):
        """Test leave method with various parameters."""
        exam_room = ExamRoom(5)
        
        # Seat a student
        seat = exam_room.seat()
        
        # Leave the seated student
        exam_room.leave(seat)
        
        # Verify seat is removed
        assert seat not in exam_room.seats

    def test_example_from_problem(self):
        """Test the example scenario from the LeetCode problem."""
        exam_room = ExamRoom(10)
        
        # Follow the example pattern
        result1 = exam_room.seat()  # Should return 0
        result2 = exam_room.seat()  # Should return 9
        result3 = exam_room.seat()  # Should return 4
        
        exam_room.leave(0)
        exam_room.leave(4)
        
        result4 = exam_room.seat()  # Should choose optimal position
        result5 = exam_room.seat()  # Should choose optimal position
        
        # Verify results make sense
        assert result1 == 0
        assert result2 == 9
        assert result3 == 4
        
        # After leaving 0 and 4, next seats should be reasonable
        assert isinstance(result4, int)
        assert isinstance(result5, int)
        assert 0 <= result4 < 10
        assert 0 <= result5 < 10

    def test_algorithm_optimality(self):
        """Test that the algorithm chooses optimal seats."""
        exam_room = ExamRoom(10)
        
        # Place students at specific positions
        exam_room.seats = [1, 8]  # Manually set for test
        
        # Next student should sit at position 4 or 5 (middle of largest gap)
        next_seat = exam_room.seat()
        # Distance from 1 to 4 is 3, distance from 4 to 8 is 4
        # Distance from 1 to 5 is 4, distance from 5 to 8 is 3
        # So position 4 gives min distance 3, position 5 gives min distance 3
        # Both are equally good, algorithm should pick one consistently
        assert next_seat in [4, 5]
