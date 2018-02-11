print('Enter the list of numbers and type done when finished...!!\n')
t = list()
while True:
    inp = input()
    if inp == 'done':
        break
    value = int(inp)
    t.append(value)
big = max(t)
small = min(t)
print(t,'\n' 'max:',big,'\n','min:',small)
    
