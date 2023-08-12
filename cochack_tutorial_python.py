#a simple print function
print('hello world!')

#multiline strings
print("""


""")

#simple concatenation

#using the + operator or implicit concatenation
#samething
print("py" + "thon")
print("py" "thon")

#simple list definition
list = [1,4,9]

#slicing
print(list[:])

#functions
#a simple fibonacci series
def fib_series(num):
    a, b = 0, 1
    while a < num:
        print(a)
        a, b = b, a+b

fib_series(17)
        