import sys
import subprocess
import json

def limpar_tela(): #Funçao limpar tela universal
    subprocess.run(['cls' if sys.platform == 'win32' else 'clear'], shell=True)

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

def aplica_voltar(dados_usuario): #Opera a funçao voltar
    estado_voltar = voltar()

    if estado_voltar == 1:
        menu(dados_usuario)

    elif estado_voltar == 2:
        checar_cadastro(ler_dados)

    else:
        aplica_voltar(dados_usuario)

def validar_numero(mensagem): #Confirma que so existam numeros em inputs numerais
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada

        except ValueError:
            limpar_tela()
            print('')
            print("Por favor, insira apenas números.")
            print('')

def checar_cadastro(dados_usuario): #Verifica se o usuário é ou não cadstrado
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

        # Load existing user data from the file
        dados_armazenados = ler_dados('informacoes_de_login.json')

        if dados_armazenados is not None and 'E-mail' in dados_armazenados and 'Senha' in dados_armazenados:
            if email == dados_armazenados['E-mail'] and senha == dados_armazenados['Senha']:
                limpar_tela()
                print('')
                print('Login bem-sucedido!')
                dados_usuario.update(dados_armazenados)  # Update dados_usuario with existing data
                
                return dados_usuario
            else:
                limpar_tela()
                print('')
                print('E-mail ou senha incorretos. Tente novamente.')
                return checar_cadastro(dados_usuario)
        else:
            limpar_tela()
            print('')
            print('Não há dados de cadastro encontrados. Realize o cadastro primeiro.')
            return checar_cadastro(dados_usuario)

    elif possui_cadastro.lower() == "nao":
        limpar_tela()
        return dados_usuario

    else:
        limpar_tela()
        print('')
        print("Para selecionar as opções, digite Sim ou Não")
        return checar_cadastro(dados_usuario)

def intencao_cadastro(dados_usuario): #Verifica se o usuario quer se cadastrar
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
        intencao_cadastro(dados_usuario)

#Começo do Cadastro

def reg_email(dados_usuario): #Recebe e verifica email
    
    print('')
    email = input("Por favor, indique seu e-mail:  ")
    
    limpar_tela()
    
    print('')
    email2 = input("Agora confirme seu e-mail:  ")
    
    limpar_tela()
    
    if email == email2:
        print('')
        print('Seu e-mail foi cadastrado com sucesso')
        guardar_dados('E-mail', email, dados_usuario)
        reg_senha(dados_usuario)
    else:
        print('')
        print('Os e-mails digitados são diferentes')
        reg_email(dados_usuario)

def reg_senha(dados_usuario): #Recebe e verifica senha
    
    print('')
    senha = input("Por favor crie uma senha:  ")
    
    limpar_tela()
    
    print('')
    senha2 = input("Agora confirme sua senha:  ")
    
    limpar_tela()
    
    if senha == senha2:
        print('')
        print('Sua senha foi registrada com sucesso')
        guardar_dados('Senha', senha, dados_usuario)
        reg_cpf(dados_usuario)
    else:
        limpar_tela()
        
        print('')
        print('As senhas digitadas são diferentes')
        reg_senha(dados_usuario)
        
def reg_cpf(dados_usuario): #Recebe e verifica cpf
    
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
        cpf = input('Por favor nos informe seu cpf: ')
        cpf_sem_ponto = cpf.replace('.', '')
        cpf = cpf_sem_ponto.replace('-', '')
        
        limpar_tela()
        
        if cpf.isnumeric():
        
            if len(cpf) == 11:
                
                if cpf in blocklist:
                    limpar_tela()

                    print('')
                    print('O CPF não pode ter todos os números iguais!\n')
                    reg_cpf(dados_usuario)
                
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
                        reg_cpf(dados_usuario)
                        
            else:
                limpar_tela()

                print('')
                print('O número de CPF deve ter 11 dígitos!\n')
                reg_cpf(dados_usuario)     
        
        else:
            limpar_tela()

            print('')
            print('Digite apenas números e digitos especiais do cpf como (. e -).\n')
            reg_cpf(dados_usuario)

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
    sus = str(sus)


    if len(sus) != 15:
        limpar_tela()
        print('')
        print('Número SUS inválido')
        reg_sus(dados_usuario)
        
        
    else:
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
    
def reg_endereco(dados_usuario): #Recebe e verifica endereco
    print('')
    endereco = input("Por favor, indique seu endereço:  ")
    print('')
    
    limpar_tela()
    
    print('Endereço cadastrado com sucesso')
    guardar_dados('Endereco', endereco, dados_usuario)
    salvar_dados_arquivo('informacoes_de_login.json', dados_usuario)
    logar(dados_usuario)

#Fim do Cadastro

def logar(dados_usuario): #Verifica se o usuario quer logar depois de se cadastrar
    print('')
    print('Gostaria de fazer o login?')
    login = input("Sim, Nao? ")
    if login.lower() == "sim":
        limpar_tela()
        manuseio_login(dados_usuario)
    elif login.lower() == "nao":
        limpar_tela()
        print('')
        print('Sem problemas, quando quiser, estaremos a disposição!')
        print()
        print('Você saiu do programa')
        print()
        exit()
    else:
        limpar_tela()
        print('')
        print("Para selecionar as opções digite Sim ou Nao")
        logar(dados_usuario)

