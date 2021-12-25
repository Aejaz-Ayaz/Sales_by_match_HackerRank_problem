a = input("Enter the list of integers (seperate each integer with a space): ").split()

b = [int(i) for i in a]

c = set(b)

result = 0

for i in c:
    result += (b.count(i))//2

print(result)
