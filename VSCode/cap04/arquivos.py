import os
script_dir = os.path.dirname(__file__)
#print(script_dir)
arq1 = open(script_dir+"/arquivos/arquivo1.txt", "r")
print(arq1.read())

