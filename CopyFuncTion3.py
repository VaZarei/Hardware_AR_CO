import os
import shutil
import string
from threading import Thread
import stat

source            = "H:\Projects\SafeTranferData\Data\Fol_1"
clientDestination = "H:\Projects\SafeTranferData\Data\Fol_2"
adminDestination  = "H:\Projects\SafeTranferData\Data\Admin"


allowExtentions       = ["jpg", "txt", "pdf", "rar", "bmp", "accdb"]
incpectionExtentions  = ["exe", "py", "mp4", "ini"]
forbiddenExtentions   = ["mp3", "py"]


adminAllowPath       =  f"{adminDestination}\\AllowPathAdmin"  
adminInspectionPath  =  f"{adminDestination}\\InspectionPath"             # for Admin, Need to Inspection Then Send ...
adminforbiddenPath   =  f"{adminDestination}\\ForbiddenPath"              # for Admin, Forbiden To transfer
adminAll             =  f"{adminDestination}\\All"                        # for Admin, main Source to destinations appending ...





def getCopyError(func):
    try:
       return func
    except:
       
       print("\nWarning:\n       ----------------------------------------------  >   Please Close all Files Running")
       return None
    
def xcopyFile(source, destination):
    
    os.system(f'"cmd.exe /c xcopy "{source}" "{destination}"    /y /o /k /I "')



    
                     
def filterCopy(source, destination, ExtentionsList):

     
   filesPath       = []
   filesName       = []
   filesExtentions = []
  
   
   for root, dirs, files in os.walk(source):
          for file in files:
               #print("loop 1")
               filesPath.append(os.path.join(root,file))
               filesName.append(file)
               loc = file.find(".")
               filesExtentions.append(file[loc+1:])


   
   for index, files in enumerate(filesName) :
      #print("------------------------------------------------------------------------------------------------------------------------INdex: ", index)
      sourcFilepath = filesPath[index]
      #print("sourcFilepath: " , sourcFilepath)
      
      #filesize = os.path.getsize(sourcFilepath)
      


      destFilePath = sourcFilepath.replace(source, destination )
      destFolderPath = destFilePath.replace(files, "")
      destFolderPath = destFolderPath
      #print('destFolderPath:', destFolderPath)


      
  
      loc = files.find(".")

      #print("Source: ", sourcFilepath, "Destination: ", destFilePath)

      if len(ExtentionsList) == 0 : 
             xcopyFile(sourcFilepath, destFolderPath)
             #os.system(f'"cmd.exe /c xcopy {sourcFilepath} {destFolderPath}  /s /y /e /x /v /k /I "')  
             
      else:
          for i in range(len(ExtentionsList)):
            if files[loc+1:] == ExtentionsList[i] :
      
                   #os.system(f'"cmd.exe /c xcopy {sourcFilepath} {destFolderPath}  /s /y /e /x /v /k /I "')  
                   xcopyFile(sourcFilepath, destFolderPath)





## Admin Section _________________________________________________________________________________________________________##
    
filterCopy(source, adminAll, [])
filterCopy(source, adminInspectionPath, incpectionExtentions)
filterCopy(source, adminforbiddenPath,  forbiddenExtentions)



## Client Section _________________________________________________________________________________________________________##


#getCopyError(filterCopy(source, clientDestination, allowExtentions))

