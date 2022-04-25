def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci_generator = fibonacci()

for _ in range(15):
    print(next(fibonacci_generator))
