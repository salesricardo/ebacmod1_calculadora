# Guarda as opções de operações do programa.
# A estrutura de dado tupla foi escolhida aqui,
# pois ela estará guardando valores imutáveis em
# tempo de execução do programa.
operacoes = ('Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação', 'Resto')

print('Bem vindo(a)! Minha função aqui é lhe servir com operações básicas da matemática.')
print('O processo é bem simples. Eu lhe mostrarei quais operações estão disponíveis, e você apenas terá de escolher uma delas.')
print('Com base em sua escolha nós estaremos utilizando dois números para que possamos operar com eles.')
print('E então, vamos começar?')
print(f'Estes são os serviços que estou oferecendo no momento, todos enumerados. ')

# Loop principal do programa.
while True:

  # ETAPA 1 - Opções de direção
  ########################################

  # Apresenta operações para usuário decidir o que quer.
  # A barra de iguais (=) seguinte foi utilizada para
  # separar e organizar melhor as diferentes interações
  # do usuário com o programa.
  print('==============================================================================================')
  for o in operacoes:
    # Pequena correção +1, pois tuplas funcionam por meio
    # de índices, o qual o primeiro começa com zero (0).
    # O mesmo será feito em outros trechos do código.
    print(f'{operacoes.index(o)+1} -- {o}')

  # ETAPA 2 - Direcionamento de programa
  ########################################

  # Obtém decisão de usuário.
  decisao = input(f'Digite o número da operação que deseja utilizar, ou qualquer outro valor para sair: ')

  # Decisão de usuário é válida para este programa?
  # isnumeric() aqui impede que exceção seja lançada
  # mais à frente, levando o programa a um estado de
  # total inconsistência indefinida para o usuário.
  if decisao.isnumeric() == False and decisao not in range(1,7):
    # O usuário precisa digitar números de 1 a 6, caso
    # contrário o programa será encerrado.
    print(f'A operação escolhida não corresponde com nenhuma das disponíveis.')
    break

  # Casting de string para int, e mostra a escolha feita.
  # Um casting é necessário aqui, pois decisao será trabalhada
  # com índice, e também deverá ser verificada como número
  # nas estruturas de condição mais à frente.
  decisao = int(decisao)
  print(f'Operação escolhida: {operacoes[decisao - 1]}')

  # ETAPA 3 - Preparação de dados
  ########################################

  # Usuário insere números, mas que precisam ser
  # verificados antes para evitar lançamento de exceção.
  num_1 = input('Digite o primeiro número: ')
  num_2 = input('Agora o segundo: ')

  # Impede lançamento de exceção se valores passados
  # não forem realmente números. Programa pula iteração
  # atual para tentar novamente.
  #
  # Há uma falta aqui, pois números negativos não
  # são reconhecidos pela função isnumeric() como
  # sendo números, afinal, ela verificar todos os
  # caracteres, mas apenas um por vez. O programa
  # em si não dará um erro, mas ficará limitado
  # a trabalhar apenas com números positivos.
  if(num_1.isnumeric() and num_2.isnumeric()):
    num_1 = int(num_1)
    num_2 = int(num_2)
  else:
    print('Algum dos valores passados não é um número. Vamos tentar mais uma vez?')
    continue

  # ETAPA 4 - Processamento de dados
  ########################################

  # Adição
  if decisao == 1:
    print(f'A soma entre {num_1} e {num_2} é exatamente: {num_1 + num_2}')

  # Subtração
  elif decisao == 2:
    print(f'Ao subtrairmos {num_1} e {num_2}, encontramos: {num_1 - num_2}')

  # Multiplicação
  elif decisao == 3:
    print(f'Na multiplicação entre {num_1} e {num_2} nós temos: {num_1 * num_2}')

  # Divisão
  elif decisao == 4:
    print(f'Ao subtrairmos {num_1} e {num_2}, encontramos: {num_1 / num_2}')

  # Potenciação
  elif decisao == 5:
    print(f'Quando elevamos {num_1} à {num_2} potência, obtemos: {num_1 ** num_2}')

  # Resto
  elif decisao == 6:
    print(f'O resto entre {num_1} e {num_2} é: {num_1 % num_2}')

# Fim de programa.
print('Fim de programa.')
