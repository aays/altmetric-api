import os
import json
os.chdir('/Users/Ahmed/Downloads/export/1')
ourFiles = os.listdir()

for i in ourFiles:
    with open(i, 'r') as f:
        try:
            data = json.load(f)
        except:
            continue
        with open('results.txt', 'a') as file:
            try:
                file.write(i + ' - ' +
                           str(data['altmetric_score']['score']) +
                           '\n')
            except:
                continue
                
