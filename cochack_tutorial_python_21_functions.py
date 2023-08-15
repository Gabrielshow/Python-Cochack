# functions
# keyword argument
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
def my_function1(**kid):
    print("His last name is " + kid["lname"])

my_function1(fname = "Tobias", lname = "Refsnes") 