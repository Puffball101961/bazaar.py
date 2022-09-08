import json
import ast

f = open('ids.txt').read()

ids = ast.literal_eval(f)

for i in range(len(ids)):
    if ids[i][:6] != "ENCHAN":
        print(f'        "{ids[i]}": "{ids[i].lower().replace("_", " ")}",')
    
for i in range(len(ids)):
    if ids[i][:6] == "ENCHAN":
        print(f'        "{ids[i]}": "{ids[i].lower().replace("_", " ")}",')