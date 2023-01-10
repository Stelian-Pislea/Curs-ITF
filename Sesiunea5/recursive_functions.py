# fibonacci: 0 1 1 2 3 5 8 13 21 34
def recursive_fibonacci(n):  # functie recursiva care se apeleaza singura
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)

for i in range(10):
    print(recursive_fibonacci(i))

def suma_primelor_n(n):
    if n == 0:
        return 0
    return n + suma_primelor_n(n-1)

print(suma_primelor_n(50))
print(sum(range(51)))