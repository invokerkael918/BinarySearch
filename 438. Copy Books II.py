class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """

    def copyBooksII(self, n, times):
        # write your code here
        start = min(times)
        end = start * n
        while start + 1 < end:
            mid = (start + end) // 2
            if self.canFinish(n, times, mid):
                end = mid
            else:
                start = mid
        if self.canFinish(n, times, end):
            return end
        return start

    def canFinish(self, n, times, limit):
        count = 0
        # count is how many books we can copy in limit_time
        # return true if greater or equal to n, means we can finish n books in limit time
        for time in times:
            count += limit // time
        return count >= n


if __name__ == '__main__':
    S = Solution().copyBooksII(4, [3, 2, 4])
    print(S)
