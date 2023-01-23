# 1 Sa se scrie o functie care citeste date dintr-un fisier csv
# si le scrie intr-un fisier json. Functia primeste
# numele fisierelor ca parametri.
import csv
import json
from pprint import pprint


def csv_to_json(citeste, scrie):
    data = []
    with open(citeste, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(scrie, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4))


citeste = r'citeste.csv'
scrie = r'scrie.json'
csv_to_json(citeste, scrie)


# 2 Sa se scrie o functie care citeste date
# dintr-un fisier json si le imparte in alte doua
# fisiere astfel incat prima jumatate a datelor
# va fi in fisierul prima_jumatate.json,
# iar a doua in a_doua_jumatate.json.

def split_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    jumatate = len(data) // 2
    with open('prima_jumatate.json', 'w') as f:
        json.dump(data[:jumatate], f)
    with open('a_doua_jumatate.json', 'w') as f:
        json.dump(data[jumatate:], f)


split_json('scrie.json')


# 3 Sa se scrie o functie care citeste date dintr-un
# fisier csv si le elimina pe cele care in oricare
# coloana contin litera ‘a’. Dupa aceea va actualiza
# fisierul cu datele ce raman.

def delete_element_in_CSV(file_name, char):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        for i in range(len(data)):
            for elem in data[i]:
                if char in elem:
                    data[i].remove(elem)
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


delete_element_in_CSV('user_tema.csv', 'a')
