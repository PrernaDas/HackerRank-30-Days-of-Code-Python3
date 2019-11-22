# Enter your code here. Read input from STDIN. Print output to STDOUT
phone_book = {}
n = int(input())
if n >= 1 and n <= 100000:
    # print(n)
    for i in range(n):
        entry = str(input())
        # print(entry)
        key = entry.split(' ')[0]
        value = entry.split(' ')[1]
        phone_book[key] = value
        # print(phone_book)
query=input()
while len(query) > 0:
    if query in phone_book:
        print(query+'='+phone_book[query])
    else:
        print('Not found')
    
    try:     
        query=input()
    except:
        break