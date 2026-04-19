class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            balti = 1
            capacity = 0

            for n in nums:
                if capacity + n <= mid:
                    capacity += n

                else:
                    capacity = n
                    balti += 1

            if balti <= k:
                res = mid
                r = mid - 1

            else:
                l = mid +  1

        return res