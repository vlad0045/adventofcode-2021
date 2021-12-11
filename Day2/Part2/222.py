file = open('input.txt','r')
lst = list(file.readlines())
x = 0
purpose = 0
depth = 0

for direction in lst:
    if 'forward' in direction:
        num = int(direction.split(' ')[-1])
        depth += purpose * num
        x += num
        
    elif 'up' in direction:
        num = int(direction.split(' ')[-1])
        purpose -= num
    elif 'down' in direction:
        num = int(direction.split(' ')[-1])
        purpose  += num
print(x * depth)
file.close()

