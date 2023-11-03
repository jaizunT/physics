import matplotlib.pyplot as plt
from array import array
import numpy 
from IPython import display
from matplotlib.animation import FuncAnimation



from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#copy csv data to create Z array (theoretical data)
file = open("theoreticalMap.csv",encoding='utf-8-sig')

Z=file.readlines()
file.close()

for i in range(21):
    Z[i]=Z[i].strip()
    Z[i]=Z[i].split(',')
    for j in range(len(Z[i])):
        Z[i][j]=float(Z[i][j])
Z=numpy.array(Z)

#copy csv data to get ZNorm array (normalized theoretical data)
file = open("theoreticalMapNorm.csv",encoding='utf-8-sig')

ZNorm=file.readlines()
file.close()

for i in range(21):
    ZNorm[i]=ZNorm[i].strip()
    ZNorm[i]=ZNorm[i].split(',')
    for j in range(len(ZNorm[i])):
        ZNorm[i][j]=float(ZNorm[i][j])
ZNorm=numpy.array(ZNorm)

#copy csv data to get ZExp array (experimental data)

file = open("experimentalMap.csv",encoding='utf-8-sig')
ZExp=file.readlines()
file.close()

for i in range(21):
    ZExp[i]=ZExp[i].strip()
    ZExp[i]=ZExp[i].split(',')
    for j in range(len(ZExp[i])):
        ZExp[i][j]=float(ZExp[i][j])
ZExp=numpy.array(ZExp)

#create arrays for X,Y

def create(min, max)->list:     
    return list(range(min, max))
X = list(range(0,21))
Y = list(range(0,21))

for i in range(21):
    X[i]=create(0,29)
    Y[i]=[i]*29

#create plots
ax.plot_wireframe(X, Y, ZExp, rstride=1, cstride=1, color='red',label="Experimental Voltage Map")
ax.plot_wireframe(X, Y, ZNorm, rstride=1, cstride=1,label="Normalized Theoretical Voltage Map")
plt.legend(loc="upper left")


# Set the axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Rotate the axes and update
for angle in range(0, 360 + 1):
  
    azim = angle

    # Update the axis view and title
    ax.view_init(10, azim, 0)
    plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (10, azim, 0))
    plt.draw()
    plt.savefig(f'images/{angle:003}')
    plt.pause(.001)

