n = int(input())
s1 = list(map(int, input().split()))
s1=set(s1)
m = int(input())
s2 = list(map(int, input().split()))
s2=set(s2)

s3 = s1.union(s2)

l = []
for i in s3:
    if i in s1 and i in s2:
        pass
    else:
        l.append(i)
l.sort()
for i in l:
    print(i)
