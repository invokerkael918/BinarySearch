class Solution:
    """
    @param x: a double
    @return: the square root of x
    """

    def sqrt(self, x):
        # write your code here
        if x == 0:
            return 0

        start, end = 0, x
        if 0 < x < 1:
            end = 1

        while start + 1e-12 < end:
            mid = (start + end) / 2
            if mid * mid > x:
                end = mid
            else:
                start = mid

        if end * end <= x:
            return end

        return start


class MySolution:
    """
    @param x: a double
    @return: the square root of x
    """

    def sqrt(self, x):
        # write your code here
        if x == 0:
            return 0
        start, end = 0, x
        if 0 < x < 1:
            end = 1
        mark = 0.0000000001
        while start * start - x < mark or end * end - x < mark:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid
            else:
                start = mid

        if end * end <= x:
            return end
        return start
