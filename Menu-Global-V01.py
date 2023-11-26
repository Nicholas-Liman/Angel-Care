import sys, subprocess

def voltar(): #Inputs de navegação voltar
    
    print('')
    print('Caso deseje voltar a seleção do portal, digite "Voltar"')
    print('')
    print('Caso deseje deslogar e voltar ao início, digite "Logout"')
    print('')
    print('Caso deseje sair, digite sair "Sair"')
    print('')
    intenção_voltar = input('O que deseja fazer?  ')
    intenção_voltar = str(intenção_voltar)
        
    if intenção_voltar.lower() == "voltar":
        subprocess.run('cls', shell=True)
        estado_voltar = 1
        estado_voltar = int(estado_voltar)
        
    elif intenção_voltar.lower() == "logout":
        subprocess.run('cls', shell=True)
        estado_voltar = 2
        estado_voltar = int(estado_voltar)
        
    elif intenção_voltar.lower() == "sair":
        subprocess.run('cls', shell=True)
        print('')
        print('Você saiu do programa')
        exit()
        
    else:
        subprocess.run('cls', shell=True)
        print('')
        print('Você não digitou uma das opções validas')
        estado_voltar = 3
    
    return estado_voltar
    
def escolha_voltar(): # função de voltar
    estado_voltar = voltar()

    if estado_voltar == 1:
        print()
    
    elif estado_voltar == 2:
        cheque_cadastro()
    
    else:
        escolha_voltar()

def cheque_numero(numero): #Função validar número 
    while True:
        try:
            entrada = int(input(numero))
            return entrada
        
        except ValueError:
            subprocess.run('cls', shell=True)
            print('')
            print("Por favor, insira apenas números")
                       
def cheque_cadastro(): #Checa se o usuário é cadastrado ou não
    print('|||||||||||||||||||||||||  Angel Care  ||||||||||||||||||||||||||||')
    print('|||||||||| Bem vindo ao nosso sistema atendimento pessoal |||||||||')
    print('')
    print('-----------------| Você já possuí cadastro? |----------------------')
    print('')

    possui_cadastro = input("Sim, Nao:   ")
    possui_cadastro = str(possui_cadastro)

    estado_cadastro = 2
    estado_cadastro = int(estado_cadastro)
        
    if possui_cadastro.lower() == "sim":  #Usuário Cadastrado (Step-1)
        subprocess.run('cls', shell=True)
        
        print('')
        user = input("Seja bem vindo. Por favor indique seu e-mail:  ")
        print('')
        senha = input("Certo, agora digite sua senha:  ")
        user = str(user)
        senha = str(senha)

        estado_cadastro = 1
    
        return estado_cadastro, senha, user

    elif possui_cadastro.lower() == "nao":  #Usuário não Cadastrado (Step-1)
        subprocess.run('cls', shell=True)
        
        return estado_cadastro
    
    else: #Usuário digitou errado (Step-1)
        subprocess.run('cls', shell=True)

        print('')
        print("Para selecionar as opções digite Sim ou Nao")
        cheque_cadastro()

def intenção_cadastro(): #Checa se o usuário quer se cadastrar
    subprocess.run('cls', shell=True)
    
    print('')
    print("Será necessário fazer seu cadastro, você concorda em se cadastrar?")
    intenção = input("Sim, Nao?   ")
    intenção = str(intenção)
    
    subprocess.run('cls', shell=True)
    
    if intenção.lower() == "sim":
        subprocess.run('cls', shell=True)
        
    
    elif intenção.lower() == "nao":
        subprocess.run('cls', shell=True)
        
        print('')
        print('Sem problemas, quando quiser, estaremos a disposição!')
        print()
        print('Você saiu do programa')
        print()
        exit()

    else: #Usuário digitou errado (Step-1)
        subprocess.run('cls', shell=True)

        print('')
        print("Para selecionar as opções digite Sim ou Nao")
        intenção_cadastro()
