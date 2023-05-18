
# sourceFile = "H:\Projects\SafeTranferData\Data\Fol_1\\backAl.py"
# destFile   = "H:\Projects\SafeTranferData\Data\Fol_2\\"


import os


source = "H:\Projects\SafeTranferData\Data\Admin"
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
            