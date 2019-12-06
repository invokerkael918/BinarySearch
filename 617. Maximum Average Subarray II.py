class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """

    def maxAverage(self, nums, k):
        # write your code here
        """
        问题转换 ： 能不能找出平均值大于等于t的一段子数
        假设能，证明存在 ai - aj/j-i+1 > t
        """
        start = float(min(nums))
        end = float(max(nums))

        while start + 1e-5 < end:
            mid = (start + end) / 2  # t is mid
            if (self.canFind(nums, k, mid)):
                start = mid
            else:
                end = mid
        return start

    def canFind(self, nums, k, T):
        """
        return whether we can find nums[left...right] sum >= mid
        S = [   si|    sj|   ]
        S[j] is rightSum, 最少为前k个，所以一开始先加入前k个进去， 以后每次加入一个新的，在第44行，S[j]是个前缀和
        S[i] 可取值范围是从S[0] 到S[j-k], S[j-k] is leftSum
        S[j-k]和S[j] 永远隔k， 两条线平行移动
        我们需要的是si 左边一堆里最小的前缀和 即为minLeftSum
        """
        rightSum, leftSum, minLeftSum = 0.0, 0.0, 0.0
        for i in range(k):
            rightSum += nums[i] - T  # B[i]

        for i in range(k, len(nums) + 1):
            if rightSum - minLeftSum >= 0:
                return True
            if i < len(nums):
                rightSum += nums[i] - T
                leftSum += nums[i - k] - T
                minLeftSum = min(leftSum, minLeftSum)
        return False


if __name__ == '__main__':
    S = Solution().maxAverage([1, 12, -5, -6, 50, 3], 3)
    print(S)
