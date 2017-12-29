import numpy as np
import glob

#tweak it to check results during the process
dir = 'data/'
for file in glob.glob(dir + "*.npy"):
    item = np.load(file).item()
    print(item)
