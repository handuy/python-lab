import os
import magic

for file in os.listdir("./"):
    if os.path.isfile(file):
        print(file)
        print( magic.from_file(file) )