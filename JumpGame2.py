class Solution(object):
    def jump(nums):
        # 边界情况：如果数组只有一个元素，直接返回0，因为不需要跳跃
        if len(nums) <= 1:
            return 0
    
        # 初始化变量
        jumps = 0           # 记录跳跃的次数
        current_end = 0     # 记录当前跳跃次数范围内可以到达的最远位置
        farthest = 0        # 记录能到达的最远位置（下一跳的最远位置）

        # 遍历数组中的元素，最后一个元素不需要遍历（因为到达最后位置后不需要再跳跃）
        for i in range(len(nums) - 1):
            # 更新farthest为当前元素能达到的最远位置
            farthest = max(farthest, i + nums[i])
        
            # 如果到达了当前跳跃范围的末尾，意味着需要再跳一次来继续前进
            if i == current_end:
                jumps += 1             # 增加跳跃次数
                current_end = farthest  # 更新当前跳跃范围的末尾为下一跳的最远位置
            
                # 如果当前跳跃范围已经到达或超过最后一个位置，则跳出循环
                if current_end >= len(nums) - 1:
                    break

        return jumps  # 返回总跳跃次数
    
if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(Solution.jump(nums))  # 2