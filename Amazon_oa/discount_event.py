from typing import List

class Solution:
    def find_final_price(self, prices: List[int], queries: List[List[int]]) -> List[int]:
        for query in queries:
            if query[0] == 1:
                prices[query[1]] = query[2]
            elif query[0] == 2:
                for i, price in enumerate(prices):
                    if price < query[1]:
                        prices[i] = query[1]
        return prices


if __name__ == "__main__":
    price = [7, 5, 4]
    queries = [[2, 6, 6], [1, 2, 9], [2, 8, 8]]
    print(Solution().find_final_price(price, queries))