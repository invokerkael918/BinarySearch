class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        while start + 1 < end:

            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        else:
            return -1
if __name__ == '__main__':
    S = Solution().lastPosition([1,1],1)
    print(S)