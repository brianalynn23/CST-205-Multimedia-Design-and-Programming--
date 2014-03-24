#This program allows you to take an image, select what color you want to reserve, and then grayscale the remainder of the image. 


def grayScale(range):
  color = pickAColor()     #This allows the user to select any color they want to reserve in their image    
  picture = pickAFile()
  pic = makePicture(picture)
  for px in getPixels(pic): 
    myColor = getColor(px)
    if(distance(myColor, color) > range):    #This is how the color is reserved in an image
    
      Red = getRed(px)
      Green = getGreen(px)
      Blue = getBlue(px)
      Red = ((Red + Blue + Green)/3)
      Blue = ((Blue + Red + Green)/3)
      Green = ((Red + Blue + Green)/3)
    
      setRed(px, Red)
      setBlue(px, Blue)
      setGreen(px, Green)
  
  repaint(pic)
  

#This program allows you to reserve 2 colors in an image and grayscale the rest of the image
        


def grayScale2(range): 
  color1 = pickAColor()    #This allows the user to select the two colors he/she wants to reserve in their image
  color2 = pickAColor()
  picture = pickAFile()
  pic = makePicture(picture)
  for px in getPixels(pic): 
    myColor = getColor(px)
    if(distance(myColor, color1) > range and distance(myColor, color2) > range):   #By incorporating an "if, and" statement, this will allow the user to reserve the 2 colors they want
    
    
      Red = getRed(px)
      Green = getGreen(px)
      Blue = getBlue(px)
      Red = ((Red + Blue + Green)/3)
      Blue = ((Blue + Red + Green)/3)
      Green = ((Red + Blue + Green)/3)
    
      setRed(px, Red)
      setBlue(px, Blue)
      setGreen(px, Green)
  
  repaint(pic)
  
#This program allows you to save a manipulated image and save it to your desktop


def writeTwritePictureTo(empPic(picture):
  picture = pickAFile()
  pic = makePicture(picture)
  requestString()
 
  writePictureTo(picture, file)