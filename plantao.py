funcionarios = [
    ['João', 0],
    ['Maria', 0],
    ['Rafael', 1],
    ['Matias', 0],
    ['Guilherme', 1],
    ['Aguado', 1],
    ['Matheus', 0]
]

while True:
    print('''O que você quer fazer?
[1] Colocar funcionário para hora extra.
[2] Remover funcionário da hora extra.''')
    resposta = int(input('>>> '))
    if resposta == 1:
        print('Os funcionários que não possuem horas extras marcadas são:')
        a = 1
        for i, k in funcionarios:
            if k == 0:
                print(f'[{a}] - {i}')
            else:
                a -= 1
            a += 1
        hora_extra = int(input('Qual funcionário você quer colocar para fazer hora extra? '))
        
