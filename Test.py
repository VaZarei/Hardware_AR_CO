open("ctrlFile", "w")

import os

source = "H:\Projects\SafeTranferData\Data\Fol_2"
findFile = 0
for i in os.listdir(source) :

    extention = (i.find("."))
    if extention == -1 :
        for j in os.listdir(source + "\\" + i):
            findFile+=1
    
        findFile = 0   
        if findFile == 0:
         
            open(f'{source}\\{i}\\Safe_Transfer.txt', "w")
