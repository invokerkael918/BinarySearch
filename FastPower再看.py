class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # a ^ n % b
        # 比如 n=5,可以看做 a^(101)2 % b （5的二进制是101）
        # 拆开也就是 [a^(100)2 * a&(1)2] % b
        # 因此相当于我们把 n 做二进制转换，碰到 1 的时候，称一下对应的 a 的幂次
        # 而 a 的幂次我们只需要知道 a^1, a^(10)2, a^(100)2 ... 也就是 a^1, a^2, a^4 ...
        # 因此不断的把 a = a * a 就可以了
        # 中间计算的时候，随时可以 % b 避免 overflow 其不影响结果，这是 % 运算的特性。
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = (ans * a) % b
            a = a * a % b
            n = n // 2
        return ans % b