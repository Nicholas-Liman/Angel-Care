# 📘 Documentação – Sistema de Cadastro e Login em Python (Menu Interativo)

### Objetivo:
Este script simula um sistema de cadastro e login com menus interativos em Python, com foco em aprendizado acadêmico. Os dados são armazenados em formato JSON para simular persistência.

---

## 🔧 Estrutura Geral

O código é dividido em funções que:

- Realizam **cadastro e login** de usuários.
- Validam **dados sensíveis** como CPF e número do SUS.
- Salvam e recuperam dados de um **arquivo JSON**.
- Controlam a navegação por menus.

---

## 📂 Funções por Categoria

### Utilitários

#### `limpar_tela()`
Limpa o terminal, compatível com Windows e Unix.

#### `validar_numero(mensagem)`
Garante que o usuário digite apenas números. Usado em entradas como o número do SUS.

#### `guardar_dados(nome_funcao, retorno, dados_usuario)`
Adiciona os dados coletados ao dicionário `dados_usuario` com a chave correspondente.

---

### Manipulação de Arquivos

#### `salvar_dados_arquivo(nome_arquivo, dados)`
Salva um dicionário de dados no arquivo JSON. Impede cadastros duplicados com base no e-mail.

#### `ler_dados(nome_arquivo)`
Lê os dados do arquivo JSON e retorna como dicionário. Se não existir, retorna `{}`.

---

### Controle de Navegação

#### `voltar()`
Exibe opções para "Voltar", "Logout" ou "Sair". Retorna um número que define a ação seguinte.

#### `aplica_voltar(dados_usuario)`
Executa ações com base na escolha do `voltar()`. Redireciona ao menu ou reinicia o login.

---

### Login e Cadastro

#### `checar_cadastro(dados_usuario)`
Pergunta ao usuário se ele já é cadastrado. Se sim, verifica e-mail/senha no arquivo. Se não, retorna `{}`.

#### `intencao_cadastro(dados_usuario)`
Verifica se o usuário deseja se cadastrar. Se não, encerra o programa.

---

## 🧾 Fluxo de Cadastro

As funções abaixo são chamadas sequencialmente para capturar e validar dados do usuário:

### `reg_email(dados_usuario)`
Coleta e confirma o e-mail do usuário.

### `reg_senha(dados_usuario)`
Coleta e confirma a senha do usuário.

### `reg_cpf(dados_usuario)`
Valida o CPF (incluindo tamanho e dígitos verificadores). Rejeita CPFs com todos os números iguais.

#### `validar_cpf(cpf)`
Aplica o algoritmo de validação de CPF com cálculo dos dígitos verificadores.

### `reg_sus(dados_usuario)`
Coleta e valida o número do Cartão SUS (15 dígitos). Aceita "0" como ausência.

### `reg_endereco(dados_usuario)`
Função ainda não fornecida no código, mas deve finalizar o processo de cadastro com os dados de endereço.

---

## 📁 Exemplo de Arquivo JSON (`cadastro_usuario.json`)

```json
{
  "usuario@exemplo.com": {
    "E-mail": "usuario@exemplo.com",
    "Senha": "123456",
    "CPF": "12345678901",
    "Numero Carteira SUS": "000000000000000"
  }
}
```

---

## ✅ Considerações

- Código adequado para simulação de **fluxos de cadastro/login** com dados validados.
- Utiliza boas práticas como confirmação de entrada e verificação de duplicidade.
- Pode ser expandido com **menus gráficos** (ex: usando `tkinter`) ou com **testes automatizados**.

---
Feito por **Nicholas Lima** como caso de estudo
