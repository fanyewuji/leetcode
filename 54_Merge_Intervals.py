class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i][0] > intervals[i-1][1]:
                i += 1
            else:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
        return intervals