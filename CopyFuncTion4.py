import os
import time

flash_address =  "r:"


source            = flash_address #"H:\Projects\SafeTranferData\Data\Fol_1"
clientDestination = "H:\Projects\SafeTranferData\Data\Fol_2"
adminDestination  = "H:\Projects\SafeTranferData\Data\Admin"


allowExtentions       = ["jpg", "txt", "pdf", "rar", "bmp", "accdb"]
incpectionExtentions  = ["exe", "py", "mp4", "ini"]
forbiddenExtentions   = ["mp3", "py"]


adminAllowPath       =  f"{adminDestination}\\AllowPathAdmin\\"  
adminInspectionPath  =  f"{adminDestination}\\InspectionPath\\"             # for Admin, Need to Inspection Then Send ...
adminforbiddenPath   =  f"{adminDestination}\\ForbiddenPath\\"              # for Admin, Forbiden To transfer
adminAll             =  f"{adminDestination}\\All\\"                        # for Admin, main Source to destinations appending ...





def check_flash(flash_address):
    i = 0
    try:
      for files in os.listdir(flash_address) :
        i+=1
      return i

    except FileNotFoundError :
       return i

def getCopyError(func):
    try:
       return func
    except:
       
       print("\nWarning:\n       ----------------------------------------------  >   Please Close all Files Running")
       return None
    
def xcopyFile(source, destination):
    
        os.system(f'"cmd.exe /c xcopy "{source}" "{destination}" /s /d /y /e /x /v /k /I "')    #/s /d /y /e /x /v /k /I

def removeEmptyFolder(source):
    
    for root, dirs, files in os.walk(source):
        
        print("File :", files)
        print("Dirs :", dirs)
        print("---------")
        
   

  
    pass  

removeEmptyFolder(adminDestination)

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




while True : 
   
   if check_flash(flash_address) > 1000 :


      ## Admin Section _________________________________________________________________________________________________________##
         
      filterCopy(source, adminAll, [])
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
