#lambda expression
#small anonymous functions can be created with the lambda keyword.
def make_increment(n):
    return lambda x: x + n

f = make_increment(42)
f(0)
f(2)  #44

pairs = [(1,'one'), (2,'two'), (3,'three'),(4,'four')]
#sorts the array based on the second index
pairs.sort(key = lambda pair: pair[1])
print(pairs)

#lines don't exceed 79 characters
#use camelcase for classes and lower_case_with_underscores for functions
#and methods

#always use self as the name for hte first method argument

