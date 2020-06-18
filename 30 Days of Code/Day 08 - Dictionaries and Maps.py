# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())

    #read data into phone_book
    phone_book = {}
    for i in range(n):
        item = list(input().rstrip().split())
        phone_book[item[0]] = item[1]

    #query phone book
    while True:
        try:
            key = input()
            if key in phone_book:
                print(key+"="+phone_book[key])
            else:
                print("Not found") 
        except: break
