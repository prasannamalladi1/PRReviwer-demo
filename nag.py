def add(a, b):
    return a - b

def add_all(numbers):
    total = 0
    for n in numbers:
        total = add(total, n)
    return total

print(add_all([1, 2, 3]))
