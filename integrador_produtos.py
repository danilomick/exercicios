class Produto: #Cria a classe Produto
    def __init__(self, nome, preco): #Utiliza um método construtor para definir a classe, com nome e preço
        self.nome = nome #Define a variável nome
        self.preco = preco #Define a variável preço
    def exibir_produto(self, indice): #Cria um método para o produto, que o exibe, com o atributo índice
        print(f"\níndice: {indice}") #Exibe o índice, com quebra de linha
        print(f"Nome: {self.nome}") #Exibe o nome
        print(f"Preço: {self.preco}") #Exibe o preço
 
produtos = [] #Cria a lista produtos

def cadastrar_produto(): #Cria a função cadastrar produto, para ser utilizada pelo usuário
    print("\n---CADASTRAR PRODUTO---") #Printa o menu de cadastro com quebra de linha
    while True: #Cria um laço de repetição para validar os inputs
        nome = input("Digite o nome do produto: ") #Pede o nome do produto ao usuário
        try: #Usa tratamento de erros para validar os inputs
            preco = float(input("Digite o preço do produto: ")) #Pede o preço do produto e converte para float
            if preco <= 0: #Se o preço for menor ou igual a zero,
                print("Erro! O produto não deve ter preço 0 ou negativo.") #Printa que o produto não pode ter preço 0 ou negativo.
                continue #Volta pro loop
            else: #Se o preço for maior que 0,
                p = Produto(nome, preco) #Cria a variável temporária "p" para objetos da classe produto
                produtos.append(p) #Adiciona o produto na lista
                print(f"O produto {p.nome}, de preço {p.preco} foi cadastrado!") #Printa que o produto foi cadastrado
                break #Para o loop
        except ValueError: #Se algum dos inputs der erro,
            print("Valor inválido!") #Printa que o valor é inválido
            continue #Volta pro loop
 
def listar_produtos(): #Cria a função listar produto
    
    if not produtos: #Se não houver produtos na lista,
        print("\nNenhum produto cadastrado!") #Quebra a linha e printa que nenhum produto foi cadastrado.
    else: #Se houverem produtos,
        print("\n---LISTA DE PRODUTOS---") #Quebra a linha e printa o título do menu
        for i, p in enumerate(produtos): #Cria um loop for para acessar a posição de cada objeto na lista, com o enumerate
            p.exibir_produto(i) #Exibe cada produto de acordo com o índice
 
def comprar_produto(): #Cria a função de comprar produto
    print("\n---MENU DE COMPRA---") #Quebra a linha e printa o título do menu
    listar_produtos() #Chama a função de listar produtos
    
    while True: #Loop para tratar erros de input
        
        if not produtos: #Se não houver produtos
            return #Encerra a função

        try: #Tratamento de erros para inputs
            num = int(input("\nDigite o número do produto: ")) #Pede o número do produto e converte para inteiro
            if num < 0 or num >= len(produtos): #Se o número for menor que 0, ou for maior que o número de produtos,
                print("O produto não existe.") #Printa que o produto não existe
                continue #Volta o loop
        except ValueError: #Se o input der erro de valor
            print("Erro! Valor inválido.") #Printa o erro
            continue #Volta o loop
        
        while True: #Loop para tratar erros de input
            try: #Tratamento de erros para inputs
                qtd = int(input("Digite a quantidade desejada: ")) #Pede a quantidade e converte para inteiro
                if qtd <= 0: #Se a quantidade for menor ou igual a 0,
                    print("A quantidade não pode ser 0!") #Printa que isso não é possível
                    continue #Volta o loop
                else: #Se for maior que 0
                    break #Sai do loop
            except ValueError: #Se um dos inputs der erro de conversão
                print("Erro! Valor inválido.") #Printa o erro
                continue #Volta o loop
        
        total = produtos[num].preco * qtd #Cria a variável total, para armazenar o preço do produto escolhido multiplicado pela quantidade
        print(f"O total é {total}.") #Printa o total, utiliza o "f" para colocar variável dentro de string

        if total >= 100: #Se o total for maior ou igual a 100,
            print("Desconto disponível!") #Printa que há desconto disponível
        else: #Se for menor que 100
            print("Sem desconto!") #Printa que não há desconto

        break #Sai do loop

def menu(): #Cria a função menu
 
    while True: #Loop para manter o menu ativo
        print("\n---MENU---") #Quebra a linha e printa menu
        print("1 - Cadastrar produto") #Printa a primeira opção
        print("2 - Listar produtos") #Printa a segunda opção
        print("3 - Comprar Produto") #Printa a terceira opção
        print("4 - Sair") #Printa a quarta opção
    
        try: #Tratamento de erros para input
            escolha = int(input("\nEscolha uma opção acima: ").strip()) #Quebra a linha, pede a opção ao usuário, retira espaços em branco e converte para int
            if escolha not in (1, 2, 3, 4): #Se a escolha não for 1, 2, 3 ou 4,
                raise ValueError #Levar ao ValueError (except)
        except ValueError: #Se der erro,
            print("Valor inválido!") #Printa o erro
            continue #Volta o loop
 
        if escolha == 1: #Se a escolha for 1,
            cadastrar_produto() #Chama a função de cadastro
            continue #Mostra o menu novamente
        elif escolha == 2: #Se a escolha for 2,
            listar_produtos() #Chama a função de listagem
            continue #Mostra o menu novamente
        elif escolha == 3: #Se a escolha for 3,
            comprar_produto() #Chama a função de compra
            continue # Mostra menu novamente
        else: #Se a escolha for 4,
            print("Saindo...") #Exibe uma mensagem de encerramento
            break #Sai do loop
 
menu() #Chama a função principal (menu)