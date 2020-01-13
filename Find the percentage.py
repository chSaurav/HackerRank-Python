
#!/usr/bin/python

t = int(input())

stus = {}

for i in range(0, t):
    name, math, physic, chemistry = input().split(" ")
    stus[name] = (float(math) + float(physic) + float(chemistry)) / 3

name = input()
if name in stus:
    print("%.2f" % stus[name])
