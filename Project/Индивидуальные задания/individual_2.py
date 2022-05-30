#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    a = list(map(float, input("Введите элементы списка: ").split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    i_max, a_max = 0, 0
    for i, item in enumerate(a):
        if abs(item) > abs(a_max):
            i_max, a_max = i, item
    print(f"Максимальный по модулю элемент: ({i_max}, {a_max})")

    c, k = 0, 0
    for i in a:
        if i > 0:
            if k == 1:
                break
            k = 1
            continue
        if k == 1:
            c += i
    print(f"Сумма между первым и вторым положительными элементами: {c}")

    a.sort(key=lambda x: x == 0)
    print(f"После сортировки: {a}")