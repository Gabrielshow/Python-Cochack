#performance measurement
from timeit import Timer
value = Timer('t=a; a = b; b=t', 'a=1; b=2').timeit()
print(value)

value = Timer('a, b = b, a', 'a=1;b=2').timeit()
print(value)