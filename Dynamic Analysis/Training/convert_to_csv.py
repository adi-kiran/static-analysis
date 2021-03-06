#
# MOVE FILE OUTSIDE DATASET DIRECTORY
#

from collections import Counter

import os
import pandas as pd
import numpy as np

directory = os.path.join('.', 'Dataset')

for root, dirs, files in os.walk(directory, topdown=False):
    for name in files:
        path = os.path.join(root, name)
        # print(path)
        with open(path, 'r') as f:
            s = f.read()
        seq = s.strip().split(" ")
        seq = list(map(int, seq))
        count = Counter(seq)   
        df = pd.DataFrame.from_dict(count, orient='index').reset_index()
        df = df.rename(columns={'index':'syscall', 0:'count'})
        new_name = name.strip('txt') + 'csv'
        csv_path = os.path.join(root,'csv', new_name)
        # print(csv_path)
        df.to_csv(csv_path, index=False)

