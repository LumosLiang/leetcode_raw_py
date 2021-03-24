class Solution:
    def maxProfit(self, prices):

        # my algorithm
        # Find all the local lowest point and local hightest point
        # The max prpoints) == 1 and len(local_peak_points) == 1:

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
        
        # locate each local valley point, find the next closest local peak point, make the buy
        # for next local valley point, find the next closest local peak point, make the buy
        pointer_v = 0
        max_profit = 0
        while pointer_v < len(local_valley_points):
            if local_peak_points == []:
                break
            elif local_peak_points[0] > local_valley_points[pointer_v]:
                max_profit += prices[local_peak_points[0]] - prices[local_valley_points[pointer_v]]
                pointer_v += 1
                local_peak_points.pop(0)
            else:
                local_peak_points.pop(0)
            
        return max_profit
