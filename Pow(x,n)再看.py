class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """

    def myPow(self, x, n):
        # 接着刷
        # Take care of the case when n < 0
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        current_product = x
        while n > 0:
            if n % 2 == 1:
                ans = ans * current_product
                n = n - 1
            else:
                # when the power is even, double the current product, (e.g. 2^4 = (2^2)^2)
                current_product = current_product * current_product
                n = n // 2
        return ans