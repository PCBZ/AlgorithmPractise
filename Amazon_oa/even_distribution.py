from typing import List

class Solution:
    def minimum_step_even_distribution(self, parcels: List[int]) -> int:
        total = sum(parcels)
        lower = total // len(parcels)
        upper = lower + 1
        high_move = low_move = 0
        for parcel in parcels:
            if parcel > upper:
                high_move += parcel - upper
            elif parcel < lower:
                low_move += lower - parcel
        return max(low_move, high_move)


if __name__ == "__main__":
    parcels = [5, 5, 8, 7]
    print(Solution().minimum_step_even_distribution(parcels))