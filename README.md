# project pin

Project Pin

Um projeto inspirado no Pinterest, desenvolvido com Python e Flask, criado como projeto de estudo durante o curso da Hashtag Treinamentos.

Créditos

Este projeto foi desenvolvido acompanhando os conteúdos e conceitos apresentados no curso da Hashtag Treinamentos, servindo como prática para aprendizado de desenvolvimento web com Python e Flask.


Funcionalidades
Cadastro de usuários
Login e logout
Autenticação com Flask-Login
Senhas armazenadas com hash utilizando Flask-Bcrypt
Perfil individual para cada usuário
Upload de imagens
Feed com as imagens publicadas
Armazenamento dos usuários e publicações em SQLite
Validação de formulários com Flask-WTF
Interface web utilizando HTML e CSS
Tecnologias utilizadas
Tecnologia	Utilização
Python	Linguagem principal
Flask	Framework web
Flask-SQLAlchemy	ORM e integração com banco de dados
SQLite	Banco de dados
Flask-Login	Gerenciamento de sessões e autenticação
Flask-Bcrypt	Hash das senhas
Flask-WTF	Formulários e validações
WTForms	Criação dos formulários
HTML5	Estrutura das páginas
CSS3	Estilização
Werkzeug	Tratamento seguro dos nomes dos arquivos
Estrutura do projeto
project-pin/
├── fakepinterest/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── fotos_post/
│   │   │   └── default.png
│   │   └── fotos_site/
│   │       └── fundo-login.png
│   ├── templates/
│   │   ├── criar_conta.html
│   │   ├── feed.html
│   │   ├── homepage.html
│   │   ├── navbar.html
│   │   └── perfil.html
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   └── routes.py
├── instance/
│   └── comunidade.db
├── criar_banco.py
├── main.py
├── README.md
└── requirements.txt
Como executar
1. Clone o repositório
git clone https://github.com/zecytec/project-pin
cd project-pin
2. Crie um ambiente virtual

Windows:

python -m venv venv

Ative o ambiente:

venv\Scripts\activate

Linux/macOS:

python3 -m venv venv
source venv/bin/activate
3. Instale as dependências
pip install -r requirements.txt
4. Execute o projeto
python main.py

Acesse:

http://127.0.0.1:5000
Banco de dados

O projeto utiliza SQLite através do Flask-SQLAlchemy.

O banco está localizado em:

instance/comunidade.db

Caso o banco ainda não exista, o main.py executa automaticamente o criar_banco.py, responsável pela criação das tabelas.

Autenticação

O projeto utiliza Flask-Login para gerenciamento das sessões.

As senhas são protegidas utilizando Flask-Bcrypt, evitando que sejam armazenadas em texto puro no banco de dados.

Upload de imagens

As imagens enviadas pelos usuários são armazenadas em:

fakepinterest/static/fotos_post/

O nome dos arquivos é tratado utilizando secure_filename() do Werkzeug antes do armazenamento.

Utilizado para autenticação através de:

E-mail
Senha
FormCriarConta

Utilizado para criação de contas:

Username
E-mail
Senha
Confirmação de senha

O formulário também verifica se o e-mail já está cadastrado.

FormFoto

Utilizado para realizar o upload de imagens.

Objetivo

O Project Pin foi desenvolvido para praticar conceitos de desenvolvimento web utilizando Python e Flask, incluindo:

Desenvolvimento de aplicações web
Banco de dados relacionais
ORM com SQLAlchemy
Autenticação
Gerenciamento de sessões
Hash de senhas
Upload de arquivos
Validação de formulários
Relacionamentos entre tabelas
HTML e CSS