def fib_gen(max):
    a = 0
    b = 1
    count = 0
    
    while count < max:
        a, b = b, a+b
        yield a
        count += 1

for num in fib_gen(20):
    print(num)
    
for num in fib_gen(10):
    print(num)
