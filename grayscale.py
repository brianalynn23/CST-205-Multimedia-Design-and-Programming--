def grayScale():
  picture = pickAFile()
  pic = makePicture(picture) 
  for px in getPixels(pic):
    
    luminance = ( getRed(px) + getBlue(px) + getGreen(px) )/3
    if luminance < 50:
      setColor(px, makeColor(50, 50, 50))
    elif luminance < 100:
      setColor(px, makeColor(100, 100, 100))
    elif luminance < 150:
      setColor(px, makeColor(200, 200, 200))
    else:
      setColor(px, white)
      
  return(pic)
    
def makeImage(grayScale):
  file = '/Users/brianalynncampbell/Pictures/Lotus-Flower-Grows-In-The-Mud.jpg'
  picture = makePicture(file)
  for px in getPixels(picture):
    color = getColor(px)
    if red is 253
      set red to 250 (or some other intermediate value)
    if green is 221
      set green to 220 (or some other intermediate value)
      setColor(px, grayScale)
  show(picture)
  return(picture)