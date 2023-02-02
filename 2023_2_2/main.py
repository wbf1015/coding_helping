ss = str(input())
count = [0]
res = []
k = 0


def dfs(i, s, k):
    if i == len(ss):
        if k == 2:
            res.append(s)

    else:
        dfs(i + 1, s + ',' + ss[i], k + 1)
        dfs(i + 1, s + ss[i], k)


dfs(1, ss[0], 0)
print(len(res))
print(res)
