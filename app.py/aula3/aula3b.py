a = int(input('Primeiro valor: '))
b = int(input('Segundo valor; : '))
c = int(input('Terceiro valor: '))
if a > b:
    print("O maior numero é {}".format(a))
elif b > a and b > c:
    print('Omaior numero é {} '.format(b))
else:
    print('O maior numero é {}'.format(c))
print('Final do programa')
