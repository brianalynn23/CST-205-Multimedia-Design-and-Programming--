#This is how you turn an image into a black and white filter with line drawing.

def lineDrawing():
  filename = pickAFile()
  pic = makePicture(filename)
  pc2 = BetterBnW(pic)
  ln = makeEmptyPicture(getWidth(pic), getHeight(pic))
  px = getPixels(pic)
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      if (x == getWidth(pic)-1) and (y == getHeight(pic)-1):
        right = getColor(getPixel(pic, x, y))
        down = getColor(getPixel(pic, x, y))        
      else:
        right = getColor(getPixel(pic, x==x-1, y))
        down = getColor(getPixel(pic, x, y==y-1))
      
      c = getColor(getPixel(pic, x, y))
      c2 = getPixel(ln, x, y)

      if(distance(c, right) <= 150 and distance(c, down) <= 150):
        setColor(c2, white)
      else:
        setColor(c2, black)
  repaint (pic)
  
def BetterBnW(pic):
 filename = pickAFile()
 pic = makePicture(filename)
 pixels = getPixels(pic)
 for p in pixels:
   r = getRed(p)
   g = getGreen(p)
   b = getBlue(p)
   r = ((r * 0.299 + b + g)/3)
   g = ((r + b * 0.587 + g)/3)
   b = ((r + b + g * .114)/3)
   setRed(p, r)
   setGreen(p, g)
   setBlue(p, b)