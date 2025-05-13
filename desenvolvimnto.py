devs = []

while True:
    print()
    tipo = str(input('Digite o tipo de desenvolvimento: ')).capitalize()
    rapidez = str(input('Digite o quão rápido é se desenvolver naquilo: ')).capitalize()
    exemplo = str(input(f'Digite um exemplo do que desenvolver no tipo de desenvolvimento {tipo}: ')).capitalize()
    desenvolvimento = {"tipo": tipo, "rapidez": rapidez, "exemplo": exemplo}
    devs.append(desenvolvimento)

    print()
    continuar = str(input("Quer continuar? [S/N] ")).upper()[0]
    if continuar == 'N':
        break

for i, k in enumerate(devs):
    print(f'{devs[i]["tipo"]:.<10} - {devs[i]["rapidez"]:.^10} - {devs[i]["exemplo"]:.>10}')
