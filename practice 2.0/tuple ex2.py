# Get the distribution for hour of each email
# split the line that contains the time and seperate the hour part from the line
# count the number of instances of each hour and and print that data
fhand = open('mbox.txt')
l = list()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    else:
        #print(line)
        words = line.split()
        #print(words[5])
        delimiter = ':'
        time = words[5].split(delimiter)
        #print(time)
        l.append(time)
# count the number of occurances of each unique hour in the list

#print(l)
data = dict()
for element in l:
    hour=element[0]
    if hour in data:
        data[hour]+=1
    else:
        data[hour]=1
#print(data)
#sort the dictionary based on value
sortl = list()
for key,value in data.items():
    sortl.append((value,key))
#print(sortl)
sortl.sort(reverse=True)
finallist=sortl[:9]
#print(finallist)
for key,value in finallist:
    print(value,key)

    
