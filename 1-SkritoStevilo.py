# -*- coding: utf-8 -*-

#Ta mi nagaja, ko vnesem previsoko število program ponavlja opozorilo o previsokem številu?

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
        break
    print