#files
# openfile = open("c:/Users/kp/keys.txt", "w+")
# filedata = openfile.read()
# print(filedata)

keys = open("word.txt", "w+")
keys.write("These are the keys not working on my system")

datafile = open("word.txt", "r+")
for line in datafile.readlines():
    print(line)
datafile.close()

# we could also do it like this
# datafile2 = open("word.txt", "r+")
# for line in datafile2:
#     print(line)
# datafile.close

outputfile = open("word.txt", "w+")
outputfile.writelines(["first line\n", "second line \n"])
outputfile.write("Third line \n fourth line \n")
# checkfile("word.txt")

#appending files
outputfile2 = open("word.txt", "a+")
outputfile2.write("appending this to outputs \n")
outputfile2.close()