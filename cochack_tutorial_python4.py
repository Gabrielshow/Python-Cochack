#cochack tutorial contd
result = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(result)

#this is also equivalent to
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

print(combs)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

#nested list comprehension
matrix = [[1,2,3,4],[5,7,8,9,],[10,11,12,13]]
val = [[row[i] for row in matrix] for i in range(4)]
print(val)

#this transposes rows & columns
#this is equivalent to
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

#or using in-built function like zip()
zipped = list(zip(*matrix))
print(zipped)
