import os
import shutil
from datetime import date

entries = os.scandir(r"D:\testeFiles/teste.txt")


origin = r"D:\testeFiles/"
dst = r"D:\bkpTeste/"

for entry in entries:
    print(entry.name)
    file_copy = shutil.copy2((origin + entry.name),(dst + (entry.name.replace('.txt','') + '_' + str(date.today()) + '.txt')))
    