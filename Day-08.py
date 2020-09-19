# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = {}
for _ in range(n):
    name, number = map(str, input().split())
    phone_book[name] = int(number)

try:
    while True:
        query = input()
        if query != "":
            if query in phone_book.keys():
                print("{}={}".format(query, phone_book[query]))
            else:
                print("Not found")
        else:   
            break
except EOFError: 
    pass

