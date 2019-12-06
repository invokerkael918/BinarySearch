class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
        start = max(pages)
        end = sum(pages)

        while start + 1 < end:
            mid = (start + end) // 2

            if self.get_least_ppl(pages, mid) <= k:
                end = mid
            else:
                start = mid
        if self.get_least_ppl(pages, start) <= k:
            return start
        return end

    def get_least_ppl(self, pages, limit_time):
        count = 1
        time_cost = 0
        for page in pages:
            if time_cost + page > limit_time:
                count += 1
                time_cost = page
            else:
                time_cost += page
        return count
