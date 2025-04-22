from armazenamento import carregar_dados, salvar_dados

ARQ_VEICULOS = 'dados/veiculos.json'
veiculos = carregar_dados(ARQ_VEICULOS)

def cadastrar_veiculo():
    print("\n--- CADASTRAR VEÍCULO ---")
    placa = input("Placa: ").upper()
    if placa in veiculos:
        print("⚠️ Veículo já cadastrado!")
        return

    try:
        cor = input("Cor: ")
        modelo = input("Modelo: ")
        marca = input("Marca: ")
        nome = input("Nome do proprietário: ")
        telefone = int(input("Telefone do proprietário: "))

        if any(char.isdigit() for char in cor + modelo + marca + nome):
            raise ValueError("Campos de texto não devem conter números.")

    except (ValueError, IndexError):
        print("❌ Dados inválidos. Verifique se digitou apenas letras e números corretamente.\n")
        return

    veiculos[placa] = {
        "cor": cor,
        "modelo": modelo,
        "marca": marca,
        "proprietario": {
            "nome": nome,
            "telefone": telefone
        }
    }

    salvar_dados(ARQ_VEICULOS, veiculos)
    print("✅ Veículo cadastrado com sucesso!\n")


    salvar_dados(ARQ_VEICULOS, veiculos)
    print("✅ Veículo cadastrado com sucesso!\n")

def listar_veiculos():
    print("\n--- VEÍCULOS CADASTRADOS ---")
    if not veiculos:
        print("Nenhum veículo cadastrado.")
    else:
        for placa, dados in veiculos.items():
            dono = dados['proprietario']
            print(f"Placa: {placa} | {dados['marca']} {dados['modelo']} - {dados['cor']}")
            print(f"  Proprietário: {dono['nome']} | Telefone: {dono['telefone']}\n")
