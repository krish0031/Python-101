from audioop import avg
fhand = open('mbox.txt')

count=0
sum=0
fpoint=None

for line in fhand:
    line = line.rstrip()
    if line.find('X-DSPAM-Confidence:')==-1:
        continue
    else:
        count=count+1
        fpoint = line.find(' ')
        spconf = float(line[fpoint+1:])
        sum=sum+spconf
avg = sum/count
print("Average spam Confidence:", avg)
        
        