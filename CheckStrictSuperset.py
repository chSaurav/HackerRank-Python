#Variable A contains a set of items.
#Variable N tells the program how many sets will be created.

A = set(map(int, raw_input().split()))
N = int(raw_input())

#List in which we will store different sets once we create them.

set_list = []

#We loop N times and variable x creates N sets. We append these sets to a list. Previously created variable set_list now contains a number of different sets.

for i in range(N):
    x = set(map(int, raw_input().split()))
    set_list.append(x)

#Default value of the resuls variable is True

result = True

#We iterate over differnet sets in a list.  Result will stay True, unless we find a set to whom A is not a superset.

for i in set_list:
    if not A.issuperset(i):
        result = False

print result


------------------------------------SOLUTION 2 -------------------------

def checker():
    sub = set(map(int, input().split()))
    if sub.issubset(a):
        if(len(a)==len(sub)):
            l.append(0)
        else:
            l.append(1)
    else:
        l.append(0)


a = set(map(int, input().split()))
n = int(input())
l = []
for i in range(n):
    checker()
if all(l) == i:
    print(True)
else:
    print(False)
----------------------------TEST CASE----------------------------
83 47 85 21 49 62 95 96 73 6 97 49 91 90 56 55 70 87 55 78 11 50 6 50 66 81 45 89 31 97 41 1 86 85 2 80 88 60 49 36 41 50 98 86 84 5 94 39 52 59 69 10 27 2 14 51 54 48 17 22 45 70 44 10 98 28 55 57 85 29 15 65 51 22 64 88 56 9 78 17 55 67 21 85 51 14 98 63 83 78 42 5 71 41 95 74 4 11 81 69 86 11 81 33 21 89 14 45 99 61 92 66 68 76 9 57 64 56 51 85 32 77 17 4 53 22 79 26 75 27 92 40 0 27 37 20 42 95 6 16 68 89 54 97 3 11 20 48 80 42 45 51 63 84 43 32 35 71 14 36 8 44 30 38 7 90 23 37 54 63 10 24 1 50 65 74 30 66 44 69 98 21 17 88 82 39 66 90 80 78 21 2 11 8 0 67 70 90 56 22 10 32 65 59 30 95 77 83 91 89 94 25 45 16 3 41 30 53 96 85 40 13 95 89 1 10 1 86 86 53 0 53 39 2 99 13 36 96 68 75 69 98 88 20 41 94 72 73 5 65 79 42 96 81 76 95 15 99 51 15 36 31 50 10 50 2 2 37 63 75 19 89 90 32 27 1 40 28 42 44 30 3 66 66 18 53 14 0 43 60 15 79 43 55 92 52 72 6 79 23 17 9 66 21 4 1 37 86 39 7 57 72 72 55 31 46 52 46 79 19 44 41 65 9 69 3 11 9 44 52 26 79 11 50 99 38 8 72 84 40 15 48 75 64 57 9 0 87 34 4 18 93 72 87 49 61{-truncated-}
