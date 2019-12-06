class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """

    def findRadius(self, houses, heaters):
        # Write your code here
        houses = sorted(houses)
        heaters = sorted(heaters)
        start = 0
        end = max(houses[-1], heaters[-1])

        while start + 1 < end:
            mid = (start + end) // 2
            if self.could_heat(houses, heaters, mid):
                end = mid
            else:
                start = mid
        if self.could_heat(houses, heaters, start):
            return start
        return end

    def could_heat(self, houses, heaters, mid):
        now_heater = 0
        for i in range(len(houses)):
            while now_heater < len(heaters) and abs(houses[i] - heaters[now_heater]) > mid:
                now_heater += 1
            if now_heater == len(heaters):
                return False
        return True

class Solution2:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        radius = 0
        i = 0
        for house in houses:
            while i < len(heaters) and heaters[i] < house:
                i += 1
            if i == 0:
                radius = max(radius, heaters[i] - house)
            elif i == len(heaters):
                return max(radius, houses[-1] - heaters[-1])
            else:
                radius = max(radius, min(heaters[i]-house, house-heaters[i-1]))
        return radius
