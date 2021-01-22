class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # add nums to the end of nums to form the circular list
        new_nums = nums + nums
        d = {}
        stack = []
        res = []
        for i in range(len(new_nums)):
            # as the number is not unique, append its index to the stack
            while stack and new_nums[stack[-1]] < new_nums[i]:
                d[stack.pop()] = new_nums[i]
            stack.append(i)
            
        res = [d.get(i, -1) for i in range(len(nums))]
        return res