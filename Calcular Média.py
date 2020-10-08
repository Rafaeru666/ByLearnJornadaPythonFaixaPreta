nota1 = 7
nota2 = 5
nota3 = 3
nota4 = 6

def verificar_aprovacao():
  media = calcular_media([nota1, nota2, nota3, nota4])

  if media >= 5:
    print('Você foi aprovado!')
  else:
    print('Você foi reprovado.')

def calcular_media(notas):
  quantidade = len(notas)

  soma = 0
  for nota in notas:
    soma = soma + nota

  media = soma / quantidade

  return media

verificar_aprovacao()