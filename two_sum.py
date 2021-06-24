def two_sum(numbers, target):
    for i in range(len(numbers)):
        second_val = target - numbers[i]
        low, high = i+1, len(numbers)-1
        while low <= high:
            mid = low + (high - low) // 2
            if second_val == numbers[mid]:
                return [i + 1, mid + 1]
            elif second_val > numbers[mid]:
                low = mid + 1
            else:
                high = mid - 1