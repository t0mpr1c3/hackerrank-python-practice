# Enter your code here. Read input from STDIN. Print output to STDOUT
na = input()
a = set(map(int, input().split()))
nb = input()
b = set(map(int, input().split()))
sd = list(a.union(b).difference(a.intersection(b)))
sd.sort()
for i in sd:
    print(i)