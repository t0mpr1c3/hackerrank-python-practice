# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
r = list(map(int, input().split()))
s = set(r)
for i in s:
    if r.count(i) == 1:
        print(i)
        break