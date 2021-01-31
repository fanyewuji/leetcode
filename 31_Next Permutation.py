class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ref https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
        if len(nums) == 1:
            return
        n = len(nums) 
        for i in range(n-1,-1,-1):
            if nums[i-1] < nums[i]:
                break
        if i == 0:
            nums.sort()
            return
        for j in range(n-1,i-1,-1):
            if nums[j] > nums[i-1]:
                break
        nums[i-1], nums[j] = nums[j], nums[i-1]
        l, r = i, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1