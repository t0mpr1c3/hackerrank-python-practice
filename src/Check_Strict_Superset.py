# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
N = int(input())
s = 1
for i in range(N):
    B = set(map(int, input().split()))
    if not (A.issuperset(B) and len(A) > len(B)):
        s = 0
        break
print(["False","True"][s])