count = 0
file = open('input.txt','r')
lst = list(map(int, file.readlines()))
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        count += 1
print(count)
file.close()
