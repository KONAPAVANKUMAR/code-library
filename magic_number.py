def magic_number(n):
    total_sum = 0
    while n > 0 or total_sum > 9:
        if n == 0:
            n = total_sum 
            total_sum = 0
        total_sum += n % 10
        n //= 10
    return total_sum == 1