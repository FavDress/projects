m = int(input('Минуты:'))
h = m//60
mn = m%60
if mn < 10:
    print(f'{h}:0{mn}')
else:
    print(f'{h}:{mn}')

