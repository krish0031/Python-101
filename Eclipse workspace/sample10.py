fhand = open('mbox.txt')
d = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From ')==-1: continue
    else:
        delimiter = ' '
        words = line.split(delimiter)
        print(words)
        print(words[2])
        
        k = words[2]
        if k not in d:
            d[k]=1
        else:
            d[k]=d[k]+1
print('the list and the count are as follows:\n', d)