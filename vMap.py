import math
import copy
def volt(q,x,y,point):
    return q/dist(x,y,point[0],point[1])

def dist(x1,y1,x2,y2):
    return math.sqrt((x1/100-x2/100)**2+(y1/100-y2/100)**2)

file = open("experimentalMap.csv",encoding='utf-8-sig')

map=file.readlines()

file.close()

for i in range(21):
    map[i]=map[i].strip()
    map[i]=map[i].split(',')
    for j in range(len(map[i])):
        map[i][j]=float(map[i][j])

actual = copy.deepcopy(map)
points=[[12,14,-1],[16,14,-1],[12,6,-1],[16,6,-1],[9,10,1],[19,10,1]]

for i in range(21): # i is row, j is col
    for j in range(29):
        actual[i][j]=0
        for point in points:
            if (not((i==14 and j==12) or (i==14 and j==16)
                    or (i==6 and j==12) or (i==6 and j==16)
                    or (i==10 and j==9) or (i==10 and j==19))):
                actual[i][j]+=volt(point[2],j,i,point) #(j,i)=(x,i)

for i in range(21):
     for j in range(29):
          actual[i][j] = round(actual[i][j],2)

print(actual)
print(map)

file = open("theoreticalMap.csv","a")
for row in actual:
    for col in row:
        file.write(str(col))
        file.write(",")
    file.write("\n")
file.close()
