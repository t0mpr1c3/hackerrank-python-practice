if __name__ == '__main__':
    N = int(input())
    x = []
    for i in range(N):
        cmd = input().split(' ')
        if cmd == ["print"]:
            print(x)
        elif cmd == ["sort"]:
            x.sort()
        elif cmd == ["pop"]:
            x.pop()
        elif cmd == ["reverse"]:
            x.reverse()
        elif cmd[0] == "insert" and len(cmd) == 3:
            x.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "remove" and len(cmd) == 2:
            x.remove(int(cmd[1]))
        elif cmd[0] == "append" and len(cmd) == 2:
            x.append(int(cmd[1]))
