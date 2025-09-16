"""
Test suite for LeetCode 640: Solve the Equation

Covers edge cases and typical equations for robust validation.
"""

import unittest
from leetcode.solve_the_equation import Solution

class TestSolveTheEquation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic(self):
        self.assertEqual(self.solution.solveEquation("x+5-3+x=6+x-2"), "x=2")

    def test_infinite(self):
        self.assertEqual(self.solution.solveEquation("x=x"), "Infinite solutions")

    def test_no_solution(self):
        self.assertEqual(self.solution.solveEquation("x=x+2"), "No solution")

    def test_simple(self):
        self.assertEqual(self.solution.solveEquation("2x=x"), "x=0")

    def test_negative(self):
        self.assertEqual(self.solution.solveEquation("2x+3x-6x=x+2"), "x=-1")

    def test_constants(self):
        self.assertEqual(self.solution.solveEquation("1+1=x"), "x=2")

    def test_commutative(self):
        self.assertEqual(self.solution.solveEquation("x+2=2+x"), "Infinite solutions")

    def test_zero(self):
        self.assertEqual(self.solution.solveEquation("0=0"), "Infinite solutions")

    def test_x_only(self):
        self.assertEqual(self.solution.solveEquation("x=0"), "x=0")
        self.assertEqual(self.solution.solveEquation("0=x"), "x=0")

    def test_negative_x(self):
        self.assertEqual(self.solution.solveEquation("-x=1"), "x=-1")
        self.assertEqual(self.solution.solveEquation("x=-1"), "x=-1")

    def test_multiple_x(self):
        self.assertEqual(self.solution.solveEquation("2x+3=3x+2"), "x=1")
        self.assertEqual(self.solution.solveEquation("4x+2=2x+10"), "x=4")

if __name__ == "__main__":
    unittest.main()
