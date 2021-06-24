
def fizzbuzz(n):
    result = []
    
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            result.append('FizzBuzz')
        elif i%3 == 0:
            result.append('Fizz')
        elif i%5 == 0:
            result.append('Buzz')
        else:
            result.append(i)
    return result

def fizzbuzz_with_helper_func(n):
    return [fb(m) for m in range(1,n+1)]
    
def fb(m):
    r = (m % 3 == 0) * "Fizz" + (m % 5 == 0) * "Buzz"
    return r if r != "" else m
