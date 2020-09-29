import re

gmail_regx = re.compile("^[a-z\.]+@gmail.com$")
gmail_accounts = dict()

n = int(input())
for _ in range(n):
	first_name, email = input().split(' ')
	if gmail_regx.match(email):
		gmail_accounts[email] = first_name

sorted_gmail = sorted(gmail_accounts.values())
for name in sorted_gmail:
	print(name)