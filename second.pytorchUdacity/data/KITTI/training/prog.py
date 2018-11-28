import os

with open("./dict_removed.txt") as myfile:
    Lines = myfile.readlines()
    Line = Lines[0]
#    myfile.write("\n")
    infos = Line.split(' ')
print(len(Line))
with open("./dict_removed2.txt", "w") as myfile:
    for i in range(int(len(Line)/13)):
        indmin = i * 13
        indmax = (i + 1) * 13
        myfile.write(Line[indmin:indmax]+"\n")
