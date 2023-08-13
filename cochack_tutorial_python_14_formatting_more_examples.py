#python indexes
sentence = "The right hand of God is in everything but his left, how often do you see God use his right hand, it is indeed a miraculous sight. convention states his left hand is solely for his displeasure..."
firstleft = sentence.find("left")
print(firstleft)
lastleft = sentence.rfind("left")
print(lastleft)
firstright = sentence.index("right")
print(firstright)
lastright = sentence.rindex("right")
print(lastright)
print('Numbered lefts: ', sentence.count("left"))
print(sentence.startswith("The"))
print(sentence.endswith("..."))

#slicing
word = "everything"
print(word[1:5]) #not including index 5
print(word[4:2]) #empty string

#formatting string
name1 = "James"
name2 = "Barton"
love1 = "{0: ^7} {1:>3}".format(name1, name2)
print(love1)

#the 7 above declares the width of the argument
#^ -> centre align; forces the padding to placed after the sign( if any)
#< -> left aligned
#> -> right aligned

num1 = 89548.9
num2 = 9845.89
output = "{0:>10.3f} {1:.5f}".format(num1,num2)
print(output)

#f -> fixed point type
#g -> general format; significant digits to include

seven = "boy"
word = "Harold's a clever {0!s}".format(seven)
#the !s calls string on the argument first
print(word)

word1 = "Harold's a clever {0!r}".format(seven)
#calls repr() on the argument first
print(word1)

word2 = "Harold's a clever {0!a}".format(seven)
#calls ascii on the argument first
print(word2)

#repr shows quote while string doesn't
print('{:*^30}'.format('centered')) #the use of "*" as a fill char
print('{:,}'.format(123457890))

score = 19
total = 22
print('correct answer: {:.2%}'.format(score/total))

#use of extend
array = []
list2 = [-57, 27, 8]
array.extend(list2)
print(array)






