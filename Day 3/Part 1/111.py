file = open('input.txt','r')
lst = list(file.readlines())
count_1, count_0 = '', ''
gamma, epsilon = '', ''
for i in range(len(lst[0]) - 1):
    for j in lst:
        if j[i] == '1':
            count_1 += j[i]
        else:
            count_0 += j[i]
    count_11 = count_1.count('1')
    count_00 = count_0.count('0')
    if count_11 > count_00:
        gamma += '1'
    elif count_11 < count_00:
        gamma += '0'
    count_1 = ''
    count_0 = ''
for lst2 in gamma:
    if lst2 == '1':
        epsilon += '0'
    else:
        epsilon += '1'
gamma = int(gamma, base=2)
epsilon = int(epsilon, base=2)
answer = gamma * epsilon
print(answer)
