from copyFS import *
from arduinoFS import *
from timeFS import *
from definitionsFS import *

import os
import time
import shutil



def getCopyError(func):
    try:
       return func
    except:
       
       print("\nWarning:\n       ----------------------------------------------  >   Please Close all Files Running")
       return None
    
def xcopyFile(source, destination):
    
        os.system(f'"cmd.exe /c xcopy "{source}" "{destination}" /s /d /y /e /x /v /k /I "')    #/s /d /y /e /x /v /k /I

def deleteEmptyFolders(source) :

    emptyFolderAddress = []
    for root, dirs, files in os.walk(source):

        if len(files) == 0 and len(dirs) == 0 :
            emptyFolderAddress.append(root)


    while len(emptyFolderAddress) > 0 :
        #print("emptyFolders :", emptyFolderAddress)
        for i in emptyFolderAddress :
            try:
                    os.removedirs(i)
            except :
                    print("Cant Delete, May be folder in use or not empty !")
        emptyFolderAddress = []

        for root, dirs, files in os.walk(source):

                if len(files) == 0 and len(dirs) == 0 :
                    emptyFolderAddress.append(root)



    print("Done")
    
def filterCopy(source, destination, ExtentionsList):

     
   filesPath       = []
   filesName       = []
   filesExtentions = []
  
   
   for root, dirs, files in os.walk(source):
          for file in files:
               #print("file:", file)
               filesPath.append(os.path.join(root,file))
               filesName.append(file)
               loc = file.find(".")
               filesExtentions.append(file[loc+1:])


   
   for index, files in enumerate(filesName) :
      #print("------------------------------------------------------------------------------------------------------------------------INdex: ", index)
      sourcFilepath = filesPath[index]
      destFilePath = sourcFilepath.replace(source, destination )
      destFolderPath = destFilePath.replace(files, "")
      destFolderPath = destFolderPath
      
  
      loc = files.find(".")

      if len(ExtentionsList) == 0 : 
             xcopyFile(sourcFilepath, destFolderPath)
            
             
      else:
          for i in range(len(ExtentionsList)):
            if files[loc+1:] == ExtentionsList[i] :
                   xcopyFile(sourcFilepath, destFolderPath)

      
   deleteEmptyFolders(destination)








# --------------------------------------





while True : 
   
   if check_flash(flash_address) > 0 :


      ## Admin Section _________________________________________________________________________________________________________##
         
      #filterCopy(source, adminAll, [])
      filterCopy(source, adminInspectionPath, incpectionExtentions)
      filterCopy(source, adminforbiddenPath,  forbiddenExtentions)
     

      ## Client Section _________________________________________________________________________________________________________##


      #getCopyError(filterCopy(source, clientDestination, allowExtentions))
      break
   
   
   else :
      print("Flash is Unplug . . .     !")
      time.sleep(2)
      
      val = input("Trying to coonect to Flash   ,    if you want to quit please write 'q' and if you want to continue write 'c' :")
      if val == 'q' :
          break   

      if val == 'c' :
          pass   








val = input("Delete all ?  (y / n):")

if val == "y" :
    
    os.system(f"rd /s /q H:\Projects\SafeTranferData\Data\\Admin")
    
    

if val == "n" :
    
    pass
