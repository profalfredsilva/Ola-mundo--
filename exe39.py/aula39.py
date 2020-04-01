from datetime import date
atual = date.today().year
nasc = int(input('Qual é o ano do seu nascimento ?'))
idade = atual - nasc
print ('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade,atual))
if idade == 18:
    print('Voce tem 18 anos aliste-se IMEDIATAMENTE !')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para seu alistamento militar'.format(saldo))
    ano = atual + saldo
    print('voce deve se alistar em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado a {} anos'.format(saldo))
    ano= atual - saldo
    print('Seu alistamento foi em {}'.format(ano))  