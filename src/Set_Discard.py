# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
#print(s)
N = int(input())
for i in range(N):
    cmd = input()
    #print(cmd)
    if (cmd == "pop"):
        s.pop()
    else:
        c = cmd.split()
        if (c[0] == "discard"):
            s.discard(int(c[1]))
        elif (c[0] == "remove"):
            try:
                s.remove(int(c[1]))
            except:
                # keyerror
                a = 1
    #print(s)
print(len(s))
