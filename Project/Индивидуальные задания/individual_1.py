#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    a = list(map(int, input("Введите элементы списка: ").split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    pos = len([i for i in a if i > 0])
    print(f"Кол-во положительных элементов: {pos}")
    neg = len([i for i in a if i < 0])
    print(f"Кол-во отрицательных элементов: {neg}")

    if pos > neg:
        print("Положительных элементов больше")
    elif neg > pos:
        print("Отрицательных элементов больше")
    else:
        print("Кол-во положительных и отрицательных элементов одинаково")