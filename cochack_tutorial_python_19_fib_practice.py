#simple fibonacci function
num = int(input("Enter a number: "))

#first fibonacci number starting from zero
def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        print(n-1)
        return (0, 1)
    else:
        prev = fibonacci(n - 1)
        a, b = prev
        a, b = b, a + b
        print(a)
        return (a, b)

#another pattern
def fib(n):
    if n < 1:
        return 0
    else:
        x, y = 1, 0
        for i in range(n):
            x, y = y, x+y
            print(x)

fib(num)

# fibonacci(num)

