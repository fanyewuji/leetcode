class Solution:
    def longestMountain(self, A: List[int]) -> int:
        state = ''
        res = 0
        count = 0
        top = -float('inf')
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                if state == 'down':
                    res = max(res, count+1)
                    count = 0
                    state = ''
                elif state == 'up':
                    count = 0
                    state = ''
            elif A[i] > A[i-1]:
                if state == 'down':
                    res = max(res, count+1)
                    count = 1
                    state = 'up'
                elif state == 'up':
                    count += 1
                else:
                    count = 1
                    state = 'up'
            else:
                if state == 'down':
                    count += 1
                elif state == 'up':
                    count += 1
                    state = 'down'
            # print(i, state, count)
        if state == 'down':
            res = max(res, count+1)
        return res