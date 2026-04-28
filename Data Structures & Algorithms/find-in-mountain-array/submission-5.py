class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l, r = 1, length - 2

        while l <= r:
            mid = (l + r) // 2
            left, right, midd = mountainArr.get(mid - 1), mountainArr.get(mid + 1), mountainArr.get(mid)

            if left < midd < right:
                l = mid + 1

            elif left > midd > right:
                r = mid - 1

            else:
                break

        peak = mid

        l, r = 0, peak 

        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val < target:
                l = mid + 1

            elif val > target:
                r = mid - 1

            else:
                return mid

        l, r = peak, length - 1

        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val > target:
                l = mid + 1

            elif val < target:
                r = mid - 1

            else:
                return mid

        return -1

        