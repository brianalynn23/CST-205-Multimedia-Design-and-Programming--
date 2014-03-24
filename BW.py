def BW():
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
      
  repaint (pic)