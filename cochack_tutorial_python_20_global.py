# if you use the global keyword, the variable belongs to the global scope
def myfunc():
    global x
    x = "Cool"
    
myfunc()

print("Python is " + x)

# use the global keyword if you want to change a global variable in a function

x = "Incredible"

def func():
    global x
    x = "Awesome"
    
func()

print("Python is " + x)