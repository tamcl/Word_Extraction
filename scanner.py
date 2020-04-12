import re
import string
import os

Names = []
path = 'input/'

for i in os.listdir(path):
    Names.append(i)

ignorepath = 'ignore.txt'
ignoreFile = open(ignorepath,'r')
ignore = ignoreFile.read().split('\n')

Error = ''
EN = 1
Word = {}
for a in string.ascii_lowercase:
    Word[a] = set()

for inputp in Names:
    file = open(path+inputp,'r')
    raw = file.read()
    filt = re.sub(r"""
               [,.;@#?!&$‘()=+“”:'’]+  # Accept one or more copies of punctuation
               \ *           # plus zero or more copies of a space,
               """,
               " ",          # and replace it with a single space
               raw, flags=re.VERBOSE)
    filt = filt.replace("\n", " ").split(" ")
    count = 1
    for w in filt:
        e = w.lower()
        if len(e) > 0:
            #print(e[0])
            if e[0] in string.ascii_lowercase:
                if e not in ignore:
                    Word[e[0]].add(e)
            else:
                Error += 'Error word ({}) from : {} at word number {} \t(Error Number {})\n'.format(e, inputp, count, EN)
                EN+=1
        count += 1

filepath = 'output/'
for t in Word.keys():
    if len(Word[t]) > 0:
        filename = filepath
        filename += t
        filename +='.txt'
        f = open(filename,'w')
        output = ''
        for y in Word[t]:
            output+=y
            output+='\n'
        f.write(output)
open('Error.txt','w').write(Error)



