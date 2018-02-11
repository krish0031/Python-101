fname = input('Enter the file name:\n')
fman = open(fname)
t=[]
for line in fman:
    if line.startswith('From '):
        delimiter = " "
        t = line.split(delimiter)
        print(t[2:5])
        