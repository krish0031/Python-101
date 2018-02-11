fman = open('words.txt')
t=[]
d=dict()
for line in fman:
    line = line.lower()
    t = line.split()
    i=0
    for word in t:
        if word not in d:
            d[word] = 1
        else:
            d[word] = d[word] +1
lst = list(d.keys())
for key in d:
    if d[key]>3:
        print(key,d[key])
