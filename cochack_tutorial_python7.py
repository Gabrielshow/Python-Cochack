#fancier output formatting
import math
year = 2023
event = 'Referendum'
val = f'Results of the {year} {event}'
print(val)

print(f'The value of pi is approximately {math.pi:.3f}.')

#other string format method
print('we are the {} who say {}.'.format('knights', 'Ni'))

print('This {food} is {adjective}.'.format(food = 'spam', adjective = 'absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill','Manthers', other = 'Georg'))

table = {'sjoerd' : 4127, 'Jack':4098, 'Dcab': 8737878}
print('Jack: {0[Jack]:d}, sjoerd: {0[sjoerd]:d}, Dcab: {0[Dcab]:d}'.format(table))

#you could also implement the above like this
print('Jack: {Jack:d}, sjoerd: {sjoerd:d}, Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    
#manual string formatting
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
    
#oldstring formatting
print('the value of pi is approximately % 7.7f.' % math.pi)



    