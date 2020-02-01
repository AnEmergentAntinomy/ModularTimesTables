import matplotlib.pyplot as plt
import math
import gif

pi = math.pi
points = []
locations = []
frames = []
modulus = 360
radius = 1
coeff = 0.00

fig, ax = plt.subplots(1, 1)
ax.set_aspect('equal')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)


# linestyles
solid = "-"
loose_dot = (0, (1, 10))
dot = ":"
dense_dot = (0, (1, 1))
loose_dash = (0, (5, 10))
dash = "--"
dense_dash = (0, (5, 1))
loose_dashdot = (0, (3, 10, 1, 10))
dashdot = "-."
dense_dashdot = (0, (3, 1, 1, 1))
loose_dashdotdot = (0, (3, 10, 1, 10, 1, 10))
dashdotdot = (0, (3, 5, 1, 5, 1, 5))
dense_dashdotdot = (0, (3, 1, 1, 1, 1, 1))


# Generates m points on a circle with radius r
def GeneratePoints(r,m):
    for x in range(0,m+1):
        pointx = math.cos(2*pi/m*x)*r
        pointy = math.sin(2*pi/m*x)*r
        points.append((pointx,pointy))


# Generates the numbers for each point for the modular multiplication with option to plot points
def GenerateLocations(plot=False):
    x = 0
    for point in points:
        if plot == True:
            pointx,pointy = point
            plt.scatter(pointx,pointy,s=5)
        location = (x,point)
        locations.append(location)
        x += 1


# Generates Modular Times Table with given coeff and solid lines by default
@gif.frame
def GenerateLines(c,m,style,live=False,show=False):
    for n in range(m):
        point = locations[n]
        place = point[0]
        loc = point[1]
        mod = (place * c) % m
        mod_int = int(mod)
        end_point = locations[mod_int]
        line_end = end_point[1]
        x = (loc[0],line_end[0])
        y = (loc[1],line_end[1])
        plt.plot(x,y,linestyle=style)
        if live == True:
            plt.pause(0.001)
    if show == True:
        plt.show()
            


# Generates frames for gif from current coefficient (c) to higher coefficient (l)
def Gif(c,m,l,style):
    while c < (l+0.01):
        plt.axis('equal')
        frame = GenerateLines(c,m,style)
        frames.append(frame)
        print(c)
        c += 0.01
        c = round(c,2)


# Shows a single times table
def ShowSingleTable(c,r,m,style=solid):
    GeneratePoints(r,m)
    GenerateLocations()
    GenerateLines(c,m,style,live=True,show=True)


# Animates modular times tables and saves as gif (depending on how far apart c and l are, this could take a while)
def AnimateTables(c,r,m,l,style=solid):
    GeneratePoints(r,m)
    GenerateLocations()
    Gif(c,m,l,style)
    gif.save(frames, "modmath.gif", duration=50)


if __name__ == "__main__":
    AnimateTables(coeff,radius,modulus,10)
##    ShowSingleTable(coeff,radius,modulus)
