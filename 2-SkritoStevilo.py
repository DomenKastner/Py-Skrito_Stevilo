# -*- coding: utf-8 -*-

# P0 tem, ko na koncu kode zamenjam break in print mi po zagonu ponudi možnost za vpis le dvakrat?
# Jaz pa bi rad, da me program sprašuje dokler ne uganem prave številke.

skritostevilo = int(raw_input(" Ugani številko\n od 1 do 99: "))

while 69 != "skritostevilo":
    print

    if skritostevilo < 69:
        print " Vpisal si prenizko številko"
        skritostevilo = int(raw_input("Ugani številko od 1 do 99: "))

    elif skritostevilo > 69:
        print " Vpisal si previsoko številko"

    else:
        print "Čestitke! Uganil si pravo številko"
        print
    break