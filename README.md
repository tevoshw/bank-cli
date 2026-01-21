# Bank CLI – Sistema de Login em Python

Este projeto é um **sistema simples de login e criação de contas em CLI (Command Line Interface)**, desenvolvido em **Python**, utilizando **SQLite** como **único banco de dados** para persistência das informações.

O objetivo principal **não é criar um sistema bancário real**, mas sim **treinar e consolidar conceitos fundamentais** de desenvolvimento.

---

## Objetivos do projeto

Este projeto foi criado com fins **educacionais**, para praticar:

- Python
- SQLite (CRUD e consultas SQL)
- Programação Orientada a Objetos (POO)
- Lógica de autenticação (login e criação de conta)
- Git e GitHub (versionamento e colaboração)
- Organização de projetos em Python
- Desenvolvimento de aplicações em CLI

---

## Funcionalidades

- Criar conta de usuário
- Login de usuário
- Persistência de dados com **SQLite**
- Interface via terminal (CLI)

---

## Tecnologias utilizadas

- **Python 3**
- **SQLite3** (banco de dados local)
- **Git**
- **GitHub**

> Todo o sistema de dados do projeto é feito **exclusivamente com SQLite**, sem uso de bancos externos.

---

## Estrutura do projeto

```text
bank-cli/
│
├── bank/
│   ├── data.py            # Inicializa o banco de dados e cria as tabelas
│   ├── services.py        # Lógica principal do sistema
│   ├── validation.py      # Regras de login e validações
│   └── database.db        # Banco SQLite (ignorado pelo Git)
│
├── main.py                # Ponto de entrada da aplicação
├── .gitignore
└── README.md
```

## Banco de dados (SQLite)

O arquivo `data.py` é responsável por:

- Criar o arquivo `database.db` automaticamente
- Criar a tabela principal do sistema (`bank`)
- Garantir que o banco exista antes de qualquer operação

### Responsabilidades do `data.py`

- Inicialização do banco de dados
- Criação de tabelas utilizando `CREATE TABLE IF NOT EXISTS`
- Configuração básica do SQLite

O banco de dados é criado automaticamente na **primeira execução do projeto**.

> O arquivo `.db` não é versionado no Git, pois é específico de cada ambiente local.

---

## Participantes

- **tevoshw**
- **JvcCoding**

---

## Observações

- O banco de dados é local e criado automaticamente
- Cada usuário gera seu próprio arquivo `.db`
- O projeto não utiliza frameworks externos
- Projeto desenvolvido exclusivamente para **aprendizado**

---

## ▶️ Como executar

```bash
python main.py


