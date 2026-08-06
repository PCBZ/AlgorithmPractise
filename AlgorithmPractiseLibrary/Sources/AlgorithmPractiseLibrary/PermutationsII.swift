class Solution {
    func permuteUnique(_ nums: [Int]) -> [[Int]] {

        let sortedNums = nums.sorted()
        var res = [[Int]]()
        var used = [Int: Bool]()
        func backtrack(_ path: inout [Int]) {
            if path.count == sortedNums.count {
                res.append(path)
                return
            }
            for i in 0..<sortedNums.count {
                if used[i] ?? false {
                    continue
                }
                if i > 0 && sortedNums[i] == sortedNums[i-1] && !(used[i-1] ?? false) {
                    continue
                }
                path.append(sortedNums[i])
                used[i] = true
                backtrack(&path)
                path.removeLast()
                used[i] = false
            }
        }
        var path = [Int]()
        backtrack(&path)
        
        return res
    }
}
