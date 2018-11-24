import os

lista = [f for f in os.listdir("./label_2/")]
for f in lista:
    with open("./label_2/"+f) as labelf:
        Lines = labelf.readlines()
        Line = Lines[0]
        Dane = [float(info) for info in Line.split(' ')[1:13]]
        print(Dane)
