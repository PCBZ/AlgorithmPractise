//
//  main.swift
//  AlgorithmPractise
//
//  Created by wenshuang zhou on 2026-05-31.
//

import Foundation

print("Hello, World!")

class Solution {
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        func findLeft() -> Int {
            var (start, end) = (0, nums.count - 1)
            while start < end {
                let mid = (start + end) / 2
                if nums[mid] < target {
                    start = mid + 1
                } else {
                    end = mid
                }
            }
            return end
        }

        func findRight() -> Int {
            var (start, end) = (0, nums.count - 1)
            while start < end {
                let mid = (start + end) / 2
                if nums[mid] <= target {
                    start = mid
                } else {
                    end = mid + 1
                }
            }
            return start
        }

        return [findLeft(), findRight()]
    }
}


print(Solution().searchRange([5,7,7,8,8,10], 8))
