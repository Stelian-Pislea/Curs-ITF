# 1.0
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# 1.1
print(note_muzicale)
# 1.2
note_muzicale = note_muzicale[::-1]
# 1.3
print(note_muzicale)
# 1.4
note_muzicale.reverse()
# 1.5
print(note_muzicale)

# 2
print(note_muzicale.count('do'))

# 3
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
print(list1 + list2)
list1.extend(list2)
print(list1)

# 4.0
list1.sort()
print(list1)
# 4.1
#list1.sort(0)
print(list1)
# 4.2
list1.remove(0)
print(list1)
# 5
if len(list1) == 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')

# 6
list1.clear()

# 7
if len(list1) == 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')

# 8
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

# 9
print(f"Ana a luat nota {(dict1['Ana'])}")
print(f"Gigel a luat nota {(dict1['Gigel'])}")
print(f"Dorel a luat nota {(dict1['Dorel'])}")

# 10
dict1['Dorel'] = 6
print(dict1)

# 11
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

# Ex optionale
# 1
jucatori = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5']
schimbari_efectuate = 0
if schimbari_efectuate < 0:
    exit(0)
schimbari_max = 3
in_teren = ['jucator1', 'jucator2', 'jucator3', ]

jucator_eliminat = 'jucator3'
jucator_adagat = 'jucator5'
jucator_schimbat = 'jucator4'

if jucator_eliminat in in_teren and schimbari_efectuate < schimbari_max:
    schimbari_efectuate += 1
    in_teren.remove(jucator_eliminat)
    in_teren.append(jucator_adagat)
if schimbari_max < schimbari_efectuate:
    exit(0)
else:
    print(f'A intrat {jucator_adagat} si a iesit {jucator_eliminat}, mai ai {schimbari_max - schimbari_efectuate} schimbari.')
if 'jucator4' not in in_teren:
    print(f'nu se poate efectua schimbarea deoarece jucătorul nu e în teren')
if schimbari_max - schimbari_efectuate < 0:
    exit(0)
else:
    print(f'Schimbari ramase {schimbari_max - schimbari_efectuate}')