def portal(): #Função Portal

    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print('|||||||||||||||||||||||||| Angel Care |||||||||||||||||||||||||||||')
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print('|||||||||||||||||| Bem vindo ao nosso portal ||||||||||||||||||||||')
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print('||||||||||||||| Qual serviço você deseja acessar?||||||||||||||||||')
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print('|                                                                 |')
    print('|||||| Para selecionar digite o número respectivo ao serviço  |||||')
    print('|                                                                 |')
    print('|-----------------------------------------------------------------|')
    print('|(1)| - Atendimento Presencial                                    |')
    print('|-----------------------------------------------------------------|')
    print('|(2)| - Atendimento Online                                        |')
    print('|-----------------------------------------------------------------|')
    print('|(3)| - Triagem Digital                                           |')
    print('')

    #Input da Escolha (Step-2)
    #select = int(select)
    select = validar_numero('Digite o número do serviço: ')

    limpar_tela()

    #Filtro da Escolha (Step-2)
    if  select == 1:
        limpar_tela()
        intenção = 1
        return intenção

    elif select == 2:
        limpar_tela()
        intenção = 2
        return intenção

    elif select == 3:
        limpar_tela()
        intenção = 3
        return intenção
        
    else:
        limpar_tela()
        print('')
        print('Para selecionar as opções, digite apenas o NÚMERO respectivo à opção')
        print('')
        portal()

def presencial(dados_usuario): #Função consulta presencial
    limpar_tela()
    
    print('')
    print('|||| Bem vindo ao portal de agendamento presencial Angel Care ||||')
    print('||||||||| Essas são as localizações mais próximas de você ||||||||') 
    
    #Quando o menu tiver conexão com backend, ele irá visualizar o endereço de cadastro e irá procurar clinicas parceiras próximas da região.
    aplica_voltar(dados_usuario)

def online(dados_usuario): #Função consulta online
    limpar_tela()
    
    print('')
    print('|||| Bem vindo ao portal de agendamento online Angel Care ||||')
    print('')
    print('Esses são os nossos profissionais, por favor veja os horários disponiveis e suas especialidades e marque sua consulta') 
    
    #Quando o menu tiver conexão com backend, ele irá visualizar o nome, disponibilidade e especialidade dos médicos.
    aplica_voltar(dados_usuario)

def triagem(dados_usuario): #Função consulta presencial
    
    print('||||||||||||| Bem vindo a Triagem digital Angel Care ||||||||||||||')
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print('|||||||||||||| Nos informe o seu sintoma mais sério |||||||||||||||')
    print('|||||||||||||| Ou o que mais se encaixa no momento  |||||||||||||||')
    print('|                                                                 |')
    print('|||||| Para selecionar digite o número respectivo do sintoma  |||||')
    print('|                                                                 |')
    print('|-----------------------------------------------------------------|')
    print('')

    print('|(1)| Azul: Dor crônica já diagnosticada, troca de curativos ou aplicação de medicação com receita                                    |')
    print('')

    print('|(2)| Verde: Febre baixa, hemorragia sob controle, dores leves, resfriados ou viroses                                                 |')
    print('')

    print('|(3)| Amarelo: Picos de hipertensão, hemorragias moderadas, sinais vitais irregulares, vômito intenso ou desmaios                     |')
    print('')

    print('|(4)| Laranja: Arritmia, cefaléia intensa, suspeita de AVC ou dor severa                                                              |')
    print('')

    print('|(5)| Vermelho: Queimaduras em mais de 25% do corpo, parada cardiorespiratória, problemas respiratórios, convulsão ou traumatismo     |')
    print('')

    select = validar_numero('Digite o número do serviço: ')


    #Filtro da Escolha (Step-2)
    if  select == 1:
        limpar_tela()
        print('Estes casos aceitam até quatro horas de espera para atendimento, segundo previsto no método de triagem de Manchester.')
        

    elif select == 2:
        limpar_tela()
        print('Seguindo o padrão do processo de triagem, o tempo de espera desses pacientes pode ser de, no máximo, duas horas.')

    elif select == 3:
        limpar_tela()
        print('Para os pacientes identificados pela cor amarela, o tempo de espera admitido pelo protocolo é de até 50 minutos.')
              
    
    elif select == 4:
       limpar_tela()
       print('Segundo definido pelo protocolo, o tempo médio de espera aceitável para esse tipo de quadro clínico é de até 10 minutos.')
        
    
    elif select == 5:
        limpar_tela()
        print('Nestes casos, o atendimento deve ser realizado de forma imediata. ')
        
        
    else:
        limpar_tela()
        print('Para selecionar as opções, digite apenas o NÚMERO respectivo à opção')
        triagem(dados_usuario)
     
    
    #Quando o menu tiver conexão com backend, o usuario sera redirecionado ao nosso chatbot de triagem
    aplica_voltar(dados_usuario)

def menu(dados_usuario): #Manuseia a função portal
    limpar_tela()
    intencao = portal()

    if intencao == 1:
        presencial(dados_usuario)
    elif intencao == 2:
        online(dados_usuario)
    else:
        triagem(dados_usuario)
        
    return dados_usuario

def manuseio_login(dados_usuario): #Função main que manipula as associadas
    dados_usuario = checar_cadastro(dados_usuario)
    if 'E-mail' not in dados_usuario:
        intencao_cadastro(dados_usuario)
    menu(dados_usuario)

manuseio_login({})

#Mesmo não tendo conectividade com o backend ou banco de dados, nosso código retorna:
#E-mail e senha de usuários já cadastrados, para enviar e verificar com o banco
#Todas as informações de cadastro, como E-mail, senha, CPF, cartão SUS, endereço, para serem salvos no banco
