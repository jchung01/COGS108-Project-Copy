import numpy as np
import requests
# import io
# from pathlib import Path
import json
import zipfile


#Change include zip in same folder as this code to get wordcount
with zipfile.ZipFile("FinalProjects-Sp21-main.zip", "r") as f:
    for name in f.namelist():
        if '.ipynb' not in name:
            continue
        rf = json.loads(f.read(name))
        wordcount = 0
        for i, cell in enumerate(rf['cells']):
            if cell['cell_type'] == 'markdown':
                for string in cell['source']:   
                        try:
                            #converts string into list
                            words = string.split(" ")
                            
                            #remove non words
                            while('\n' in words):    
                                words.remove('\n')
                            while('#' in words):    
                                words.remove('#')
                            while('##' in words):    
                                words.remove('##')
                            while('###' in words):    
                                words.remove('###')
                            while('####' in words):    
                                words.remove('####')
                            while('-' in words):    
                                words.remove('-')    
                            
                            #check output if neccessary
                            #print(words)
                            
                            wordcount += len(words)
                            
                        except IndexError:
                            print("INDEXERROR", string)
                            
        print(name, wordcount)
        #print(name)
        #print(wordcount)
        #print(name + ',', wordcount) #CSV format
