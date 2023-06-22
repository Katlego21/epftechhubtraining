first = 0
second = 1
temp = 0
sum = 0
# numbers less than 4 000 000
while temp < 4000000:
    temp = first + second
    first = second
    second = temp
# calculate sum of even nums
    if temp % 2 ==0:
        sum = sum + temp

print(sum)