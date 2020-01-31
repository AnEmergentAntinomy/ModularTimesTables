import matplotlib.pyplot as plt
import math

pi = math.pi
points = []
locations = []
modulo = 360
radius = 1
coeff = 90.0

fig, ax = plt.subplots(1, 1)
ax.set_aspect('equal')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

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

styles = [solid, loose_dot, dot, dense_dot, loose_dash, dash, dense_dash, loose_dashdot,
          dashdot, dense_dashdot, loose_dashdotdot, dashdotdot, dense_dashdotdot]

def GeneratePoints(r,n):
    for x in range(0,n+1):
        pointx = math.cos(2*pi/n*x)*r
        pointy = math.sin(2*pi/n*x)*r
        points.append((pointx,pointy))


def GenerateLocations(plot=False):
    x = 0
    for point in points:
        pointx,pointy = point
        if plot == True:
            plt.scatter(pointx,pointy,s=5)
        location = (x,point)
        locations.append(location)
        x += 1


def GenerateLines(style=solid,live=True):
    for n in range(modulo):
        n = n % modulo
        point = locations[n]
        place = point[0]
        loc = point[1]
        mod = (place * coeff) % modulo
        mod_int = int(mod)
        end_point = locations[mod_int]
        line_end = end_point[1]
        x = (loc[0],line_end[0])
        y = (loc[1],line_end[1])
        plt.plot(x,y,linestyle=style)
        if live == True:
            plt.pause(0.001)


def Main():
    GeneratePoints(radius,modulo)
    GenerateLocations()
    GenerateLines(style=loose_dash)
    plt.show()

if __name__ == "__main__":
    Main()
