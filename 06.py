# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    string = input()
    even = ""
    odd = ""

    for i in range(len(string)):
        if i % 2 == 0:
            even += str(string[i])
        else:
            odd += str(string[i])

    print("{} {}".format(even, odd))
