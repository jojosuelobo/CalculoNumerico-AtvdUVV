def printM(matriz, matriz2):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end=' ')
            if(j == 2):
                print(f' = {matriz2[i]}')
    print()

# Organiza a matriz
def att(matriz1, matriz2):
    aux1 = matriz2[0] / matriz1[0][0]
    aux2 = - (matriz1[0][1] / matriz1[0][0])
    aux3 = - (matriz1[0][2] / matriz1[0][0])
    x1 = [aux1, aux2, aux3]

    aux1 = matriz2[1] / matriz1[1][1]
    aux2 = - (matriz1[1][0] / matriz1[1][1])
    aux3 = - (matriz1[1][2] / matriz1[1][1])
    x2 = [aux1, aux2, aux3]

    aux1 = matriz2[2] / matriz1[2][2]
    aux2 = - (matriz1[2][0] / matriz1[0][0])
    aux3 = - (matriz1[2][1] / matriz1[0][0])
    x3 = [aux1, aux2, aux3]

    return [x1, x2, x3]

# Jacobbi
def iter(matriz3 ,iteracao):
    x1 = matriz3[0][0] + matriz3[0][1] *iteracao[1] + matriz3[0][2] *iteracao[2]
    x2 = matriz3[1][0] + matriz3[1][1] *iteracao[0] + matriz3[1][2] *iteracao[2]
    x3 = matriz3[2][0] + matriz3[2][1] *iteracao[0] + matriz3[2][2] *iteracao[1]
    iteracao[0] = x1
    iteracao[1] = x2
    iteracao[2] = x3
    return iteracao

# Seidel
def seid(matriz3, iteracao):
    x1 = matriz3[0][0] + matriz3[0][1] * iteracao[1] + matriz3[0][2] * iteracao[2]
    x2 = matriz3[1][0] + matriz3[1][1] * x1 + matriz3[1][2] * iteracao[2]
    x3 = matriz3[2][0] + matriz3[2][1] * x1 + matriz3[2][2] * x2
    iteracao[0] = x1
    iteracao[1] = x2
    iteracao[2] = x3
    return iteracao

#Matriz "Ax"
matriz1 = ([10,2,1],
           [1,5,1],
           [2,3,10])
#Matriz "b"
matriz2 = [7,-8,6]

#prescisao = 1
iteracao = [0,0,0]

resp = input('Digite (1) para inserir matriz e (QUALQUER OUTRA COISA) para usar a matriz padrao: ')
if (resp == '1'):
#Insercao da matriz pelo usuario
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            matriz1[i][j] = int(input(f'Insira a matriz Ax em relação a (Ax = B): [{i+1}][{j+1}]: '))
    for i in range(len(matriz2)):
            matriz2[i] = int(input(f'Insira os valores da matriz B em relação a (Ax = B): [1][{i+1}]: '))
print('MATRIZ PADRAO: ')
printM(matriz1, matriz2)

resp = input('Digite (1) para o metodo Gauss-Jacobi e (QUALQUER OUTRA COISA) para usar o metodo Gauss-Seidel: ')
if (resp == '1'):
    print('-> Metodo Gauss-Jacobi')
    matriz3 = att(matriz1, matriz2)
    qnt = int(input('Informe a quantidade de iterações desejadas: '))
    for i in range(qnt):
        print(f'{i+1}: ITERAÇÃO: [{iteracao[0]:.5f}, {iteracao[1]:.5f}, {iteracao[2]:.5f}]')
        iteracao = iter(matriz3, iteracao)
else:
    print('-> Metodo Gauss-Seidel')
    matriz3 = att(matriz1, matriz2)
    qnt = int(input('Informe a quantidade de iterações desejadas: '))
    for i in range(qnt):
        print(f'{i + 1}: ITERAÇÃO: [{iteracao[0]:.5f}, {iteracao[1]:.5f}, {iteracao[2]:.5f}]')
        iteracao = seid(matriz3, iteracao)