#!/usr/bin/env python3

from collections import Counter

def leggi_file():
    fin = open("testo.txt")
    counter = Counter([parola for parola in
                       fin.read().replace('\n', ' ').split(' ')
                       if parola != ''])

    fin.close()

    return counter

def secondo_elemento(t):
    return -t[1], t[0]

def stampa_statistica(statistica):
    for parola, num in sorted(statistica.items(), key=secondo_elemento):
        print("La parola {0} compare {1} volte".format(parola, num))

stat = leggi_file()
stampa_statistica(stat)
