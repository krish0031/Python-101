import os
os.chdir('C:\\Users\krish\Desktop\Python')
fhand = open('mbox-short.txt')

d=dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):continue
    else:
        #print (line)
        words = line.split()
        
        pos =  words[1].find('@')+1
        for charc in words[1]:
            domain = words[1][pos:]   
        
            if domain in d:
                d[domain]+=1
            else:
                d[domain] = 1


print(d)




    
  
    
    
    # removing the extra punctuations: looping through each charecter of the word
    
    