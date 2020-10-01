# Question link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem/
# Code section:
def solve(dic, q):
    for k in q:
        if k in dic.keys():
            print("%s=%d"%(k,dic[k]))
        else:
            print("Not found")
    return

test = int(input())
phoneBook = {}
while test>0:
    name, number = input().strip().split()
    number = int(number)
    phoneBook[name] = number
    test -= 1
query = []
try: 
    while True: 
        inp = input()
        if inp != "":
            query.append(inp)
        else:
            break 
except EOFError: 
    solve(phoneBook, query)
