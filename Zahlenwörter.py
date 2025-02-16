Einer = [['', []], ['un', []], ['dode', []], ['tre', ['s']], ['quattuor', []], ['quin', []], ['se', ['x']], ['septe', ['m', 'n']], ['okto', ['m', 'n']], ['nove', []]]
Zehner = [[[], ''], [['n'], 'dezi'], [['m','s'], 'viginti'], [['n','s'], 'triginta'], [['n','s'], 'quadraginta'], [['n','s'], 'quinquaginta'], [['n'], 'sexaginta'], [['n'], 'septuaginta'], [['m','x'], 'oktoginta'], [[], 'nonaginta']]
Hunderter = [[[],''],[['n','x','s'], 'zenti'], [['n'], 'duzenti'], [['n','s'], 'trezenti'], [['n','s'], 'quadringenti'], [['n','s'], 'quingenti'], [['n'], 'seszenti'], [['n'], 'septingenti'], [['m','x'], 'oktingenti'], [[], 'nongenti']]
# Falls man ein Zehner-Präfix nimmt, ohne diesen mit einem Hunderter-Präfix zu kombinieren, muss man die Endung -a (falls vorhanden) durch -i ersetzen.



for h in range(10):
    for z in range(10):
        for e in range(10):
            temp = ''
            if len(Einer[e][1]) != 0:
                if z == 0:
                    if len(Hunderter[h][0])!=0:
                        for i in range(len(Einer[e][1])):
                            for ii in range(len(Hunderter[h][0])):
                                if Hunderter[h][0][ii] == Einer[e][1][i]:
                                    temp = Hunderter[h][0][ii]
                else:
                    if len(Zehner[z][0]) != 0:
                        for i in range(len(Einer[e][1])):
                            for ii in range(len(Zehner[z][0])):
                                if Zehner[z][0][ii] == Einer[e][1][i]:
                                    temp = Zehner[z][0][ii]
            final = Einer[e][0]+temp+Zehner[z][1]+Hunderter[h][1]
            if h == 0 and len(final)!=0:
                if final[-1] == 'a':
                    final = final[0:-1] + 'i'
            print(h*100+z*10+e,': ', final)
