# Enter your code here. Read input from STDIN. Print output to STDOUT
#number of inputs
n = int(input())
#creating a set 'countries'
countries = set()
#taking input of countries

for i in range(n):
    countries.add(input())
#as set contains distinct elements we just need to print the length
print(len(countries))
