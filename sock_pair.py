# Sample input 1:
# a = [1,2,1,2,1,3,2]     # outputs 2

# Sample input 2:
# a = [1,2,3]             # outputs 0

a = [10, 20, 20, 10, 10, 30, 50, 10, 20]    # outputs 3

b = set(a)

c = 0

for i in b:
    c += (a.count(i))//2

print(c)
