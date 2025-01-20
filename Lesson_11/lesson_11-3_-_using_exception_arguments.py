try:
   infile = open('dataFile.txt', 'r')
   infile.write("hello")

   infile.close()
except IOError as ioe:
   print ("filename:", ioe.filename)
   print ("strerror:", ioe.strerror)
