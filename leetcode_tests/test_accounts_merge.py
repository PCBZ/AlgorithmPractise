"""
Unit tests for Accounts_Merge.py
Tests the Union Find solution for merging accounts with common emails.
"""

import sys
import importlib.util
import pytest

# Import the solution using importlib
spec = importlib.util.spec_from_file_location(
    "accounts_merge",
    "/Users/wenshuangzhou/Developer/AlgorithmPractise/leetcode/accounts_merge.py"
)
accounts_merge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(accounts_merge)

Solution = accounts_merge.Solution


class TestAccountsMerge:
    """Test class for accounts merge functionality."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_merge(self):
        """Test basic account merging with common emails."""
        accounts = [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"]
        ]
        result = self.solution.accountsMerge(accounts)
        
        # Sort result for consistent comparison
        result = sorted(result, key=lambda x: (x[0], x[1]))
        
        expected = [
            ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
            ['John', 'johnnybravo@mail.com'],
            ['Mary', 'mary@mail.com']
        ]
        expected = sorted(expected, key=lambda x: (x[0], x[1]))
        
        assert result == expected

    def test_single_account(self):
        """Test with single account."""
        accounts = [["John", "john@email.com"]]
        result = self.solution.accountsMerge(accounts)
        expected = [["John", "john@email.com"]]
        assert result == expected

    def test_no_merge_needed(self):
        """Test accounts with no common emails."""
        accounts = [
            ["John", "john1@email.com"],
            ["John", "john2@email.com"],
            ["Mary", "mary@email.com"]
        ]
        result = self.solution.accountsMerge(accounts)
        
        # Sort result for consistent comparison
        result = sorted(result, key=lambda x: (x[0], x[1]))
        
        expected = [
            ["John", "john1@email.com"],
            ["John", "john2@email.com"],
            ["Mary", "mary@email.com"]
        ]
        expected = sorted(expected, key=lambda x: (x[0], x[1]))
        
        assert result == expected

    def test_multiple_emails_single_account(self):
        """Test single account with multiple emails."""
        accounts = [["John", "john1@email.com", "john2@email.com", "john3@email.com"]]
        result = self.solution.accountsMerge(accounts)
        expected = [["John", "john1@email.com", "john2@email.com", "john3@email.com"]]
        assert result == expected

    def test_chain_merge(self):
        """Test chain merging through common emails."""
        accounts = [
            ["John", "john1@email.com", "john2@email.com"],
            ["John", "john2@email.com", "john3@email.com"],
            ["John", "john3@email.com", "john4@email.com"]
        ]
        result = self.solution.accountsMerge(accounts)
        expected = [["John", "john1@email.com", "john2@email.com", "john3@email.com", "john4@email.com"]]
        assert result == expected

    def test_different_names_same_email(self):
        """Test that accounts with different names but same email stay separate."""
        accounts = [
            ["John", "shared@email.com"],
            ["Jane", "shared@email.com"]
        ]
        result = self.solution.accountsMerge(accounts)
        
        # Sort result for consistent comparison
        result = sorted(result, key=lambda x: x[0])
        
        expected = [
            ["Jane", "shared@email.com"],
            ["John", "shared@email.com"]
        ]
        
        assert result == expected

    def test_complex_merge_scenario(self):
        """Test complex merging scenario with multiple interconnected accounts."""
        accounts = [
            ["David", "david.lee.lg@gmail.com"],
            ["David", "david.lee.lg@gmail.com", "david@email.com"],
            ["David", "david@email.com", "david.work@company.com"],
            ["David", "david.personal@gmail.com"]
        ]
        result = self.solution.accountsMerge(accounts)
        
        # Should merge first three accounts, keep last one separate
        assert len(result) == 2
        
        # Find the merged account
        merged_account = None
        single_account = None
        for account in result:
            if len(account) > 2:  # More than just name and one email
                merged_account = account
            else:
                single_account = account
        
        assert merged_account is not None
        assert single_account is not None
        assert merged_account[0] == "David"
        assert single_account == ["David", "david.personal@gmail.com"]
        
        # Check that merged account contains all expected emails
        expected_emails = ["david.lee.lg@gmail.com", "david@email.com", "david.work@company.com"]
        assert sorted(merged_account[1:]) == sorted(expected_emails)

    def test_empty_accounts(self):
        """Test with empty accounts list."""
        accounts = []
        result = self.solution.accountsMerge(accounts)
        assert result == []

    def test_account_with_single_email(self):
        """Test accounts that each have only one email."""
        accounts = [
            ["Alice", "alice@email.com"],
            ["Bob", "bob@email.com"],
            ["Charlie", "charlie@email.com"]
        ]
        result = self.solution.accountsMerge(accounts)
        
        # Sort result for consistent comparison
        result = sorted(result, key=lambda x: x[0])
        
        expected = [
            ["Alice", "alice@email.com"],
            ["Bob", "bob@email.com"],
            ["Charlie", "charlie@email.com"]
        ]
        
        assert result == expected

    def test_large_merge_group(self):
        """Test merging a large group of accounts."""
        accounts = [
            ["User", "email1@test.com", "email2@test.com"],
            ["User", "email2@test.com", "email3@test.com"],
            ["User", "email3@test.com", "email4@test.com"],
            ["User", "email4@test.com", "email5@test.com"],
            ["User", "email5@test.com", "email6@test.com"]
        ]
        result = self.solution.accountsMerge(accounts)
        
        assert len(result) == 1
        assert result[0][0] == "User"
        expected_emails = ["email1@test.com", "email2@test.com", "email3@test.com", 
                          "email4@test.com", "email5@test.com", "email6@test.com"]
        assert sorted(result[0][1:]) == sorted(expected_emails)

    def test_duplicate_emails_same_account(self):
        """Test account with duplicate emails (should be handled gracefully)."""
        accounts = [
            ["John", "john@email.com", "john@email.com", "john2@email.com"]
        ]
        result = self.solution.accountsMerge(accounts)
        
        # Should handle duplicates and keep unique emails
        assert len(result) == 1
        assert result[0][0] == "John"
        # Check that emails are unique and sorted
        emails = result[0][1:]
        assert emails == sorted(list(set(emails)))


if __name__ == "__main__":
    pytest.main([__file__])
