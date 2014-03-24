def shrink(original, factor):
   width = original.getWidth()
   height = original.getHeight()
   image = PythonImage(width / factor, height / factor)
   oldX = 0
   newX = 0
   while oldX < width - factor:
      oldY = 0
      newY = 0
      while oldY < height - factor:
         oldP = original.getPixel(oldX, oldY)
         newP = image.getPixel(newX, newY)
         newP.setRed(oldP.getRed())
         newP.setGreen(oldP.getGreen())
         newP.setBlue(oldP.getBlue())
         oldY += factor
         newY += 1
      oldX += factor
      newX += 1
   return image