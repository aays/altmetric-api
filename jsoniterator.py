'''
A simple script that goes through all the .json files in a directory, 
and then writes the Altmetric scores for each to a single text file.

Created by: Ahmed + the Earl Haig BDC teams
14/11/2016
'''

import os
import json
os.chdir('')
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
                
