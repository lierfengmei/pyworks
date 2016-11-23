
"makeTextFile.py -- create text file"

import os
ls = os.linesep

#get filename

while True:
    fname = input("Please input filename:")
    if os.path.exists(fname):
        print("Error:'%s' already exists" % fname)
    else:
        break

#get line content(text) lines
all = []
print("\nEnter lines('.' by itself to quit).\n")

#loop until user terminates input
while True:
    entry = input('> ')
    if entry=='.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
try:
    with open(fname,'w') as fobj:
        fobj.writelines(['%s%s' % (x,ls) for x in all])
        fobj.close()
except IOError as err:
    print("File Error:",err)
