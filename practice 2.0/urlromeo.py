import urllib.request,urllib.parse,urllib.error
host = 'http://data.pr4e.org/romeo-full.txt'
d=dict()
fhand = urllib.request.urlopen(host)
for line in fhand:
    line = line.decode().rstrip()
    words = line.split()
    for word in words:
        if word not in d:
            d[word]=1
        else:
            d[word]=d[word]+1
#print(d)

for key,value in d.items():
    print(key,value)