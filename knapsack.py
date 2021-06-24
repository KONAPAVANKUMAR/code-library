class Item:

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def get_maximum_value(items, capacity):
    dp = [0] * (capacity + 1)
    for item in items:
        for cur_weight in reversed(range(item.weight, capacity+1)):
            dp[cur_weight] = max(dp[cur_weight], item.value + dp[cur_weight - item.weight])
    return dp[capacity]