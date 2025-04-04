from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_map = {}
        for item in accounts:
            name, emails = item[0], set(item[1:])
            if name not in account_map:
                account_map[name] = []
                account_map[name].append(emails)
            else:
                exist = False
                for account in account_map[name]:
                    for email in emails:
                        if email in account:
                            print(account)
                            exist = True
                            break
                    if exist:
                        break
                if not exist:
                    account_map[name].append(emails)
        print(account_map)

if __name__ == "__main__":
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    print(Solution().accountsMerge(accounts))