class Solution:
    def maxProfit(self, prices):

        # my algorithm:
        # Find all the local valley point and local peak point
        # for every local valley point, compute the max with every local peak point
        # Then return the largest one

        if prices == []:
            return 0
        
        if len(prices) == 1:
            return 0

        local_valley_points = []
        local_peak_points = []

        for i in range(len(prices)):
            if i == 0:
                if prices[i + 1] - prices[i] > 0:
                    local_valley_points.append(i)
                else:
                    local_peak_points.append(i)
            elif i == len(prices) - 1:
                if prices[i] - prices[i - 1] > 0:
                    local_peak_points.append(i)
                else:
                    local_valley_points.append(i)
            elif prices[i] - prices[i - 1] > 0 and prices[i + 1] - prices[i] <= 0:
                local_peak_points.append(i)
            elif prices[i] - prices[i - 1] <= 0 and prices[i + 1] - prices[i] > 0:
                local_valley_points.append(i)

        if len(local_valley_points) == 1 and len(local_peak_points) == 1:
            if local_valley_points == [len(prices) - 1]:
                return 0
            elif local_valley_points == [0]:
                return prices[-1] - prices[0]
        
        max_profit = 0
        for local_valley in local_valley_points:
            for local_peak in local_peak_points:
                if not local_peak < local_valley:
                    if prices[local_peak] - prices[local_valley] > max_profit:
                        max_profit = prices[local_peak] - prices[local_valley]

        return max_profit
