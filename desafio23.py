print('{} DESAFIO 23 {}'.format('=' * 10, '=' * 10))
n = int(input('Digite um número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print("""\nunidade: {}
dezena: {}
centena: {}
milhar: {}""".format(u, d, c, m))
