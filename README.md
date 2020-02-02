# ModularTimesTables
Python script for generating modular times tables with matplotlib and gif

Usage Tips:

the variables at the top (coeff,radius,modulus,itval,length) make it simpler to change those values while experimenting

ShowSingleTable(c,r,m,style) will plot out a single table line by line

AnimateTimesTables(c,r,m,i,l,style) will produce times tables and put each one as an individual frame in a gif

    c (the coefficient) is the number to multiply by
    r (the radius) determines the size of the circle
    m (the modulus) is the amount of points on the circle
    i (iteration value) is the amount c changes each frame
    l (the end coefficient) determines how many frames will be in the gif
    style is the style of line to use (solid,dot,dash,loose_dash,dashdot,etc.)
      if no style is given it will default to solid


Examples:

  179(c) mod 360(m) something neat happens when the coefficient is (modulus/2)-1, try these two examples and see the difference
  
    ShowSingleTable(179,1,360)
    ShowSingleTable(179,1,360,loose_dash)


  gif of tables in mod360(m) with radius of 1(r) from 0(c) to 1(l) with c increasing by 0.01(i) each frame until it reaches l

    AnimateTimesTables(0,1,360,0.01,1)
  
  
  Other neat single patterns are:
    
    41 mod 360, 36 mod 360, 90 mod 360, 180 mod 360, 270 mod 360, 269 mod 360
