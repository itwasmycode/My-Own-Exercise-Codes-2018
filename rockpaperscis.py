import os
import csv
from collections import defaultdict, namedtuple


def main():
    print_header()


def print_header():
    print("--------------------------")
    print("Welcome to Rock-Paper Scissors Game!")
    print("--------------------------")


class Player:
    def __init__(self, name):
        self.name = name


class Roll:
    def __init__(self, name):
        self.name = name

    def can_be_defeated(self, roll):
        pass

    def sear_ch(self, rolling):
        direct = os.getcwd() + '/battle-table.csv'
        with open(direct, "r") as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                print(row[rolling])


e1 = Roll('Emre')
e1.sear_ch('Gun')
