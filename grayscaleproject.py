def grayScale(picture):
  for px in getPixels(picture): # [px1, px2, px3 ...]
    
    Red = getRed(px)
    Green = getGreen(px)
    Blue = getBlue(px)
    
    grey = (Red + Green + Blue) / 3
    
    greyColor = makeColor(grey , grey , grey)
    setColor(px, greyColor)
  
  return picture