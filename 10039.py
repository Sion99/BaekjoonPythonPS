
sum = 0
for i in range(1,6):
    j = int(input())
    if j < 40:
        sum = sum + 40
    else:
        sum = sum + j

average = int(sum / 5)
print(average)

