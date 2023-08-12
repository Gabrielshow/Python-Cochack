#control flow
def control_flow():
    x = 10
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('zero')
    elif x == 1:
        print('single')
    else:
        print('more')

control_flow()

#simple ranges
# for i in range (5):
#	print(i)

#pass statement
#it does nothing. it can be used when a statement is required
#syntactically but the program requires no action.
#it is also used as a place-holder for a function or conditional body when
#you are working on new code, allowing you to keep thinking at a more abstract level.
# the pass is silently ignored.

class MyEmptyClass:
    pass

def initlog(*arg):
    pass

#functions
#arbitrary argument lists or variadic function we use * to show  a variable that takes any number of arguments unlike the
#spread [...] operator used in other programming languages

def write_multiple_items(file , separator, *args):
    file.write(separator.join(args))
    

def concat(*args, sep="/"):
    return sep.join(args)

print( concat("earth", "mars" , "venus"))
print( concat("earth", "mars", "venus", sep="."))

#unpacking argument list or variadic parameters
#use * to unpack
print(list(range(3,7)))

args = [3,7]
print(list(range(*args)))
#in the same fashion dicitionaries can be unpacked with the ** operator
def parrot(voltage, state = "a stiff", action="vroom"):
    print ("--This parrot wouldn't", action, end = '')
    print (" if you put", voltage, "volts through it. ", end = '')
    print ( "E's", state, "!")
    
d = {"voltage": "four million", "state" : "bloody Demised", "action" : "VOOM" }
parrot(**d)