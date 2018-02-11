import os
fhand = open('mbox.txt')
print(fhand)


count=0
for line in fhand:
    line=line.rstrip()
   
    if line.find('@uct.ac.za'):
        print(line)
        count+=1
print(count)

help(line.rstrip)
