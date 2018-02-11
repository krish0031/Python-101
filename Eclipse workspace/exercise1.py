from audioop import avg
fhand = open('mbox.txt')

count=0
sum=0
fpoint=None

for line in fhand:
    if line.find('X-DSPAM-Confidence:'):
        print(line)
        fpoint=line.find('X-DSPAM-Confidence:')+19
        print(fpoint)
        spconf = int(line[fpoint:fpoint+7])
        sum=sum+spconf
        count+=1
avg=sum/count
print("the avg spam confidence is: ",avg)
    

    