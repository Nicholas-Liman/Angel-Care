import sys
import subprocess
import json

def limpar_tela(): #Funçao limpar tela universal
    subprocess.run(['cls' if sys.platform == 'win32' else 'clear'], shell=True)

#Precisa de uma função para guardar e ler os dados do registro/Login em json
def salvar_dados_arquivo(nome_arquivo, dados): #Salva os arquivos em json
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

def guardar_dados(nome_funcao, retorno, dados_usuario): #Manipula os dados para salvar em json
    dados_usuario[nome_funcao] = retorno

def ler_dados(nome_arquivo): #Acessa e lê os dados dentro do Json
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        return None

def voltar(): #Funçoes de voltar dentro do portal
    print('')
    print('Caso deseje voltar à seleção do portal, digite "Voltar"')
    print('')
    print('Caso deseje deslogar e voltar ao início, digite "Logout"')
    print('')
    print('Caso deseje sair, digite "Sair"')
    print('')
    escolha_usuario = input('O que deseja fazer?  ')
    escolha_usuario = str(escolha_usuario)

    if escolha_usuario.lower() == "voltar":
        limpar_tela()
        return 1

    elif escolha_usuario.lower() == "logout":
        limpar_tela()
        return 2

    elif escolha_usuario.lower() == "sair":
        limpar_tela()
        print('')
        print('Você saiu do programa.')
        exit()

    else:
        limpar_tela()
        print('')
        print('Você não digitou uma das opções válidas.')
        return 3

def aplica_voltar(): #Opera a funçao voltar
    estado_voltar = voltar()

    if estado_voltar == 1:
        menu()

    elif estado_voltar == 2:
        checar_cadastro()

    else:
        aplica_voltar()

#Precisamos de algo para validar a entrada de números apenas
def validar_numero(mensagem): #Confirma que so existam numeros em inputs numerais
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada

        except ValueError:
            limpar_tela()
            print('')
            print("Por favor, insira apenas números.")

def checar_cadastro(): #Verifica se o usuário é ou não cadstrado
    print('')
    print('|||||||||||||||||||||||||  Angel Care  ||||||||||||||||||||||||||||')
    print('|||||||||| Bem-vindo ao nosso sistema de atendimento pessoal |||||||||')
    print('')
    print('-----------------| Você já possui cadastro? |----------------------')
    print('')
    
    possui_cadastro = input("Sim, Não:   ")

    if possui_cadastro.lower() == "sim":
        limpar_tela()
        print('')
        email = input("Seja bem-vindo. Por favor, indique seu e-mail:  ")
        print('')
        senha = input("Certo, agora digite sua senha:  ")

        #Aqui deve ser chamada a função de validação
        
                limpar_tela()
                print('')
                print('Login bem-sucedido!')
                
                return dados_usuario
            else:
                limpar_tela()
                print('')
                print('E-mail ou senha incorretos. Tente novamente.')
                
        else:
            limpar_tela()
            print('')
            print('Não há dados de cadastro encontrados. Realize o cadastro primeiro.')
            

    elif possui_cadastro.lower() == "nao":
        limpar_tela()
       
    else:
        limpar_tela()
        print('')
        print("Para selecionar as opções, digite Sim ou Não")
        
def intencao_cadastro(): #Verifica se o usuario quer se cadastrar
    limpar_tela()

    print('')
    print("Será necessário fazer seu cadastro. Você concorda em se cadastrar?")
    intencao = input("Sim, Não?   ")
    intencao = str(intencao)

    limpar_tela()

    if intencao.lower() == "sim":
        limpar_tela()
        reg_email(dados_usuario)

    elif intencao.lower() == "nao":
        limpar_tela()

        print('')
        print('Sem problemas, quando quiser, estaremos à disposição!')
        print()
        print('Você saiu do programa')
        print()
        exit()

    else:
        limpar_tela()

        print('')
        print("Para selecionar as opções, digite Sim ou Não")
        intencao_cadastro()

#Partes de Registro do usuário devem vir aqui em baixo

def reg_cpf(dados_usuario): #Recebe e verifica cpf
    limpar_tela()
    
    blocklist = [
    '00000000000',
    '11111111111',
    '22222222222',
    '33333333333',
    '44444444444',
    '55555555555',
    '66666666666',
    '77777777777',
    '88888888888',
    '99999999999'
    ]

    while True:

        print('')
        cpf = input(' Por favor nos informe seu cpf: ')
        cpf_sem_ponto = cpf.replace('.', '')
        cpf = cpf_sem_ponto.replace('-', '')
        
        if cpf.isnumeric():
        
            if len(cpf) == 11:
                
                if cpf in blocklist:
                    limpar_tela()

                    print('')
                    print('O CPF não pode ter todos os números iguais!\n')
                    reg_cpf()
                
                else:
                    
                    if validar_cpf(cpf):
                        limpar_tela()

                        print('')
                        print('CPF cadastrado com sucesso\n')
                        guardar_dados('CPF', cpf, dados_usuario)
                        reg_sus(dados_usuario)
                        return cpf

                    else:
                        limpar_tela()

                        print('')
                        print(' CPF Inválido!\n')
                        reg_cpf()
                        
            else:
                limpar_tela()

                print('')
                print('> O número de CPF deve ter 11 dígitos!\n')
                reg_cpf()     
        
        else:
            limpar_tela()

            print('')
            print('Digite apenas números e digitos especiais do cpf como (. e -).\n')
            reg_cpf()

def validar_cpf(cpf): #valida cpf recebido
        corpo_cpf = cpf[:9]
        digito_cpf = cpf[-2:]

        calculo_1 = 0
        calculo_2 = 0
        
        multiplicacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        
        for i, j in zip(multiplicacao, corpo_cpf):
            calculo_1 += i * int(j)
        #print(f'Cálculo 1: {calculo_1}')
        
        resto_1 = calculo_1 % 11
        #print(f'Resto 1: {resto_1}')
        
        digito_1 = 0 if resto_1 < 2 else 11 - resto_1
        #print(f'Dígito 1: {digito_1}\n')
        
        corpo_cpf += str(digito_1)
        
        for i, j in zip(multiplicacao, corpo_cpf[1:]):
            calculo_2 += i * int(j)
        
        #print(f'Cálculo 2: {calculo_2}')
        
        resto_2 = calculo_2 % 11
        #print(f'Resto 2: {resto_2}')
        
        digito_2 = 0 if resto_2 < 2 else 11 - resto_2
        #print(f'Dígito 2: {digito_2}')
        
        return digito_cpf == f'{digito_1}{digito_2}'

def reg_sus(dados_usuario): #recebe e salva o cartão do sus
    print('')
    sus = validar_numero('Digite apenas os números do seu cartão SUS, caso não tenha, digite 0: ')
    sus = int(sus)

    if sus == 0:
        limpar_tela()

        print('')
        print('Sem problemas, seguiremos para o próximo passo! ')
        reg_endereco(dados_usuario)

    else:
        limpar_tela()

        print('')
        print('Número SUS cadastrado com sucesso')
        guardar_dados('Numero Carteira SUS', sus, dados_usuario)
        reg_endereco(dados_usuario)
        return sus

