if __name__ == "__main__":
    N = int(input())
    trees = list(map(int, input().split(" ")))
    trees.sort(reverse=True)

    Ans = 0
    for i in range(len(trees)):
        Ans = max(trees[i] + i + 2, Ans)
    
    print(Ans)