from conexao import conectar

def cadastrar_veiculo():
    
    print("\n--- CADASTRAR VEÍCULO ---")

    try:
        conn = conectar()
        if not conn:
            return
        cur = conn.cursor()

        placa = input("Placa do veículo: ").upper().strip()

        
        cur.execute("SELECT 1 FROM carros WHERE placa = %s", (placa,))
        if cur.fetchone():
            print("⚠️ Veículo já cadastrado com essa placa.")
            cur.close()
            conn.close()
            return

        cor = input("Cor: ").strip()
        modelo = input("Modelo: ").strip()
        marca = input("Marca: ").strip()
        nome = input("Nome do proprietário: ").strip()
        telefone = input("Telefone do proprietário (apenas números): ").strip()

        
        cur.execute(
            "INSERT INTO proprietarios (nome, telefone) VALUES (%s, %s) RETURNING id_proprietario",
            (nome, telefone)
        )
        id_proprietario = cur.fetchone()[0]

        
        cur.execute(
            "INSERT INTO carros (id_proprietario, cor, modelo, marca, placa) VALUES (%s, %s, %s, %s, %s)",
            (id_proprietario, cor, modelo, marca, placa)
        )

        conn.commit()
        print("✅ Veículo cadastrado com sucesso!")

    except Exception as e:
        print("❌ Erro ao cadastrar veículo:", e)

    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass

def listar_veiculos():
    
    print("\n--- VEÍCULOS CADASTRADOS ---")

    try:
        conn = conectar()
        if not conn:
            return
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                c.placa,
                c.marca,
                c.modelo,
                c.cor,
                p.nome,
                p.telefone
            FROM carros c
            JOIN proprietarios p ON c.id_proprietario = p.id_proprietario
            ORDER BY c.placa;
        """)
        resultados = cur.fetchall()

        if not resultados:
            print("Nenhum veículo cadastrado.\n")
            cur.close()
            conn.close()
            return

        for placa, marca, modelo, cor, nome, telefone in resultados:
            print(f"Placa: {placa} | {marca} {modelo} - {cor}")
            print(f"  Proprietário: {nome} | Telefone: {telefone}\n")

        cur.close()
        conn.close()

    except Exception as e:
        print("❌ Erro ao listar veículos:", e)

def listar_veiculos_com_usuario():
    
    print("\n--- VEÍCULOS CADASTRADOS ---")
    try:
        conn = conectar()
        if not conn:
            return
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                c.placa,
                c.marca,
                c.modelo,
                c.cor,
                p.nome,
                p.telefone,
                f.usuario
            FROM carros c
            JOIN proprietarios p ON c.id_proprietario = p.id_proprietario
            LEFT JOIN funcionarios f ON c.id_funcionario = f.id_funcionario
            ORDER BY c.placa;
        """)
        resultados = cur.fetchall()

        if not resultados:
            print("Nenhum veículo cadastrado.\n")
            cur.close()
            conn.close()
            return

        for placa, marca, modelo, cor, nome, telefone, usuario in resultados:
            print(f"Placa: {placa} | {marca} {modelo} - {cor} | Usuário: {usuario or 'Desconhecido'}")
            print(f"  Proprietário: {nome} | Telefone: {telefone}\n")

        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Erro ao listar veículos:", e)
