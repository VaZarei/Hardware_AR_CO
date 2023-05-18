import os, shutil
import time


input = input("Write Destination : ")
print("We Copy them to your specific Folder: ", input)
time.sleep(5)

shutil.copytree('H:\Projects\SafeTranferData\Data\Fol_1', input , dirs_exist_ok=True)
