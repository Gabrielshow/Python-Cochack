# Array methods
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
thislist.remove("banana")
print(thislist)
#The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print(thislist)
thislist.pop(1)
print(thislist)
del thislist[0]
print(thislist)
# The del keyword can also delete the list completely:
# del thislist
# The clear() method empties the list:
# thislist.clear()
# print(thislist)
thislist.append("orange")
thislist.append("banana")
thislist.append("grape")

# Make a copy of a list with the copy() method:
mylist = thislist.copy()
print(mylist)
# Another way to make a copy is to use the built-in method list().
mylist1 = list(thislist)
print(mylist)
newlist = mylist + mylist1
print(newlist)

# Another way to join two lists are by appending all the items from list2 into list1, one by one:
list1 = ["Goku", "Gosu", "Sinatra"]
for x in newlist:
    list1.append(x)
print(list1) 

# Or you can use the extend() method, which purpose is to add elements from one list to another list:
list2 = []
list2.extend(list1)
print(list1)

# It is also possible to use the list() constructor to make a new list.
thislist1 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist1)

# Python has a set of built-in methods that you can use on lists.
# Method
# Description
# append()
# Adds an element at the end of the list
# clear()
# Removes all the elements from the list
# copy()
# Returns a copy of the list
# count()
# Returns the number of elements with the specified value
# extend()
# Add the elements of a list (or any iterable), to the end of the current list
# index()
# Returns the index of the first element with the specified value
# insert()
# Adds an element at the specified position
# pop()
# Removes the element at the specified position
# remove()
# Removes the item with the specified value
# reverse()
# Reverses the order of the list
# sort()
# Sorts the list