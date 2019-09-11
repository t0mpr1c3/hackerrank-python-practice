if __name__ == '__main__':
    grades = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])
    grades.sort(key = lambda x: x[1])
    scores = list(set(map(lambda x: x[1], grades)))
    scores.sort()
    second_lowest_names = [x[0] for x in grades if x[1] == scores[1]]
    second_lowest_names.sort()
    for n in second_lowest_names:
        print(n)
