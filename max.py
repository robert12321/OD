import os, sys


#tab = np.array([1000])
Min = 99999999
ind = 0
Pack = "2"
Set = "12_f"
with open("./"+Pack+"/TRACKLETS/"+Set+"/obs1_rear_rtk_interpolated.csv") as obsfile:
    with open("./"+Pack+"/TRACKLETS/"+Set+"/cap_rear_rtk_interp.csv") as capfile:
        capfile.readline()
        obsfile.readline()
        for i in range(len([f for f in os.listdir("./"+Pack+"/TRACKLETS/"+Set+"/camera/") ])):
            Inf1 = capfile.readline().split(',')
            Inf2 = obsfile.readline().split(',')

            x1 = float(Inf1[2])
            y1 = float(Inf1[3])
            #z1 = float(Inf1[4])
            x2 = float(Inf2[2])
            y2 = float(Inf2[3])
            #z2 = float(Inf2[4])
            
            d = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
            if Min > d:
                ind = i
                Min = d

print(Min)
print(ind)
