nome = str(input('Escreva seu nome: '))
idade = int(input('Sua idade: '))

if idade < 16:
    print('O individuo', nome, ' ainda não pode votar')
elif 16 <= idade <= 17:
    print('Optativo a votação do individuo', nome)
elif 18 <= idade < 70:
    print('O individuo', nome, ' é obrigado a votar')
else:
    print('A votação para o individuo', nome, ' é optativa')
