class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """

    def myPow(self, x, n):
        # 接着刷
        # Take care of the case when n < 0
        # 磨2除2是为了转换2进制，if判定如果当前位置为一时ans乘x，反之不乘。
        # Example 3^6 = 3^4 * 3^2 = 1*3^4 + 1*3^2 + 0*3^1:
        # 磨第一此时个位为0，不乘，不过底数要自己乘自己(3^2)，因为已经到了十位，是2次蜜了
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        current_product = x
        while n > 0:
            if n % 2 == 1:
                ans = ans * current_product
                # when the power is even, double the current product, (e.g. 2^4 = (2^2)^2)
            current_product = current_product * current_product
            n = n // 2
        return ans