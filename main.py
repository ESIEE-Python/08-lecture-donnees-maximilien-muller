#### Imports et définition des variables globales
"""
^^
"""
import random
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """
    retourne le contenu du fichier <filename>
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')  # Lecture du fichier avec ';' comme séparateur
        return [[int(value) for value in row] for row in reader]# Conversion des valeurs en entiers

def get_list_k(data, k):
    """
    ^^^^
    """
    l = data[k]
    return l

def get_first(l):
    """
    ^^^^^^
    """
    return l[0]

def get_last(l):
    """
    ^^^^^^
    """
    return l[-1]

def get_max(l):
    """
    ^^^^^^
    """
    return max(l)

def get_min(l):
    """
    ^^^^^^
    """
    return min(l)

def get_sum(l):
    """
    ^^^^^^
    """
    print(l)
    return sum(l)


#### Fonction principale

def main():
    """
    fonction main
    """
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))
    data = read_data(FILENAME)

    k = random.randint(0,len(data))

    if data:
        print(f"Liste {k}: {get_list_k(data, k)}")
        print(f"Premier élément: {get_first(data[k])}")
        print(f"Dernier élément: {get_last(data[k])}")
        print(f"Maximum: {get_max(data[k])}")
        print(f"Minimum: {get_min(data[k])}")
        print(f"Somme: {get_sum(data[k])}")

if __name__ == "__main__":
    main()
