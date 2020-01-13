# NOTE: You must convert the inputs to int in order for the hash() call to return the proper outputs

n = int(input())
t = tuple(map(int, input().split()))

print(hash(t))
