class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        new_nums = sorted(enumerate(nums), key=lambda x: x[1])
        get_i = [0] * n
        for i, (orig, _) in enumerate(new_nums):
            get_i[orig] = i

        LOG = 18
        st = [[0] * LOG for _ in range(n)]

        r = 0
        for i in range(n):
            if r < i: r = i
            while (r + 1 < n and
                   new_nums[r + 1][1] - new_nums[r][1] <= maxDiff and
                   new_nums[r + 1][1] - new_nums[i][1] <= maxDiff):
