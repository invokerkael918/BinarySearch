class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """

    def findDuplicate(self, nums):
        # write your code here

        start = 1
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if self.findTotalSmallerOrEqual(nums, mid) > mid:
                end = mid
            else:
                start = mid
        if self.findTotalSmallerOrEqual(nums, start) > start:
            return start
        return end

    def findTotalSmallerOrEqual(self, nums, target):
        count = 0
        for num in nums:
            if num <= target:
                count += 1
        return count
