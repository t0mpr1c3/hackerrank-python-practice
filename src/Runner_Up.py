if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    uniq = list(set(arr))
    uniq.sort()
    print(uniq[-2])

