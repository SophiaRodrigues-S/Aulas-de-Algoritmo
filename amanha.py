def bissexto(a):
    return a % 4 == 0 and a % 100 != 0 or a % 400 == 0
       

def dia_maximo(m, a):
    if m == 2:
        return 28 + bissexto(a)
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31

def valida(d, m, a):
    if a < 1:
        return False
    if m < 1 or m > 12:
        return False
    if d < 1 or d > dia_maximo(m, a):
        return False
    return True

def exibe_ds(d, m, a):
     d += 1
     if d > dia_maximo(m, a):
         d = 1
         m += 1
         if m > 12:
             m = 1
             a += 1
     print(f'Dia seguinte: {d:02}/{m:02}/{a:04}')
    


def main():
    d, m, a = map(int, input('Data?').split('/'))

    if valida(d, m, a):
        exibe_ds(d, m, a)

    else:
        print('Data Inválida!')

main()



