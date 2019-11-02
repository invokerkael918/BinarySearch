class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        # write your code here
        n = len(A) + len(B)
        if n % 2 == 0:
            return (self.findKthElement(A, B, n // 2) + self.findKthElement(A, B, n // 2 + 1)) / 2
        return self.findKthElement(A, B, n // 2 + 1)

    def findKthElement(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        start = min(A[0], B[0])
        end = max(A[-1], B[-1])
        while start + 1 < end:
            mid = (start + end) // 2
            # [1,2,3,4,5]
            # [2,3,4,6]
            # mid = 3
            n = self.count_smaller_or_equal(A, mid)
            m = self.count_smaller_or_equal(B, mid)

            if n + m >= k:
                end = mid
            else:
                start = mid
        if self.count_smaller_or_equal(A, start) + self.count_smaller_or_equal(B, start) == k:
            return start
        return end

    def count_smaller_or_equal(self, l, k):
        start = 0
        end = len(l) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if l[mid] <= k:
                start = mid
            else:
                end = mid
        if l[end] <= k:
            return end + 1
        if l[start] <= k:
            return start + 1
        return 0


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    B = [2, 3, 4, 5]
    S = Solution().findMedianSortedArrays(A, B)
    print(S)
