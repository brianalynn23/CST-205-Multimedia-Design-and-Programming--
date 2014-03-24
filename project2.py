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
  file = pickAFile()
  writePictureTo(pic, file)    #This will allow the user to save their image to a file after the manipulation.


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
  file = pickAFile()
  writePictureTo(pic, file)    #This will allow the user to save their image to a chosen file after the manipulation.
  
  
#This program makes an image black and white.   
  
  
  
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
  file = pickAFile()
  writePictureTo(pic, file)    #This will allow the user to save their image to a chosen file after the manipulation.
 
   
  
#This program adds a red, blue negative effect to an image.


def redAndBlueEffect(): 
  file = pickAFile() 
  picture = makePicture(file)
  show(picture)
  for pixel in getPixels(picture):
    redValue = getRed(pixel)      #This is how the red value is created in the image. 
    newColor = makeColor( redValue, 0, 255 - redValue)    #by making it a negative red value, this will give it the negative effect.
    setColor(pixel,newColor)
  repaint(picture)
  file = pickAFile()    
  writePictureTo(picture, file)    #This will allow the user to save their image to a chosen file after the manipulation. 





  