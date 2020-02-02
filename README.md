# ModularTimesTables
Python script for generating modular times tables with matplotlib and gif
    

Usage Tips:

the variables at the top (coeff,radius,modulus,itval,end_c,style) make it simpler to change those values while experimenting

ShowSingleTable(c,r,m,style=solid,live=True,dots=False) will plot out a single table line by line
  the left number shows the current number (place), the bottom number shows place multiplied by c in mod m
    live can be set to false to just print the final image

AnimateTables(c,r,m,i,e,style=solid,dots=False) will produce times tables and put each one as an individual frame in a gif
  this will print out the coefficient as it builds the tables and then export a gif in the current directory

    c (the coefficient) is the number to multiply by
    r (the radius) determines the size of the circle
    m (the modulus) is the amount of points on the circle
    i (the iteration value) is the amount c changes each frame
    e (the end coefficient) determines how many frames will be in the gif

    style is the style of line to use ("solid","dot","dash","loose_dash","dashdot",etc.)
      if no style is given it will default to solid
    dots can be set to True to plot the points of the circle


These examples are commented out and a default example is above them

Examples:

  179(c) mod 360(m) something neat happens when the coefficient is (modulus/2)-1, try these two examples and see the difference
  
    ShowSingleTable(179,1000,360)
    ShowSingleTable(179,1000,360,loose_dash)


  gif of tables in mod360(m) with radius of 1000(r) from 0(c) to 10(e) with c increasing by 0.01(i) each frame until it reaches e with dash lines and dots

    AnimateTables(0,1000,360,0.01,10,style=dash,dots=True)
  
  
  Other neat single patterns are:
    
    41 mod 360, 36 mod 360, 90 mod 360, 180 mod 360, 270 mod 360, 269 mod 360

