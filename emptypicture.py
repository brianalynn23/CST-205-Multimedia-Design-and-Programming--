def makeEmptyPicture():
   picture = pickAFile() 
   pic = makePicture(picture)
   show(pic)   
   setAllPixelsToAColor(pic, green)
   show(pic)
   addText(pic, "hello")