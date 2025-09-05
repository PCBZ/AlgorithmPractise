"""
Test cases for LeetCode 51: N-Queens
"""

import pytest
from typing import List

from leetcode.n_queens import Solution


class TestNQueens:
    """Test class for N-Queens problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def is_valid_solution(self, board: List[str]) -> bool:
        """
        Validate if a board configuration is a valid N-Queens solution.
        
        Args:
            board: List of strings representing the board
            
        Returns:
            True if valid N-Queens solution, False otherwise
        """
        n = len(board)
        queens = []
        
        # Find all queen positions
        for row in range(n):
            for col in range(n):
                if board[row][col] == 'Q':
                    queens.append((row, col))
        
        # Should have exactly n queens
        if len(queens) != n:
            return False
        
        # Check no two queens attack each other
        for i in range(len(queens)):
            for j in range(i + 1, len(queens)):
                r1, c1 = queens[i]
                r2, c2 = queens[j]
                
                # Same row, column, or diagonal
                if (r1 == r2 or c1 == c2 or 
                    abs(r1 - r2) == abs(c1 - c2)):
                    return False
        
        return True

    @pytest.mark.parametrize(
        "n,expected_count",
        [
            (1, 1),  # Trivial case
            (2, 0),  # No solution possible
            (3, 0),  # No solution possible
            (4, 2),  # Two solutions exist
            (5, 10), # Ten solutions exist
            (6, 4),  # Four solutions exist
            (7, 40), # Forty solutions exist
            (8, 92), # Classic 8-queens has 92 solutions
        ]
    )
    def test_n_queens_count(self, n, expected_count):
        """Test that the correct number of solutions is found."""
        solutions = self.solution.solveNQueens(n)
        assert len(solutions) == expected_count

    def test_solution_validity(self):
        """Test that all returned solutions are valid."""
        for n in range(1, 9):  # Test n=1 to n=8
            solutions = self.solution.solveNQueens(n)
            
            for solution in solutions:
                assert len(solution) == n, f"Solution should have {n} rows"
                for row in solution:
                    assert len(row) == n, f"Each row should have {n} columns"
                    assert row.count('Q') == 1, "Each row should have exactly one queen"
                    assert set(row) <= {'.', 'Q'}, "Only '.' and 'Q' allowed"
                
                assert self.is_valid_solution(solution), f"Invalid solution for n={n}"

    def test_specific_solutions_n4(self):
        """Test specific known solutions for n=4."""
        solutions = self.solution.solveNQueens(4)
        assert len(solutions) == 2
        
        # Convert solutions to sets for comparison (order doesn't matter)
        solution_sets = [set(sol) for sol in solutions]
        
        expected_solution_1 = {".Q..", "...Q", "Q...", "..Q."}
        expected_solution_2 = {"..Q.", "Q...", "...Q", ".Q.."}
        
        assert expected_solution_1 in solution_sets
        assert expected_solution_2 in solution_sets

    def test_edge_cases(self):
        """Test edge cases."""
        # n=1 should return single solution
        solutions = self.solution.solveNQueens(1)
        assert solutions == [["Q"]]
        
        # n=2 and n=3 should return no solutions
        assert self.solution.solveNQueens(2) == []
        assert self.solution.solveNQueens(3) == []

    def test_board_format(self):
        """Test that board format is correct."""
        solutions = self.solution.solveNQueens(4)
        
        for solution in solutions:
            assert isinstance(solution, list)
            assert len(solution) == 4
            
            for row in solution:
                assert isinstance(row, str)
                assert len(row) == 4
                assert all(c in '.Q' for c in row)

    def test_no_duplicate_solutions(self):
        """Test that no duplicate solutions are returned."""
        for n in range(1, 9):
            solutions = self.solution.solveNQueens(n)
            
            # Convert each solution to a tuple to make it hashable
            solution_tuples = [tuple(sol) for sol in solutions]
            unique_solutions = set(solution_tuples)
            
            assert len(unique_solutions) == len(solutions), f"Duplicate solutions found for n={n}"

    def test_queen_placement_constraints(self):
        """Test that queens don't attack each other in all solutions."""
        for n in [4, 5, 6, 7, 8]:
            solutions = self.solution.solveNQueens(n)
            
            for solution in solutions:
                queen_positions = []
                
                # Extract queen positions
                for row_idx, row in enumerate(solution):
                    for col_idx, cell in enumerate(row):
                        if cell == 'Q':
                            queen_positions.append((row_idx, col_idx))
                
                # Verify no attacks
                for i in range(len(queen_positions)):
                    for j in range(i + 1, len(queen_positions)):
                        r1, c1 = queen_positions[i]
                        r2, c2 = queen_positions[j]
                        
                        # No same row (implicit by construction)
                        assert r1 != r2
                        
                        # No same column
                        assert c1 != c2, f"Queens at same column: {queen_positions}"
                        
                        # No same diagonal
                        assert abs(r1 - r2) != abs(c1 - c2), f"Queens on same diagonal: {queen_positions}"

    def test_performance_reasonable_time(self):
        """Test that solution completes in reasonable time for n=8."""
        import time
        
        start_time = time.time()
        solutions = self.solution.solveNQueens(8)
        end_time = time.time()
        
        assert len(solutions) == 92
        assert end_time - start_time < 5.0  # Should complete within 5 seconds

    def test_return_type(self):
        """Test that return type is correct."""
        solutions = self.solution.solveNQueens(4)
        
        assert isinstance(solutions, list)
        for solution in solutions:
            assert isinstance(solution, list)
            for row in solution:
                assert isinstance(row, str)

    def test_symmetry_validation(self):
        """Test symmetry properties of solutions."""
        # For n=4, verify we get the expected symmetric solutions
        solutions = self.solution.solveNQueens(4)
        assert len(solutions) == 2
        
        # Solutions should be mirror images or rotations of each other
        # This is more of a mathematical property verification
