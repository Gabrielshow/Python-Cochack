#classes
# class complex():
#     def _init_(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#         
# 
# v = complex(3.0, 4.5)
# print(v.r)
# print(v.i)

#multiple inheritance
# class derivedClass ( base1, base2 , base3, base4):
#     pass
from math import pi, sin
from timeit import Timer

#generators
#for generators we use the uiled keyword to return data
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]


for char in reverse('golf'):
    print(char)
    
#generator expressions
value = sum(i *i for i in range(10))
print(value)

xvec = [10, 20, 30]
yvec = [7, 8 ,3]

#dot product
value = sum(x * y for x, y in zip(xvec, yvec))
print(value)

sine_table = {x: sin((x*pi)/180) for x in range(0, 91)}
# value = Timer(sine_table).timeit
print(sine_table)


#this could be later improved upon and saved to a csv and used for data science activities
#it is also a simple way to generate tables for various mathematical functions

#this will also throw an error because page is not defined
#you scrape a page with beautiful soup
#then create a file with keywords on each particular site
# unique_words = set(word for line in page for word in line.split())
# print(unique_words)

#where graduates could be a file/csv
#without that file this code won't run
# valecdictorian = max((student.gpa, student.name) for student in graduates)
# print(valecdictorian)

data = 'tennis'
value = list(data[i] for i in range(len(data)-1, -1,-1))
print(value)


