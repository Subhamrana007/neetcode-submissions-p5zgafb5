class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2 

        if len(a) > len(b):
            a, b = b, a

        l, r = 0, len(a) - 1

        while True:
            mid = (l + r) // 2

            aleft = a[mid] if mid >= 0 else float("-inf")
            aright = a[mid + 1] if (mid + 1) < len(a) else float("inf")

            bleft = b[half - mid - 2] if (half - mid - 2) >= 0 else float("-inf")
            bright = b[half - mid - 1] if (half - mid - 1) < len(b) else float("inf")


            if aleft <= bright and bleft <= aright:
                if total % 2 == 1:
                    return min(aright, bright)
                else:
                    return (max(aleft, bleft) + min(aright, bright)) / 2

            elif aleft > bright:
                r = mid - 1
            else:
                l = mid + 1
