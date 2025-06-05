from usuarios import login, adicionar_usuario, inicializar_admin, deletar_usuario, alterar_usuario
from veiculos import cadastrar_veiculo, listar_veiculos_com_usuario


def menu_principal():
    while True:
        print("==== MENU PRINCIPAL ====")
        print("1. Cadastrar veículo")
        print("2. Listar veículos")
        print("3. Deletar usuário")
        print("4. Alterar usuário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_veiculo()
        elif opcao == '2':
            listar_veiculos_com_usuario()
        elif opcao == '3':
            deletar_usuario()
        elif opcao == '4':
            alterar_usuario()
        elif opcao == '5':
            print("Encerrando sessão.\n")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

def menu_inicial():
    inicializar_admin()  
    while True:
        print("==== BEM-VINDO AO ESTACIONAMENTO PARK KEY ====")
        print("1. Entrar (Login)")
        print("2. Cadastrar novo funcionário")
        print("3. Deletar usuário")
        print("4. Alterar usuário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            if login():
                menu_principal()
        elif opcao == '2':
            adicionar_usuario()
        elif opcao == '3':
            deletar_usuario()
        elif opcao == '4':
            alterar_usuario()
        elif opcao == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu_inicial()
