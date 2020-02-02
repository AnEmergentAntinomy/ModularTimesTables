import matplotlib.pyplot as plt
import math
import gif

pi = math.pi

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

# variables for generating tables
coeff = 0
radius = 1000
modulus = 360
itval = 0.01
end_c = 1
style = solid


# Sets up lists and table dimensions
def Setup(title,r):
    global points
    global locations
    global frames
    
    points = []
    locations = []
    frames = []
    
    fig, ax = plt.subplots(1, 1)
    ax.set_title(title)
    ax.set_aspect('equal')
    btm = -r - (r*0.05)
    top = r + (r*0.05)
    ax.set_xlim(btm, top)
    ax.set_ylim(btm, top)


# Checks which linestyle is used and returns as string
def StyleCheck(style):
    if style == solid:
        s = "solid"
    elif style == dot:
        s = "dot"
    elif style == dense_dot:
        s = "ddot"
    elif style == loose_dash:
        s = "ldash"
    elif style == dash:
        s = "dash"
    elif style == dense_dash:
        s = "ddash"
    elif style == loose_dashdot:
        s = "ldash"
    elif style == dashdot:
        s = "dashdot"
    elif style == dense_dashdot:
        s = "ddashdot"
    elif style == loose_dashdotdot:
        s = "ldashdotdot"
    elif style == dashdotdot:
        s = "dashdotdot"
    elif style == dense_dashdotdot:
        s = "ddashdotdot"
    return s


# Generates m points on a circle with radius r
def GeneratePoints(r,m):
    for x in range(0,m+1):
        pointx = math.cos(2*pi/m*x)*r
        pointy = math.sin(2*pi/m*x)*r
        points.append((pointx,pointy))


# Generates the numbers for each point for the modular multiplication
def GenerateLocations():
    x = 0
    for point in points:
        location = (x,point)
        locations.append(location)
        x += 1


# Generates modular times table with given coeff and solid lines by default
@gif.frame
def GenerateLines(c,m,style,live=False,show=False,dots=False):
    for n in range(m+1):
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
        if dots == True:
            pointx,pointy = loc
            plt.scatter(pointx,pointy,s=5)
        if live == True:
            plt.ylabel(str(place))
            plt.xlabel(str(mod_int))
            plt.pause(0.01)
    if show == True:
        plt.show()


# Generates frames for gif from current coefficient (c) to higher coefficient (l)
def TablesGif(c,m,i,e,style,dots):
    while c <= e:
        plt.axis('equal')
        plt.xlabel(str(c))
        frame = GenerateLines(c,m,style,dots=dots)
        frames.append(frame)
        print(c)
        c += i
        c = round(c,2)


# Shows a single modular times table
def ShowSingleTable(c,r,m,style=solid,live=True,dots=False):
    title = f"{c}mod{m} Times Table"
    Setup(title,r)
    GeneratePoints(r,m)
    GenerateLocations()
    GenerateLines(c,m,style,live,show=True,dots=dots)


# Animates modular times tables and saves as gif (depending on how far apart c and l are, this could take a while)
def AnimateTables(c,r,m,i,e,style=solid,dots=False):
    title = f"mod{m} Times Tables"
    Setup(title,r)
    GeneratePoints(r,m)
    GenerateLocations()
    TablesGif(c,m,i,e,style,dots)
    print("Building gif. . .")
    s = StyleCheck(style)
    name = f"modtables_({c}-{e})mod{m}_{s}.gif"
    gif.save(frames, name, duration=50)
    print(name + " complete.\n")



if __name__ == "__main__":
    ShowSingleTable(coeff,radius,modulus,style)
    AnimateTables(coeff,radius,modulus,itval,end_c,style)

    # Examples
    
##    ShowSingleTable(179,1000,360)
##    ShowSingleTable(179,1000,360,loose_dash)
    
##    AnimateTables(0,1000,360,0.01,10,style=dash,dots=True)
##    AnimateTables(0,100,360,0.01,10)
##    AnimateTables(0,1000,360,0.01,10,dash)
