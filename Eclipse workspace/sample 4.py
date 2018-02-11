fname = 'ghost.txt'
fhand = open(fname,'w')
print(fhand)

line1="I'm awesome\n"
fhand.write(line1)
print(fhand)

fhand.close()
