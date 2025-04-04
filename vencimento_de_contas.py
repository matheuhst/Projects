dia = int(input('Digite o dia do vencimento da conta a pagar: '))
mes = int(input('Digite o mês do vencimento da conta a pagar: '))

dia_agora = 4 # exemplo de um dia
mes_agora = 4 # exempo do mês de abril

tempo_restante = dia - dia_agora

if tempo_restante <= 5 and mes == mes_agora:
    print('Sua conta está próxima de vencer, tome cuidado.')

elif tempo_restante >= 5 and tempo_restante <= 15 and mes == mes_agora:
    print('Sua conta ainda levará algum tempo para vencer.')

elif tempo_restante > 15 or mes > mes_agora:
    print('Sua conta ainda está longe de vencer.')
