def makeBlue():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    setRed(p, r * .5)
    setGreen(p, g * .5)
  repaint(pic)
  
#This is how you tint a picture blue
  
def grayScale():
  picture = pickAFile()
  pic = makePicture(picture)
  for px in getPixels(pic): 
    
    Red = getRed(px)
    Green = getGreen(px)
    Blue = getBlue(px)
    Red = ((Red *.15 + Blue + Green)/3)
    Blue = ((Blue + Red *.114 + Green)/3)
    Green = ((Red + Blue + Green *.587)/3)
    
    setRed(px, Red)
    setBlue(px, Blue)
    setGreen(px, Green)
  
  repaint(pic)
  
#This is how you turn a picture to a grayscale