class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # two types of ranges, if seats[0] or seats[-1] is 0, then we have side range, the maximum distance is the side range itself.
        # the second type is middle range, the range is defined by two 1s on both sides. The maxium distance we can achieve is (cur_idx - last_idx)/2, then we loop through the seats and constantly update the maximum middle range
        # if the last seat is 0, we have another side_range
        # the final result is the larger of max(side_range) and max(middle_range/2) 
        last_idx = -1
        side_range = 0
        middle_range = 0
        for cur_idx in range(len(seats)):
            if seats[cur_idx] == 1:
                if last_idx == -1:
                    side_range = cur_idx
                else:
                    middle_range = max(middle_range, cur_idx-last_idx)
                last_idx = cur_idx
        if seats[-1] == 0:
            side_range = max(side_range, len(seats)-1-last_idx)
        return max(side_range, int(middle_range/2))