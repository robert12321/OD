
import sys
import time
import numpy
import string
import os #for file management make directory
import shutil #for file management, copy file
xxx = 1
DirOfTrack = sys.argv[1]
for binDir in [f for f in os.listdir(DirOfTrack)]:
    listOfBin = [f for f in os.listdir("pc-"+binDir)]
    listOfImag = [f for f in os.listdir(DirOfTrack+binDir+"/camera/")]
    if len(listOfImag)==0:
	continue
    i = 0
    os.system("mkdir pc-"+binDir+"-proc")
    print "Processing pc-"+binDir
    for img in listOfImag:
    	j = i*len(listOfBin)/len(listOfImag)
	if xxx==1:
	    print j
	    print "cp pc-"+binDir+"/"+listOfBin[j]+" pc-"+binDir+"-proc/"+img[:-4]+".bin"
    	os.system("cp "+"./pc-"+binDir+"/"+listOfBin[j]+" pc-"+binDir+"-proc/"+img[:-4]+".bin")
	i = i+1
    xxx = 0
