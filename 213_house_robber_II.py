# dynamic programing
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            def simple_rob(num_list, i, j):
                rob, not_rob = 0, 0
                for idx in range(i,j):
                    # two cases,
                    # rob the current house and the value becomes not_rob + nums[idx]
                    # not rob the current house, then the value is the maxium either rob or not rob the last house
                    rob, not_rob = not_rob+nums[idx], max(rob, not_rob)
                return max(rob, not_rob)
            n = len(nums)
            # either nums[0:n-1] or nums[1:n] has the maxium value under the condition that nums[0] and nums[n-1] are considered adjacent 
            return max(simple_rob(nums,0, n-1), simple_rob(nums,1,n))