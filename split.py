import os
import random


listOfFilesTrain = [f for f in os.listdir('./training/')]
random.shuffle(listOfFilesTrain)
ValList = listOfFilesTrain[:int(len(listOfFilesTrain)/2)]
TrainList = listOfFilesTrain[int(len(listOfFilesTrain)/2):]

for filename in listOfFilesTrain:
    with open("trainval.txt", "a") as myfile:
    	myfile.write(filename[:-4])
for filename in TrainList:
    with open("train.txt", "a") as myfile:
    	myfile.write(filename[:-4])
for filename in ValList:
    with open("val.txt", "a") as myfile:
    	myfile.write(filename[:-4])

listOfFilesTest = [f for f in os.listdir('./test/')]

for filename in listOfFilesTest:
    with open("test.txt", "a") as myfile:
    	myfile.write(filename[:-4])

