# 1 Sa se implementeze un decorator care masoara
# timpul necesar executiei unei functii.
from time import perf_counter, sleep
import time
import csv

def function_time(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        print(f"Diferenta de timp necesara generarii: {end_time - start_time}")
        return result

    return wrapper


# 2 Sa se genereze primele 100 de numere prime folosind liste,
# si apoi folosind generator. Comparati diferenta
# de timp necesara generarii.
@function_time
def numere_prime(n):
    prime = []
    for num in range(2, n + 1):
        for i in prime:
            if num % i == 0:
                break
        else:
            prime.append(num)
    return prime

@function_time
def numere_prime_gen(n):
    def prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    yield from (x for x in range(2, n + 1) if prime(x))

numere_prime(100)
numere_prime_gen(100)

# 3 Scrieti un decorator care primeste ca argument numele
# unui fisier si pentru orice functie apelata, el va scrie
# in acel fisier numele functiei, lista de argumente ca si
# string si rezultatul apelului. Fisierul este de tip csv.
# Functiile decorate pot primi oricate argumente.

def write_to_csv(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([func.__name__, args, result])
            return result
        return wrapper
    return decorator

@write_to_csv('my_file.csv')
def add(x, y):
    return x + y

add(5,3)