# Enter your code here. Read input from STDIN. Print output to STDOUT

#read from input
n = int(input())
for i in range(0, n):
    text = input()
    evenText = ''
    oddText = ''    
    for j in range(len(text)):
        if j % 2 == 0:
            evenText = evenText + text[j]
        else:
            oddText = oddText + text[j]
    print(evenText, oddText)
