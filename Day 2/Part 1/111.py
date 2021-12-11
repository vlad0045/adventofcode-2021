file = open('input.txt','r')
lst = list(file.readlines())
x = 0
y = 0
for direction in lst:
    if 'forward' in direction:
        num = int(direction.split(' ')[-1])
        x += num
    elif 'up' in direction:
        num = int(direction.split(' ')[-1])
        y -= num
    elif 'down' in direction:
        num = int(direction.split(' ')[-1])
        y += num
print(x * y)
file.close()

