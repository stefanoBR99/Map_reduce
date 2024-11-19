#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

palabra_actual = None
cuenta_actual = 0

for linea in sys.stdin:
    palabra, cuenta = linea.strip().split('\t', 1)
    try:
        cuenta = int(cuenta)
    except ValueError:
        continue

    if palabra_actual == palabra:
        cuenta_actual += cuenta
    else:
        if palabra_actual:
            print("{}\t{}".format(palabra_actual, cuenta_actual))

        palabra_actual = palabra
        cuenta_actual = cuenta

if palabra_actual == palabra:
    print("{}\t{}".format(palabra_actual, cuenta_actual))

