a = input('a:')
b = input('b:')

x = float(a.replace(',','.'))
y = float(b.replace(',','.'))

sum1 = x+y
avg1 = round((x+y)/2, 2)
print(f'sum={sum1}; avg={avg1}')