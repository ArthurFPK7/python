# print ("Hello world, Python!")

import os

# restaurantes=['PythonBurguer', 'Madalosso', 'Notubo']
# dicionário
restaurantes=[  {'nome':'Pão com Banha','categoria':'Gourmet','ativo':False},
                {'nome':'Saco de Feijão','categoria':'Feijoada','ativo':True},
                {'nome':'Bife Sujo','categoria':'Churrascaria','ativo':False}
            ]

def exibir_nome_do_programa():
    print('𝕊𝕒𝕓𝕠𝕣 𝕖𝕩𝕡𝕣𝕖𝕤𝕤')
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()
    
def opcao_invalida():
    print('Opção invalida\n')
    voltar_menu_principal()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('CADASTRO DE NOVOS RESTAURANTES')
    nome_do_restaurante=input('Digite o nome do restaurante que você quer cadastrar')
    categoria = input (f'Digite a categoria do restaurante:' {nome_do_restaurante})
    dados_do_restaurante = ('nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False)
    restaurantes.append(nome_do_restaurante)
    print(f'O Restaurante {nome_restaurante} foi cadastrado com sucesso')
    voltar_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('LISTANDO RESTAURANTES')
    
    for restaurante in restaurantes:
        nome_restaurante=restaurante
        categoria=restaurante['categoria']
        ativo=retaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}' )

def finalizar_app():
    exibir_subtitulo('Finalizar app')
    
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
    
def escolher_opcao():
    try:
        opcao_escolhida=int(input('Escolha uma opção: '))
        
        if opcao_escolhida==1:
            # print('Você escolheu cadastrar um restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida==2:
            # print('Você escolheu listar os restaurantes')
            listar_restaurantes()
        elif opcao_escolhida==3:
            print('Ativar restaurante')
        else: 
            opcao_invalida()
    except: 
        opcao_invalida()
        
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__=='__main__':
    main()