n = int(input())
binary = bin(n)[2:]

count = 0
max_count = 0
for i in range(len(binary)):
    if int(binary[i]) == 0:
        count = 0
    else:
        count += 1
        max_count = max(max_count, count)

print(max_count)
