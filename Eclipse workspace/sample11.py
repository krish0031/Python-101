fhand = open('mbox.txt')
d = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From ')==-1: continue
    else:
        delimiter = ' '
        words = line.split(delimiter)
        print(words)
        i=2
        for i in range(len(words)):        
            if words[2] not in d:
                d[words[2]]=1
            else:
                d[words[2]]=d[words[2]]+1
print('the list and the count are as follows:\n', d)