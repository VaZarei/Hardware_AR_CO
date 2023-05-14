import os
import shutil
import string
from threading import Thread
import stat

source            = "H:\Projects\SafeTranferData\Data\Fol_1"
print("source: ", source)
clientDestination = "H:\Projects\SafeTranferData\Data\Fol_2"
adminDestination  = "H:\Projects\SafeTranferData\Data\\Admin"

allowExtentions       = ["jpg", "txt", "pdf", "rar", "bmp", "accdb"]
incpectionExtentions  = ["exe", "py", "mp4", "ini"]
forbiddenExtentions   = ["mp3"]


adminAllowPath       =  f"{adminDestination}\\AllowPathAdmin"  
adminInspectionPath  =  f"{adminDestination}\\InspectionPath"             # for Admin, Need to Inspection Then Send ...
adminforbiddenPath   =  f"{adminDestination}\\ForbiddenPath"              # for Admin, Forbiden To transfer
adminAll             =  f"{adminDestination}\\All"                        # for Admin, main Source to destinations appending ...

#print(*dir(os), sep="\n")
def copyComplete(source, target):
    # copy content, stat-info (mode too), timestamps...
    shutil.copy2(source, target)
    # copy owner and group
    st = shutil.stat(source)
    shutil.chown(target, st.st_uid, st.st_gid)


def getCopyError(func):
    try:
       return func
    except:
       
       print("\nWarning:\n       ----------------------------------------------  >   Please Close all Files Running")
       return None
                     
def filterCopy(source, destination, ExtentionsList):

     
   filesPath       = []
   filesName       = []
   filesExtentions = []
  
   
   for root, dirs, files in os.walk(source):
          for file in files:
               
               filesPath.append(os.path.join(root,file))
               filesName.append(file)
               loc = file.find(".")
               filesExtentions.append(file[loc+1:])


   
   for index, files in enumerate(filesName) :
       
      #print("file: ", files)
      sourcFilepath = filesPath[index]
      #print("sourcFilepath:    ", sourcFilepath)
      filesize = os.path.getsize(sourcFilepath)
      #print("FileSize : ", round(filesize/1024/1024 , 2))


      destPath = sourcFilepath.replace(source, destination )
      #print("destPath        : ", destPath)
      destFolderPath = destPath.replace(files, "")
      #print("destFolderPath :  ",destFolderPath)


      #os.makedirs(destFolderPath , exist_ok= True)
      
      
      loc = files.find(".")
      if len(ExtentionsList) == 0 : 
         os.makedirs(destFolderPath , exist_ok= True)
         try:
             
            #copyComplete(sourcFilepath, destPath) 
            #  source_file      = open(sourcFilepath, 'rb')
            #  destination_file = open(destPath, 'wb')
            #  shutil.copyfileobj(source_file, destination_file)

             #shutil.copystat(sourcFilepath , destPath, follow_symlinks=True )
             Thread(target=shutil.copy2, args=[sourcFilepath , destPath]).start()
         except PermissionError:
             print("NONE - ---------------------------------------------------")
   
            
      else:
          for i in range(len(ExtentionsList)):
            if files[loc+1:] == ExtentionsList[i] :
                os.makedirs(destFolderPath , exist_ok= True)
                try:
                    
                  #copyComplete(sourcFilepath, destPath) 
                  #   source_file      = open(sourcFilepath, 'rb')
                  #   destination_file = open(destPath, 'wb')
                  #   shutil.copyfileobj(source_file, destination_file)

                   #shutil.copystat(sourcFilepath , destPath, follow_symlinks=True )
                   Thread(target=shutil.copy2, args=[sourcFilepath , destPath]).start()
                except PermissionError:
                    print("NONE - ---------------------------------------------------")



   return True , print("Copy To Destination is Done : " , destination)




## Admin Section _________________________________________________________________________________________________________##
    
filterCopy(source, adminAll, [])
filterCopy(adminAll, adminInspectionPath, incpectionExtentions)
filterCopy(adminAll, adminforbiddenPath , forbiddenExtentions)



## Client Section _________________________________________________________________________________________________________##


getCopyError(filterCopy(source, clientDestination, allowExtentions))

