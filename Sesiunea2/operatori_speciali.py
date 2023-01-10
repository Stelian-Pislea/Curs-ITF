#1.operatori de identitate
x1 = 5
y1 = 5
x2 = 'hello'
y2 = 'hello'
print(x1 is y1)
print(x1 is not y1)
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x3 == y3)
print(x3 is y3)
print(x3 is x3) # pentru tipuri de date complexe is verifica daca cei doi operanzi sunt exact acelasi obiect

# 2.membeship operators(operatori de aparteneta)
x = 'Ana are mere'
print('a' in x)
print('t' not in x)