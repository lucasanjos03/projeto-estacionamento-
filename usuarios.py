import bcrypt
from conexao import conectar

def inicializar_admin():
    
    try:
        conn = conectar()
        if not conn:
            return
        cur = conn.cursor()
        
        cur.execute("SELECT id_funcionario FROM funcionarios WHERE usuario = 'admin'")
        if not cur.fetchone():
            senha_hash = bcrypt.hashpw('1234'.encode(), bcrypt.gensalt()).decode()
            cur.execute(
                "INSERT INTO funcionarios (usuario, senha) VALUES (%s, %s)",
                ('admin', senha_hash)
            )
            conn.commit()
        cur.close()
    except Exception as e:
        print("Erro ao inicializar administrador:", e)
    finally:
        if conn:
            conn.close()

def login(return_user=False):
    
    print("\n--- LOGIN ---")
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    try:
        conn = conectar()
        if not conn:
            return False if not return_user else None
        cur = conn.cursor()

        cur.execute(
            "SELECT senha FROM funcionarios WHERE usuario = %s",
            (usuario,)
        )
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row and bcrypt.checkpw(senha.encode(), row[0].encode()):
            print("✅ Login bem-sucedido!\n")
            return usuario if return_user else True
        else:
            print("❌ Usuário ou senha incorretos.\n")
            return False if not return_user else None

    except Exception as e:
        print("Erro no login:", e)
        return False if not return_user else None

def adicionar_usuario():
    
    print("\n--- CADASTRAR NOVO FUNCIONÁRIO ---")
    usuario = input("Novo usuário: ").strip()

    try:
        conn = conectar()
        if not conn:
            return
        cur = conn.cursor()

        
        cur.execute("SELECT 1 FROM funcionarios WHERE usuario = %s", (usuario,))
        if cur.fetchone():
            print("⚠️ Usuário já existe!\n")
            cur.close()
            conn.close()
            return

        senha = input("Nova senha: ").strip()
        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
        cur.execute(
            "INSERT INTO funcionarios (usuario, senha) VALUES (%s, %s)",
            (usuario, senha_hash)
        )
        conn.commit()
        cur.close()
        conn.close()

        print("✅ Funcionário cadastrado com sucesso!\n")

    except Exception as e:
        print("Erro ao cadastrar funcionário:", e)

def deletar_usuario():
    
    print("\n--- DELETAR FUNCIONÁRIO ---")
    usuario = input("Usuário a deletar: ").strip()
    if usuario == 'admin':
        print("⚠️ Não é permitido deletar o usuário 'admin'.\n")
        return

    try:
        conn = conectar()
        if not conn:
            return
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM funcionarios WHERE usuario = %s", (usuario,))
        if not cur.fetchone():
            print("⚠️ Usuário não encontrado.\n")
            cur.close()
            conn.close()
            return

        cur.execute("DELETE FROM funcionarios WHERE usuario = %s", (usuario,))
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Usuário deletado com sucesso!\n")
    except Exception as e:
        print("Erro ao deletar usuário:", e)

def alterar_usuario():
    
    print("\n--- ALTERAR FUNCIONÁRIO ---")
    usuario = input("Usuário a alterar: ").strip()
    if usuario == 'admin':
        print("⚠️ Não é permitido alterar o usuário 'admin'.\n")
        return

    try:
        conn = conectar()
        if not conn:
            return
        cur = conn.cursor()
        cur.execute("SELECT id_funcionario FROM funcionarios WHERE usuario = %s", (usuario,))
        row = cur.fetchone()
        if not row:
            print("⚠️ Usuário não encontrado.\n")
            cur.close()
            conn.close()
            return

        id_funcionario = row[0]
        novo_usuario = input("Novo nome de usuário (deixe em branco para manter): ").strip()
        nova_senha = input("Nova senha (deixe em branco para manter): ").strip()

        if novo_usuario:
            cur.execute("UPDATE funcionarios SET usuario = %s WHERE id_funcionario = %s", (novo_usuario, id_funcionario))
        if nova_senha:
            senha_hash = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt()).decode()
            cur.execute("UPDATE funcionarios SET senha = %s WHERE id_funcionario = %s", (senha_hash, id_funcionario))
        if novo_usuario or nova_senha:
            conn.commit()
            print("✅ Usuário alterado com sucesso!\n")
        else:
            print("Nenhuma alteração realizada.\n")
        cur.close()
        conn.close()
    except Exception as e:
        print("Erro ao alterar usuário:", e)
