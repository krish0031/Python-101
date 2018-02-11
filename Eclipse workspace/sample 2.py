fhand =open('mbox.txt')
for line in fhand:
    line=line.rstrip()
    if line.find('@uct.ac.za):
        print(line)