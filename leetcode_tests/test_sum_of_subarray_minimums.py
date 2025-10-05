import pytest
from leetcode.sum_of_subarray_minimums import Solution

class TestSumSubarrayMinimums:
    def test_leetcode_examples(self):
        """Test official LeetCode examples."""
        sol = Solution()
        
        # Example 1: [3,1,2,4] -> 17
        # Subarrays: [3]=3, [1]=1, [2]=2, [4]=4, [3,1]=1, [1,2]=1, [2,4]=2, 
        #           [3,1,2]=1, [1,2,4]=1, [3,1,2,4]=1
        # Sum: 3+1+2+4+1+1+2+1+1+1 = 17
        assert sol.sumSubarrayMins([3, 1, 2, 4]) == 17
        
        # Example 2: [11,81,94,43,3] -> 444
        assert sol.sumSubarrayMins([11, 81, 94, 43, 3]) == 444
    
    def test_single_element(self):
        """Test arrays with single element."""
        sol = Solution()
        assert sol.sumSubarrayMins([1]) == 1
        assert sol.sumSubarrayMins([42]) == 42
        assert sol.sumSubarrayMins([100]) == 100
    
    def test_two_elements(self):
        """Test arrays with two elements."""
        sol = Solution()
        assert sol.sumSubarrayMins([1, 2]) == 4  # [1]=1, [2]=2, [1,2]=1 -> 1+2+1=4
        assert sol.sumSubarrayMins([2, 1]) == 4  # [2]=2, [1]=1, [2,1]=1 -> 2+1+1=4
        assert sol.sumSubarrayMins([5, 5]) == 15 # [5]=5, [5]=5, [5,5]=5 -> 5+5+5=15
    
    def test_sorted_arrays(self):
        """Test sorted arrays (ascending and descending)."""
        sol = Solution()
        
        # Ascending: [1,2,3,4,5] -> 35
        # Each element contributes differently based on position
        assert sol.sumSubarrayMins([1, 2, 3, 4, 5]) == 35
        
        # Descending: [5,4,3,2,1] -> 35  
        # Same total but different distribution
        assert sol.sumSubarrayMins([5, 4, 3, 2, 1]) == 35
    
    def test_duplicate_elements(self):
        """Test arrays with duplicate elements."""
        sol = Solution()
        assert sol.sumSubarrayMins([1, 1, 1]) == 6   # All minimums are 1
        assert sol.sumSubarrayMins([2, 2, 2, 2]) == 20  # All minimums are 2
        assert sol.sumSubarrayMins([3, 1, 3, 1, 3]) == 21
    
    def test_edge_cases(self):
        """Test various edge cases."""
        sol = Solution()
        
        # Array where minimum is at start
        assert sol.sumSubarrayMins([1, 5, 3, 4]) == 25
        
        # Array where minimum is at end  
        assert sol.sumSubarrayMins([5, 3, 4, 1]) == 25
        
        # Array where minimum is in middle
        assert sol.sumSubarrayMins([3, 4, 1, 5]) == 21
    
    def test_large_values(self):
        """Test with large values that require modulo operation."""
        sol = Solution()
        MOD = 10**9 + 7
        
        # Large array with large values
        large_arr = [1000000] * 100
        result = sol.sumSubarrayMins(large_arr)
        
        # Manual calculation: n*(n+1)/2 * min_val % MOD
        n = 100
        expected = (n * (n + 1) // 2 * 1000000) % MOD
        assert result == expected
    
    def test_performance_large_array(self):
        """Test performance with larger arrays."""
        sol = Solution()
        
        # Array of size 1000 with alternating pattern
        arr = [i % 2 + 1 for i in range(1000)]  # [1,2,1,2,1,2,...]
        result = sol.sumSubarrayMins(arr)
        assert isinstance(result, int)
        assert 0 <= result < 10**9 + 7
    
    def test_mountain_array(self):
        """Test mountain-like arrays."""
        sol = Solution()
        
        # Mountain: increases then decreases
        mountain = [1, 2, 3, 4, 3, 2, 1]
        result = sol.sumSubarrayMins(mountain)
        assert result == 50
        
        # Valley: decreases then increases  
        valley = [4, 3, 2, 1, 2, 3, 4]
        result = sol.sumSubarrayMins(valley)
        assert result == 48
    
    def test_modulo_correctness(self):
        """Test that modulo operation is applied correctly."""
        sol = Solution()
        
        # Create scenario that might overflow without modulo
        arr = [1] * 500  # Large array of same elements
        result = sol.sumSubarrayMins(arr)
        
        # Result should be within modulo range
        assert 0 <= result < 10**9 + 7
        
        # Manual verification for smaller case
        small_arr = [1] * 10
        small_result = sol.sumSubarrayMins(small_arr)
        # For n identical elements with value v: v * n*(n+1)/2
        expected = 1 * 10 * 11 // 2
        assert small_result == expected