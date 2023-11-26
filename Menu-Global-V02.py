import sys
import subprocess
import json

def limpar_tela(): #Funçao limpar tela universal
    subprocess.run(['cls' if sys.platform == 'win32' else 'clear'], shell=True)

#Precisa de uma função para guardar e ler os dados do registro/Login em json

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

#Maria Por favor colocar a parte de verificação de cpf que vc fez em aula aqui


