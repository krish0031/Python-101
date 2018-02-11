fname=input('Enter the filename:\n')
try:  
    fhand=open(fname)
    count = 0
    for line in fhand:
            if line.startswith('Subject:'):
                count+=1

            print("Enter a Valid File name")
    print("there are ", count, " 'Subjects' in the file")
except:
    print("enter a valid file name..!!")        