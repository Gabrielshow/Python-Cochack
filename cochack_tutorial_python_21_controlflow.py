# control flow
# If you have only one statement to execute, you can put it on the same line as the if statement.
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 2000
b = 330
c = 500
if a > b: print("a is greater than b")
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")
if a > b and c > a:
    print("Both conditions are True")
if a > b or a > c:
    print("At least one of the conditions is True")

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
    print(x)
else:
    print("Finally finished!") 