def imc(peso, altura):
  altura_quadrada = altura ** 2
  meu_imc = peso / altura_quadrada
  print(f'O meu imc é {meu_imc:.2f}') #:.2f arredonda para duas casas decimais
  return meu_imc

meu_imc = imc(66, 1.75)