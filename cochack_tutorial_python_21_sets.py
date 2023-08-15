thisset = {"apple", "banana", "cherry"}
print(thisset)
for x in thisset:
    print(x)
    
print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.

thisset.add("orange")

print(thisset)

thisset.update(["orange", "mango", "grapes"])

print(thisset)
print(len(thisset))
# To remove an item in a set, use the remove(), or the discard() method
thisset.remove("banana")

print(thisset)

thisset.discard("grapes")

# If the item to remove does not exist, discard() will NOT raise an error.
# If the item to remove does not exist, remove() will raise an error.
# Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
x = thisset.pop()

print(x)

print(thisset)
# The clear() method empties the set:
# thisset.clear()
# The del keyword will delete the set completely
# del thisset
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = {"a", "b" , "c"}
set7 = {1, 2, 3}

set4.update(set7)
print(set4)

# Both union() and update() will exclude any duplicate items.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Python has a set of built-in methods that you can use on sets.
# Method
# Description
# add()
# Adds an element to the set
# clear()
# Removes all the elements from the set
# copy()
# Returns a copy of the set
# difference()
# Returns a set containing the difference between two or more sets
# difference_update()
# Removes the items in this set that are also included in another, specified set
# discard()
# Remove the specified item
# intersection()
# Returns a set, that is the intersection of two other sets
# intersection_update()
# Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()
# Returns whether two sets have a intersection or not
# issubset()
# Returns whether another set contains this set or not
# issuperset()
# Returns whether this set contains another set or not
# pop()
# Removes an element from the set
# remove()
# Removes the specified element
# symmetric_difference()
# Returns a set with the symmetric differences of two sets
# symmetric_difference_update()
# inserts the symmetric differences from this set and another
# union()
# Return a set containing the union of sets
# update()
# Update the set with the union of this set and others

