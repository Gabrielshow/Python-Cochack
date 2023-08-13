#the random module
import random
import statistics
value = random.choice(['apple', 'banana', 'pearl'])

#sampling without replacement
value = random.sample(range(100),10)
print(value)

#random float
value = random.random()
print(value)

#random integer chosen form range
value = random.randrange(8)
print(value)

data = [2.75, 1.75, 1.25, 0.25, 1.5, 3.5]
value = statistics.mean(data)
print(value)

value = statistics.median(data)
print(value)

value = statistics.variance(data)
print(value)




