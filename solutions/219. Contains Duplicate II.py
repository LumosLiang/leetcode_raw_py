class Solution:
    def containsNearbyDuplicate(self, nums, k):
        value_index = {}
        for idx, value in enumerate(nums):
            if value not in value_index:
                value_index[value] = [idx]
            else:
                value_index[value].append(idx)
                if len(value_index[value]) >= 2 and (value_index[value][-1] - value_index[value][-2] <= k):
                    return True
                else:
                    continue

        return False
