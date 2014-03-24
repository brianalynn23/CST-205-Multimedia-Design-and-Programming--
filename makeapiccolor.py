
#This is how you turn a picture blue


def makeBlue():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    setRed(p, r * .2)
    setGreen(p, g * .2)
  repaint(pic)

#This is how you give an image a red filter.  

def makeRed():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    b = getBlue(p)
    g = getGreen(p)
    setBlue(p, b * .2)
    setGreen(p, g * .2)
  repaint(pic)
  
#This is how you give an image a green filter.

def makeGreen():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    setRed(p, r * .2)
    setBlue(p, b * .2)
  repaint(pic)
