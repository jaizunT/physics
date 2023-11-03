import math
import copy
def volt(q,x,y,point):
    return q/dist(x,y,point[0],point[1])

def dist(x1,y1,x2,y2):
    return math.sqrt((x1/100-x2/100)**2+(y1/100-y2/100)**2)
def error(exp,theor):
    return abs((exp-theor)/theor)*100

#data of experimentalMap is put into an array called map
file = open("experimentalMap.csv",encoding='utf-8-sig')
map=file.readlines()
file.close()

#turning string array of lines into 2d float array
for i in range(21):
    map[i]=map[i].strip()
    map[i]=map[i].split(',')
    for j in range(len(map[i])):
        map[i][j]=float(map[i][j])

actual = copy.deepcopy(map)

#points are the nodes of charge (x,y,q)
points=[[12,14,-1],[16,14,-1],[12,6,-1],[16,6,-1],[9,10,1],[19,10,1]]

#calculating theoretical voltage for each coordinate
for i in range(21): # i is row, j is col
    for j in range(29):
        actual[i][j]=0
        for point in points:
            if (not((i==14 and j==12) or (i==14 and j==16)
                    or (i==6 and j==12) or (i==6 and j==16)
                    or (i==10 and j==9) or (i==10 and j==19))):
                actual[i][j]+=volt(point[2],j,i,point) #(j,i)=(x,y)

#replacing values of 0 with -200 and 200
for i in range(21):
     for j in range(29):
        actual[i][j] = round(actual[i][j],2)
        if(actual[i][j]==0): 
            if(i==10): actual[i][j]=200
            else: actual[i][j]=-200
        
#uploading theoretical map to csv
file = open("theoreticalMap.csv","w")
for i in range(21):
    for j in range(29):
        file.write(str(actual[i][j]))
        if(j!=28): file.write(",")
    file.write("\n")
file.close()


#normalizing theoretical map
actualNorm=copy.deepcopy(actual)
for i in range(21):
    for j in range(29):
        actualNorm[i][j]=round(actual[i][j]/40+5,2)

#uploading normalized theoretical map to csv
file = open("theoreticalMapNorm.csv","w")
for i in range(21):
    for j in range(29):
        file.write(str(actualNorm[i][j]))
        if(j!=28): file.write(",")
    file.write("\n")
file.close()

#calculating percent error
sum=0
for i in range(21):
    for j in range(29):
        if(actualNorm[i][j]!=0): 
            sum=sum+error(map[i][j],actualNorm[i][j])
avgError=sum/(21*29)
print(avgError)