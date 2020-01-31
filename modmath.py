import matplotlib.pyplot as plt
import math
import gif

pi = math.pi
points = []
locations = []
frames = []
modulo = 360
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


# Generates n points on a circle with radius r
def GeneratePoints(r,n):
    for x in range(0,n+1):
        pointx = math.cos(2*pi/n*x)*r
        pointy = math.sin(2*pi/n*x)*r
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
def GenerateLines(c,style,live=False):
    for n in range(modulo):
        point = locations[n]
        place = point[0]
        loc = point[1]
        mod = (place * c) % modulo
        mod_int = int(mod)
        end_point = locations[mod_int]
        line_end = end_point[1]
        x = (loc[0],line_end[0])
        y = (loc[1],line_end[1])
        plt.plot(x,y,linestyle=style)
        if live == True:
            plt.pause(0.001)


# Generates frames for gif from current coefficient (c) to higher coefficient (l)
def Gif(c,l,style):
    while c < l:
        plt.axis('equal')
        frame = GenerateLines(c,style)
        frames.append(frame)
        print(c)
        c += 0.01
        c = round(c,2)


# Shows a single times table
def ShowSingleTable(c,r,n,style=solid):
    GeneratePoints(r,n)
    GenerateLocations()
    GenerateLines(c,style,live=True)
    plt.show()


# Animates modular times tables and saves as gif
def AnimateTables(c,r,n,l,style=solid):
    GeneratePoints(r,n)
    GenerateLocations()
    Gif(c,l,style)
    gif.save(frames, "modmath.gif", duration=100)


if __name__ == "__main__":
    AnimateTables(coeff,radius,modulo,100)
##    ShowSingleTable(coeff,radius,modulo)
