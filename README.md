# ModularTimesTables
Python script for generating modular times tables with matplotlib and gif

Usage Tips:

the variables at the top (coeff,radius,modulus) make it simpler to change those values while experimenting with single tables

ShowSingleTable(c,r,n,style=solid) will plot out a single table line by line

AnimateTimesTables(c,r,n,l,style=solid) will produce times tables and put each one as an individual frame in a gif

    c (the coefficient) is the number to multiply by
    r (the radius) determines the size of the circle
    n (the modulus) is the amount of points on the circle
    l (the end coefficient) determines how many frames will be in the gif
    style is the style of line to use (solid,dot,dash,loose_dash,dashdot,etc.)


Examples:
  c       n
  179 mod 360 (something neat happens when the coefficient is (modulus/2)-1, try these two examples and see the difference
  
    ShowSingleTable(179,1,360)
    ShowSingleTable(179,1,360,loose_dash)
  
  
  Other neat patterns are:
    
    41 mod 360, 36 mod 360, 90 mod 360, 180 mod 360, 270 mod 360, 269 mod 360
