#output formatting
import reprlib
import pprint
value = reprlib.repr(set('supercalifragilisticexpialidocious'))
print(value)

#pretty printer
#it adds line breaks & indentation to more clearly reveal data structures
t = [[[['black','cyan'],'white',['green','red']], [['magenta','yellow'], 'blue']]]
pprint.pprint(t, width = 30)


