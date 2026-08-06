class LongestSubstringWithoutRepeatingCharacters {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var used = Set<Character>()
        var end = 0
        let chars = Array(s)
        var maxLength = 0
        
        for start in 0..<chars.count {
            while end < chars.count && !used.contains(chars[end]) {
                used.insert(chars[end])
                end += 1
            }
            maxLength = max(maxLength, end - start)
            used.remove(chars[start])
        }
        
        return maxLength
    }
}
