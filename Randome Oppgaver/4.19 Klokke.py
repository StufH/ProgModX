print("I dette programmet skal du skrive inn et klokkeslett med formen tt:mm")
d = 0
mm = 0

while True:
    try:
        tt = int(input("skriv din verdi for timer:\n"))
        if 0 <= tt >= 23:
            print("skriv inn en rett verdi for timer")
            continue
        mm = int(input("skriv din verdi for minutter:\n"))
        if 0 <= mm >= 59:
            print("skriv inn en rett verdi for minutter")
            continue
        else:
            break
    finally:
        print("")
tt_2 = float(input("hvor mange timer har det gått? \n"))
mm_2 = float(input("hvor mange minutter har det gått? \n"))
tt = tt + tt_2
mm = mm + mm_2
ttmod = tt % 23
mmmod = mm % 59
mm_timer = mm // 60
if mm > 59:
    tt = tt + mm_timer
    mm = mmmod
if tt > 23:
    tt = ttmod
mm = int(mm)
tt = int(tt)
if tt >= 10 and mm >= 10:
    print(f"Klokken er nå {tt}:{mm}")
elif tt >= 10 and mm < 10:
    print(f"Klokken er nå {tt}:0{mm}")
elif tt < 10 and mm >= 10:
    print(f"Klokken er nå 0{tt}:{mm}")
else:
    print(f"Klokken er nå 0{tt}:0{mm}")