#del statement
a = [-1,1,50.25,333,393]
del(a[0])
print(a)

#tuples
#they are immutable

#sets
#set operators

a = set('abracadabra')
b = set('alacazam')

print(a)

#letters in a but not in b
val = a - b
print(val)

#letters in a or b or both
union = a | b
print(union)

#letters in both a & b
both = a & b
print(both)

#letters in a or b but not in both
a_b_not_both =  a^b
print(a_b_not_both)

#set comprehension
a1 = { x for x in 'abracadabra' if x not in 'abc'}
print(a1)

#dictionaries
#they store key and value pairs
tel = {'jack': 4038, 'scope':4139}
print(tel['jack'])

#looping techniques on dictionaries

#key and corresponding value can be retrieved of the same item
#using the items() method
knights = {'gallhead': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)
    
#when looping through a sequence, the position inde & corresponding value can be retrieved at the same
#time using the enumerate function.
for i, v in enumerate(knights):
    print(i,v)
#it works better with arrays if used on dicitionaries the
#index and the key will be printed
    
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)
    
#to loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite-color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('what is your {0} ? It is {1}.'.format(q,a))
    
for i in reversed(range(1, 10, 2)):
    print(i)
    
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
    

    


