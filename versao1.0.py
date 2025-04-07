##ajeitar usuarios

def login():
    print("\n--- LOGIN ---")
    user = input("Usuário: ")
    senha = input("Senha: ")
    if user in usuarios and usuarios[user] == senha:
        print("LOGIN BEM-SUCEDIDO!\n")
        return True
    else:
        print("❌ Usuário ou senha incorretos.\n")
        return False

def adicionar_funcionario():
    print("\n--- CADASTRAR NOVO FUNCIONÁRIO ---")
    novo_user = input("Novo usuário: ")
    if novo_user in usuarios:
        print("Usuário já existe!")
        return
    nova_senha = input("Nova senha: ")
    usuarios[novo_user] = nova_senha
    salvar_dados(##arquivo pra salvar, usuarios)
    print("Usuário cadastrado com sucesso!\n")

