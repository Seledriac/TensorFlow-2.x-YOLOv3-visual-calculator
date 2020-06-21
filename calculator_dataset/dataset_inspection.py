# This script inspects the dataset directory

import os
path = 'calculator_dataset/dataset/train'
liste = os.listdir(path)
listops = ['d','x','+','-'] + list(range(10))
for eltops in listops:
    eltops = str(eltops)
    listo = [elt for elt in liste if elt[0] == eltops]
    print(eltops, ": nb elts = ", len(listo))