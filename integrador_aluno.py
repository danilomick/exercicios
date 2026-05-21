alunos = [] #Cria uma lista para dicionários
 
while True: #Loop para o sistema de cadastro
    try: #Tratamento de erros para os inputs
 
        #Laço while para pedir o nome, e forçá-lo a ser string
        while True: #Laço de repetição para loop
            try: #Tratamento de erros
                nome = input("Digite o nome do aluno: ") #Pede o nome ao usuário
                float(nome) #Converte o nome para float (numérico)
                print("Erro! O nome não pode ser um número.") #Se for convertido, o valor é um número. Printa a mensagem de erro.
            except ValueError: #Se a conversão der em erro.
                if nome: #Se um nome existir (se não for vazio)
                    break #Sai do loop e prossegue o código
                else: #Se o nome for vazio
                    print("Erro! O nome não pode estar vazio.") #Printa a mensagem de erro
 
        #Pedir idade
        idade = int(input("Digite a idade: "))  #Pede a idade ao usuário e transforma em int
        if idade > 0 and idade <= 125: #Verifica se a idade é maior que 0 e menor ou igual a 125.
            pass #Se for, prossegue normalmente
        else: #Se a condição for falsa
            print("Valor inválido! A idade precisa ser maior que 0 e menor ou igual a 125.") #Printa o erro
            continue #Repete a iteração
 
        #Pedir nota
        nota = float(input("Digite a nota: ").replace(",", ".")) #Pede a nota ao usuário, substitui vírgula pra ponto e converte para float
        if nota >= 0 and nota <= 10: #Verifica se a nota está entre 0 e 10
            pass #Se for, prossegue normalmente
        else: #Se a condição for falsa
            print("Valor inválido! A nota precisa ser entre 0 e 10.") #Printa o erro
            continue #Repete a iteração
 
        #Função de verificação da situação
        def classificar_aluno(nota):
            if nota >= 7: #Se a nota for maior ou igual a 7
                return "Aprovado" #A situação será aprovado
            elif nota >= 5: #Se a nota for maior ou igual a 5
                return "Recuperação" #A situação será recuperação
            else: #Se ela estiver entre 0 e 4.9
                return "Reprovado" #A situação será reprovado
 
        aluno = {"nome": nome, "idade": idade, "nota": nota, "situacao": classificar_aluno(nota)} #Adiciona os respectivos valores em dicionários
        alunos.append(aluno) #Adiciona o aluno na lista
 
        while True: #Cria um loop para forçar o usuário a escrever corretamente
            escolha = input("Deseja cadastrar outro aluno? (s/n) ") #Pergunta ao usuário como prosseguir
            if escolha.strip().lower() == "s": #Se a escolha, removida os espaços e em caixa baixa, for s
                break #Sai do loop
            elif escolha.strip().lower() == "n": #Se a escolha, removida os espaços e em caixa baixa, for n
                break #Sai do loop
            else: #Se o usuário digitar algo que não for s ou n
                print("Valor inválido! Tente novamente! Digite apenas s ou n.") #Printa o valor inválido, e loopa novamente
         
        if escolha.strip().lower() == "n": #Se a escolha, removida os espaços e em caixa baixa, for n,
            break #O código segue (O else: continue está omisso por redundância)
 
    except ValueError: #Se algum dos inputs der erro,
        print("Valor inválido!") #Printa o erro
 
#Função de printar os valores na tela
def mostrar_valores(alunos):
    print("\n---RESULTADO---") #Printa o título
 
    for aluno in alunos: #Cria um loop dentro da lista
        print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']} | Situação: {aluno['situacao']}") #Printa cada nome, idade, nota e situação
 
#Função de calcular a média da turma
def calcular_media(alunos): 
    if len(alunos) > 0: #Se o número de alunos for maior que 0
        media = sum(aluno['nota'] for aluno in alunos) / len(alunos) #Define que a média é a soma de todas as notas (utilizando o loop for que percorre a lista alunos) dividido pela quantidade
        print(f"\nMédia da turma: {media:.2f}") #Printa a média da turma, com o valor apenas em duas casas decimais
 
#Função de verificar as situações
def verif_situacao(alunos):
 
    aprovados = 0 #Cria a variável "aprovados" para posteriormente contar quantos aprovados existem
    recuperacao = 0 #Cria a variável "recuperação" para o mesmo propósito
    reprovados = 0 #Cria a variável "reprovados" para o mesmo propósito
 
    for aluno in alunos: #Percorre a lista de alunos com loop for
        if aluno['situacao'] == 'Aprovado': #Se a situação do aluno for igual a 'Aprovado'
            aprovados += 1 #Soma-se 1 à variável aprovados
        elif aluno['situacao'] == 'Recuperação': #Se a situação for igual a 'Recuperação'
            recuperacao += 1 #Soma-se 1 à variável recuperacao
        else: #Se a situação for 'reprovado'
            reprovados += 1 #Soma-se 1 à variável reprovados
 
    print(f"Aprovados: {aprovados}") #Printa quantos alunos estão aprovados
    print(f"Recuperação: {recuperacao}") #Printa quantos alunos estão de recuperação
    print(f"Reprovados: {reprovados}") #Printa quantos alunos estão reprovados
 
#Função de verificar as maiores e as menores notas
def maior_menor(alunos):
    def r_nota(aluno): #Função de "retornar" a nota de cada aluno
        return aluno['nota'] #Retorna a nota
 
    aluno_maior = max(alunos, key = r_nota) #Retorna o dicionário do aluno com a maior nota. O key serve para determinar qual valor ele deve usar.
    aluno_menor = min(alunos, key = r_nota) #Retorna o dicionário do aluno com a menor nota
 
    print(f"\nAluno com maior nota: {aluno_maior['nome']} - {aluno_maior['nota']}") #Exibe o nome e a maior nota
    print(f"Aluno com menor nota: {aluno_menor['nome']} - {aluno_menor['nota']}") #Exibe o nome e a menor nota
 
mostrar_valores(alunos) #Chama a função de mostrar valores
calcular_media(alunos) #Chama a função de calcular e mostrar a média
verif_situacao(alunos) #Chama a função de contar as stiuações e printar
maior_menor(alunos) #Chama a função de verificar e mostrar as maiores e menores notas