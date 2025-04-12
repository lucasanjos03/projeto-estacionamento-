from armazenamento import carregar_dados, salvar_dados

ARQ_USUARIOS = 'dados/usuarios.json'
usuarios = carregar_dados(ARQ_USUARIOS)

def login():
    print("\n--- LOGIN ---")
    user = input("Usuário: ")
    senha = input("Senha: ")
    if user in usuarios and usuarios[user] == senha:
        print("✅ Login bem-sucedido!\n")
        return True
    else:
        print("❌ Usuário ou senha incorretos.\n")
        return False

def adicionar_usuario():
    print("\n--- CADASTRAR NOVO FUNCIONÁRIO ---")
    novo_user = input("Novo usuário: ")
    if novo_user in usuarios:
        print("⚠️ Usuário já existe!")
        return
    nova_senha = input("Nova senha: ")
    usuarios[novo_user] = nova_senha
    salvar_dados(ARQ_USUARIOS, usuarios)
    print("✅ Usuário cadastrado com sucesso!\n")

def inicializar_admin():
    if not usuarios:
        usuarios['admin'] = '1234'
        salvar_dados(ARQ_USUARIOS, usuarios)
