# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
r = list(map(int, input().split()))
s = set(r)
t = set()
c = 0
for i in r:
    if i in t:
        s.discard(i)
    else:
        t.add(i)
print(list(s)[0])
