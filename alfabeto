alfabeto = 'A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z'
lista = alfabeto.split('.')


def criptografar(palavra, chave):
    palavra_nova = []
    for letra in palavra:
        for posicao, valor in enumerate(lista):
            if letra == valor:
                if (posicao + chave) < len(lista):
                    palavra_nova.append(lista[posicao + chave])
                elif (posicao + chave) >= len(lista):
                    c2 = (posicao + chave) % 26
                    palavra_nova.append(lista[c2])

    formatada = ''.join(palavra_nova)
    return formatada

def descriptografar(vetor, chave):
    palavra_nova = []
    for letra in palavra:
        for posicao, valor in enumerate(lista):
            if letra == valor:
                if (posicao + chave) < len(lista):
                    palavra_nova.append(lista[posicao + chave])
                elif (posicao + chave) >= len(lista):
                    c2 = (posicao + chave) % 26
                    palavra_nova.append(lista[c2])

    formatada = ''.join(palavra_nova)
    return formatada


while True:
    escolha = int(input('''O que você quer fazer?
[1] Criptografar
[2] Descriptografar
[3] Sair
>>> '''))
    if escolha == 1:
        palavra = str(input('Digite uma palavra: ')).upper()
        chave = int(input('Digite a sua chave: '))
        resultado = criptografar(palavra, chave)
        mostra = str(input('Quer ver como ficou? [S/N] ')).upper()[0]
        if mostra == 'S':
            print(resultado)
            continue
    
    if escolha == 2:
        palavra = str(input('Digite uma palavra: ')).upper()
        chave = int(input('Digite a chave para tentar descriptografar: '))
        resultado = descriptografar(palavra, chave)
        if resultado != palavra:
            print('Chave errada, irmão.')
            break
        else:
            print(resultado)

        mostra = str(input('uer ver como ficou? [S/N] ')).upper()[0]
        if mostra == 'S':
            print(resultado)
            continue
        
        cont = str(input('Quer continuar? [S/N] ')).upper()[0]
        if cont != 'S':
            break
        elif cont == 'S':
            continue
    
    if escolha == 3:
        palavra = ''
        print('Lista apagada. ')
        continue
    
    if escolha == 4:
        print(lista)
        continue

    if escolha == 5:
        break

