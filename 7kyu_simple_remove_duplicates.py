def solve(arr):
    l = []
    for i in arr[::-1]:
        if i not in l:
            l.append(i)
    l.reverse()
    return l

print (solve([3,4,4,3,6,3]))