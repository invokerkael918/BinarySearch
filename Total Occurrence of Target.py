class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def totalOccurrence(self, A, target):
        # write your code here
        if not A:
            return 0
        first = self.getFirstPosition(A, target)
        last = self.getLastPosition(A, target)
        if first == -1:
            return 0
        else:
            return last - first + 1

    def getFirstPosition(self, nums, target):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid

            elif nums[mid] == target:
                end = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def getLastPosition(self, nums, target):
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


