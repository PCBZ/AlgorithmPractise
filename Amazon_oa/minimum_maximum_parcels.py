from typing import List

class Solution:
    def getMinimumMaximumParcel(self, parcels: List[int], extra_parcels: int) -> int:
        def isCapable(max_value: int) -> bool:
            more_parcel_count = 0
            for parcel in parcels:
                if parcel > max_value:
                    return True
                more_parcel_count += max_value - parcel
                if more_parcel_count > extra_parcels:
                    return True
            return False
        
        left, right = max(parcels), max(parcels) + extra_parcels
        while left <= right:
            mid = (left + right) // 2
            if isCapable(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    parcels = [7, 5, 1, 9, 1]
    extra_parcels = 25
    print(Solution().getMinimumMaximumParcel(parcels, extra_parcels))