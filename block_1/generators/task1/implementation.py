def fib(size):
    start = 1
    next_num = 1
    exchange = start
    for i in range(size):
        yield start
        start, next_num = next_num, start + next_num
