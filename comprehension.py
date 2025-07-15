# square = [x**2 for x in range(10)]
# evens = [x for x in range(10) if x%2==0]

square = list(map(lambda x: x**2, range(10)))
evens = list(filter(lambda x: x % 2 == 0, range(10)))

print(square)
print(evens)