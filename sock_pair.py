# a = [1,2,1,2,1,3,2]   # output should be 2

# a = [10, 20, 20, 10, 10, 30, 50, 10, 20]    # output should be 3

a = [1,2,3]             # output should be 0

b = set(a)

c = 0

for i in b:
    c += (a.count(i))//2

print(c)
