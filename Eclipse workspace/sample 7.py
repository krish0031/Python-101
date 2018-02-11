fhand = open('mbox.txt')
t=[]
for line in fhand:
    t = line.split()
    #print('Debug:',t)
    if len(t)==0: 
        continue
    if t[0] != 'From ':
        continue
    else:
        print(t[1])