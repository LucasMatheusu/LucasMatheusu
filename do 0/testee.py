def exibir_tabela_onibus (onibus):
    print("\nTabela de Ônibus:")
    print(f"{'0':<5} {'sao paulo':<20} {'9;00':<15} {'100':<10}")
    print("-" * 50)
    for i, (destino, hora_partida, preco) in enumerate(onibus, start=1):
        print(f"{i:<5} {destino:<20} {hora_partida:<15} {preco:<10}")
    print("-" * 50)


def selecionar_onibus(onibus):
    while True:
        exibir_tabela_onibus(onibus)
        try:
            escolha = int(input("\nDigite o ID do ônibus que você deseja viajar (ou 0 para sair): "))
            if escolha == 0:
                print("Saindo...")
                break
            elif 1 <= escolha <= len(onibus):
                destino, hora_partida, preco = onibus[escolha - 1]
                print(f"\nVocê selecionou o ônibus para {destino} com partida às {hora_partida} e o preço é {preco}.")
            else:
                print("ID inválido. Por favor, escolha um ID válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


# Dados dos ônibus
onibus = [
    ("São Paulo", "08:00", "R$ 120,00"),
    ("Rio de Janeiro", "10:00", "R$ 150,00"),
    ("Belo Horizonte", "12:00", "R$ 100,00"),
    ("Curitiba", "14:00", "R$ 140,00")
]
# Executar a função de seleção
selecionar_onibus(onibus)