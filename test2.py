import os
import time

def monitorUSBStorage():
    label = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
    'T','U','V','W','X','Y','Z']
    monitorDisk = []
    for i in label:
        try:
            file = open(i+':/')
            print("------------------------------- > file: ", file)
        except Exception as e:
            '''
            error = 2  =>not found
            error = 13 =>permission denied (exist!)
            '''
            if(e.errno == 13):
                print("Disk : "+i+" Exist!")
            else:
                monitorDisk.append(i)



monitorUSBStorage()



# file = open('m'+':/')
# print("------------------------------- > file: ", file)