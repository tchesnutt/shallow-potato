import os

from utils import RAW_DATA_LOC


for filename in os.listdir(RAW_DATA_LOC):
    cleanFilename = filename.replace("_", "")
    print(os.getcwd())
    os.rename(RAW_DATA_LOC + filename, RAW_DATA_LOC + cleanFilename)
