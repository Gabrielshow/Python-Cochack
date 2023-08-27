# python inbuilt structures
from collections import ChainMap
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple

defaults = {'theme': 'default', 'language':'eng', 'showIndex': True, 'showFooter': True}
cm =  ChainMap(defaults)
cm2 = cm.new_child({'theme':'bluesky'})
print(cm2['theme'])
print(cm2.pop('theme'))
print(cm2['theme'])
cm2.maps[0] = {'theme':'desert', 'showIndex':False}
print(cm2['showIndex'])
print(cm2.parents)

# counter 
ct = Counter()
ct.update('abca')
print(ct)
ct.update({'a':3})
print(ct)
for item in ct:
    print('%s : %d' % (item, ct[item]))

# orderedDict
# it is often used in conjunction with the sorted methd to create a sorted dicitonary.
# for example, in the following example we sue a lambda function to sort on the values, here we use a numerical expression to sort the intger values:
od1 = OrderedDict()
od1['one'] = 1
od1['two'] = 2
od2 = OrderedDict()
od2['two'] = 2
od2['one'] = 1


# defaultdict
# defaultdict overrides one method, __missing__(key), and creates a new instance variable, defualt_factory.
# with defaultdict, rather than throw an error, it will run the function, supplied as the default_factory argument, which will genrate a value.
# a simple use of defaultdict is to set default_factory to int and use it to quickly tally the counts of items int he dictionary, for example:
kvs = [('three', 3), ('four', 4), ('five', 5), ('six', 6)]
od1.update(kvs)
for k, v in od1.items(): print(k,v)


#named tuples
# namedtuple method returns a tuple-like object that has fields accessible with named indexes as weel as the integer indexes of normal tuples. This allows for code
# that is, to a cerain extent, self-documenting and more readable. it can be especially useful in an application where there is a large number of tuples and we need to easily keep track of what
# each tuple represents. The namedtuple inherits methods from tupel and it is backward-compatible with tuple
# The field names are passed to the namedtuple method as comma and/or whitespace separated values. They can also be passed as a sequence of strings.
# Field names are single strings and thye can be any legal Python identifier that does not begin with a digit or an underscore.
dd = defaultdict(int)
words = str.split('red blue green red yellow blue red green greenn red')
for word in words: dd[word] += 1
print(dd)

# The namedtuple method take two optional Boolean arguments, verbose and rename. When verbose is set to True then the class definition is printed when ti si built. This argument is depreciated in favor of using the __source
# attribute. When the rename argument is set to True then any invalid field names will be automatically replaced with positional arguments. As an example, we attempt to use def as a field name. This would normally generate an error, but since we have assigned rename to True, the Python
# intrepreter allows this. However, when we attempt to look up the def value, we get a syntax error, since def is a reserved keyword. The
# illegal field name has been replaced by a field name created by adding an underscore to the positional value.
# dd2 = defaultdict(bool)
# for word in words: dd2[word] = isprimary(word)
# print(dd2)
space = namedtuple('space', 'x y z')
s1 = space(x = 2.0, y = 4.0, z = 10)
print(s1.x * s1.y * s1.z)

# the _asdict method returns an OrderedDict with the field names mapped to index keys and the values mapped to the dicitionary values, for example
space2 = namedtuple('space2', 'x def z', rename=True)
s1 = space2(3,4,5)
# s1.def #syntax Error: invalid syntax
print(s1._1)
# the replace method returns a new instance of the tuple, replacing the specified values, for example:
s3 = [4,5,6]
print(space._make(s3))

# Algorithm design paradigms
# Divide and conquer
# Greedy algorithms
# Dynamic programming
