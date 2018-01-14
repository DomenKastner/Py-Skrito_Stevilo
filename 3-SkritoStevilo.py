# -*- coding: utf-8 -*-

#Ta koda mi omogoča ugibanje le enkrat.

skritostevilo = 69

n = int(raw_input(" Ugani številko\n od 1 do 99: "))

if n == skritostevilo:
    print "E! Bravo"
elif n < skritostevilo:
    print "Vpisal si prenizko številko"
else:
    print "Vpisal si previsoko številko"