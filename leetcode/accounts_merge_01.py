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
        # Union Find data structure
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

        # Map email to name
        email_to_name = {}

        # Process each account
        for account in accounts:
            name = account[0]
            emails = account[1:]

            # Map each email to the name
            for email in emails:
                email_to_name[email] = name

            # Union all emails in the same account
            if len(emails) > 1:
                for i in range(1, len(emails)):
                    union(emails[0], emails[i])

        # Group emails by their root parent
        groups = defaultdict(list)
        for email in email_to_name:
            root = find(email)
            groups[root].append(email)

        # Build result
        result = []
        for emails in groups.values():
            name = email_to_name[emails[0]]
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
