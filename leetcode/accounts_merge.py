"""
Accounts Merge - Union Find Solution
Source: https://leetcode.com/problems/accounts-merge/description/
"""

from typing import List
from collections import defaultdict

class Solution:
    """
    Solution class for the Accounts Merge problem.
    Uses Union Find (Disjoint Set Union) to merge accounts with common emails.
    """

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Merge accounts that share at least one common email.

        Args:
            accounts: List of accounts, each containing name and emails

        Returns:
            List of merged accounts with sorted emails
        """
        def union_find_operations():
            """Helper function to create Union Find operations."""
            parent = {}

            def find(x):
                if x not in parent:
                    parent[x] = x
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                px, py = find(x), find(y)
                if px != py:
                    parent[px] = py

            return find, union

        # Group accounts by name first
        name_to_accounts = defaultdict(list)
        for i, account in enumerate(accounts):
            name_to_accounts[account[0]].append(i)

        result = []

        # Process each group of accounts with the same name
        for name, account_indices in name_to_accounts.items():
            find, union = union_find_operations()
            email_set = set()

            # Process accounts for this name
            for idx in account_indices:
                emails = accounts[idx][1:]
                email_set.update(emails)

                # Union all emails in the same account
                if len(emails) > 1:
                    for i in range(1, len(emails)):
                        union(emails[0], emails[i])

            # Group emails by their root parent for this name
            groups = defaultdict(list)
            for email in email_set:
                groups[find(email)].append(email)

            # Build result for this name
            for emails in groups.values():
                result.append([name] + sorted(emails))

        return result


if __name__ == "__main__":
    test_accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"]
    ]
    print(Solution().accountsMerge(test_accounts))
