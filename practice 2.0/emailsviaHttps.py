import urllib.request, urllib.parse, urllib.error

url = 'http://www.pr4e.org/code3/mbox.txt'
data = urllib.request.urlopen(url)
fhand = open('mboxweb.txt','wb')
size = 0
while True:
    info = data.read(1000)
    if len(info)<1:
        break
    else:
        size = size+len(info)
        decinfo = info.decode()
        fhand.write(info)
print(size)
print(fhand)
fhand.close()
mbox = open('mboxweb.txt')
cont = mbox.read()
for line in cont:
    line = line.rstrip()
    line.split()
    print(line)
