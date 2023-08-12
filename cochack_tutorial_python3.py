from collections import deque
queue = deque(["Eric", "john", "michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)
print(deque(['Michael', 'Terry', 'Graham']))


#List comprehension
def squares():
    squares = []
    for x in range(10):
        squares.append(x**2)
    print(squares)
    

squares()

#this can also be achieved in one line by using list comprehension
squares1 = [x**2 for x in range(10)]
squares2 = list(map(lambda x : x **2, range(10)))

print(squares1)
print(squares2)
