# fractals

Step one of "Make it work, make it right, make it fast". :grin:

Just playing with Bokeh Server.

### File Info:

  Three points:

  * fractal3.py
  
    [Sierpinksi Triangle](https://en.wikipedia.org/wiki/Sierpinski_triangle) generated via [Chaos Game](https://en.wikipedia.org/wiki/Chaos_game) with [Bokeh Server](https://bokeh.pydata.org/en/latest/docs/user_guide/server.html).
    
  The Sierpinski Triangle/Gasket chooses randomly from three points to create the fractal.  Using four points doesn't result in a fractal, so restrictions are needed:
    
  * fractal_restriction_1.py
    
    Restriction: Chosen target point (vertex) cannot be same as previously chosen point.
  
  * fractal_restriction_2.py
  
    Restriction: Chosen target point cannot be one point away, anti-clockwise, from previously chosen point.

  * fractal_restriction_3.py
  
    Restriction: Chosen target point cannot be two points away from previously chosen point.
