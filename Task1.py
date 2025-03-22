f = open("C:/Users/balbe/Downloads/27-124a.txt")
n, k, v, m = list(map(int, f.readline().split()))
a = [0] * k

for i in range(n):
    kilometer_num, pochta = list(map(int, f.readline().split()))
    a[kilometer_num % k] = pochta // v + (pochta % v > 0)

min_sa = sum(a)
if m < (k + 1) // 2 - 1:
    c = sum(a[:m*2 + 1])
    if a[m]:
        min_sa = c
    else:
        min_sa = 0

    for i in range(1, k):
        c += a[(i + m * 2) % k] - a[i - 1]
        if a[(i + m) % k]:
            min_sa = max(min_sa, c)

print(min_sa)
f.close

e = open("C:/Users/balbe/Downloads/27-124b.txt")
n, k, v, m = list(map(int, e.readline().split()))
a = [0] * k

for i in range(n):
    kilometer_num, pochta = list(map(int, e.readline().split()))
    a[kilometer_num % k] = pochta // v + (pochta % v > 0)

min_sb = sum(a)
if m < (k + 1) // 2 - 1:
    c = sum(a[:m*2 + 1])
    if a[m]:
        min_sb = c
    else:
        min_sb = 0

    for i in range(1, k):
        c += a[(i + m * 2) % k] - a[i - 1]
        if a[(i + m) % k]:
            min_sb = max(min_sb, c)
e.close
print(min_sb)
