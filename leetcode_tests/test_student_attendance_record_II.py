"""
Test cases for Student Attendance Record II problem.
"""

import pytest
from leetcode.student_attendance_record_II import Solution


class TestStudentAttendanceRecordII:
    """Test class for Student Attendance Record II solution."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    def test_base_case_n_1(self):
        """Test base case with n=1."""
        # For n=1: P, A, L are all valid -> 3 records
        assert self.solution.checkRecord(1) == 3
    
    def test_small_case_n_2(self):
        """Test small case with n=2."""
        # For n=2: PP, PA, PL, AP, AL, LP, LA, LL -> 8 records
        # Invalid: AA (2 absences), LLL not possible for n=2
        assert self.solution.checkRecord(2) == 8
    
    def test_medium_case_n_3(self):
        """Test medium case with n=3."""
        # More complex combinations, but must exclude:
        # - Any with 2+ absences (AA*)
        # - Any with 3+ consecutive late (LLL)
        result = self.solution.checkRecord(3)
        assert result == 19  # Known result for n=3
    
    def test_larger_case_n_4(self):
        """Test larger case with n=4."""
        result = self.solution.checkRecord(4)
        assert result == 43  # Known result for n=4
    
    def test_even_larger_case_n_5(self):
        """Test even larger case with n=5."""
        result = self.solution.checkRecord(5)
        assert result == 94  # Known result for n=5
    
    def test_constraint_no_three_consecutive_late(self):
        """Test that sequences with 3+ consecutive late days are invalid."""
        # For n=3, LLL should not be counted
        # We can't directly test this but can verify total count is correct
        assert self.solution.checkRecord(3) == 19
    
    def test_constraint_max_one_absence(self):
        """Test that sequences with 2+ absences are invalid."""
        # For n=2, AA should not be counted  
        # We can't directly test this but can verify total count is correct
        assert self.solution.checkRecord(2) == 8
    
    def test_modular_arithmetic(self):
        """Test that the result is returned modulo 10^9 + 7."""
        # For reasonable n values, result should be less than MOD
        result = self.solution.checkRecord(10)
        MOD = 10**9 + 7
        assert 0 <= result < MOD
    
    def test_larger_values(self):
        """Test with larger values to ensure performance."""
        # Test n=10 (should complete quickly with DP)
        result = self.solution.checkRecord(10)
        assert result > 0
        
        # Test n=20 
        result = self.solution.checkRecord(20)
        assert result > 0
    
    @pytest.mark.parametrize("days,expected", [
        (1, 3),
        (2, 8),
        (3, 19),
        (4, 43),
        (5, 94),
    ])
    def test_parametrized_cases(self, days, expected):
        """Parametrized test for multiple input-output pairs."""
        assert self.solution.checkRecord(days) == expected
    
    def test_edge_case_large_n(self):
        """Test with a larger n to verify algorithm efficiency."""
        # Test n=50 to ensure the DP approach is efficient
        result = self.solution.checkRecord(50)
        assert result > 0
        assert isinstance(result, int)
    
    def test_return_type(self):
        """Test that the function returns an integer."""
        result = self.solution.checkRecord(5)
        assert isinstance(result, int)
    
    def test_positive_result(self):
        """Test that the result is always positive for valid inputs."""
        for n in range(1, 11):
            result = self.solution.checkRecord(n)
            assert result > 0
    
    def test_increasing_trend(self):
        """Test that result generally increases with larger n."""
        results = []
        for n in range(1, 6):
            results.append(self.solution.checkRecord(n))
        
        # Results should be generally increasing (more days = more possibilities)
        for i in range(1, len(results)):
            assert results[i] > results[i-1]
    
    def test_algorithm_correctness_manual_verification(self):
        """Manual verification for small cases."""
        # For n=1: P, A, L (all valid) = 3
        assert self.solution.checkRecord(1) == 3
        
        # For n=2: 
        # Valid: PP, PA, PL, AP, AL, LP, LA, LL = 8
        # Invalid: AA (2 absences) = 1
        # Total possible: 3^2 = 9, Valid: 8
        assert self.solution.checkRecord(2) == 8
    
    def test_boundary_conditions(self):
        """Test boundary conditions of the constraints."""
        # The algorithm should handle edge cases properly
        result = self.solution.checkRecord(1)
        assert result == 3
        
        # Test that modular arithmetic works
        MOD = 10**9 + 7
        result = self.solution.checkRecord(100)
        assert 0 <= result < MOD


if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__, "-v"])
