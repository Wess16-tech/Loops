n = int(input("enter a number whose sum you want to find: "))
sum = 0

for i in range(1, n+1):
    sum += i
    print("sum: ", sum )