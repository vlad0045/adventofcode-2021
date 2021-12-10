count = 0
file = open('input.txt','r')
lst = list(map(int, file.readlines()))
sum1 = lst[0] + lst[1] + lst[2]
for i in range(1, len(lst) - 2):
    sum2 = lst[i] + lst[i + 1] + lst[i + 2]
    if sum1 < sum2:
        count += 1
    sum1 = sum2
print(count)
file.close()
