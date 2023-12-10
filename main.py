from geral import *
from jornalista import *
from leitor import *

usuarios_cadastrados = [{
        'nome': 'Felipe',
        'email': 'felipe@net.com',
        'senha': '12345a',
        'tipo': 'jornalista',
        'curtidas': []
    },{
        'nome': 'Joao',
        'email': 'joao@net.com',
        'senha': '12345a',
        'tipo': 'jornalista',
        'curtidas': []
    },{
        'nome': 'Rian',
        'email': 'rian@net.com',
        'senha': '12345a',
        'tipo': 'leitor',
        'curtidas': []
    }]
idmateria = [3]
materias = [{
        'id': 1,
        'titulo': 'test',
        'conteudo': 'teste',
        'data': '18/11/2023',
        'autor': 'felipe@net.com',
        'comentarios': list(),
        'curtidas': list()
    },
    {
        'id': 2,
        'titulo': 'flamengo',
        'conteudo': 'o vasco ganhou',
        'data': '18/11/2023',
        'autor': 'felipe@net.com',
        'comentarios': list(),
        'curtidas': ['joao@net.com']
    },
    {
        'id': 3,
        'titulo': 'vasco',
        'conteudo': 'o flamengo ganhou',
        'data': '18/11/2023',
        'autor': 'felipe@net.com',
        'comentarios': list(),
        'curtidas': ['joao@net.com', 'felipe@net.com', 'jose@net.com']
    }
]
usuario_logado = []

while True:

    print("-" * 30)
    print('|          Opções:           |')
    print("-" * 30)
    print('|      1. Cadastrar Usuário  |')
    print('|      2. Fazer login        |')
    print('|      3. Sair               |')
    print("-" * 30)

    opcao = input('Escolha uma opção: ')

    if (opcao == '1'):
        cadastrar(usuarios_cadastrados)

    elif (opcao == '2'):
        fazer_login(usuarios_cadastrados, materias, idmateria)

    elif (opcao == '3'):
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")

