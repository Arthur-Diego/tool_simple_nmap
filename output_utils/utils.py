
def ask_for_output(output):
    generate_output = input("Deseja gerar uma saída? (S/N): ").strip().lower()
    if generate_output == 's':
        output_file = input("Digite o nome do arquivo de saída: ").strip()
        with open(output_file, 'w') as f:
            f.write(output)
            print(f"Saida salva em '{output_file}'")
    elif generate_output != 'n':
        print("Opção inválida. Saida não gerada.")
    else:
        print("Nao foi possível gerar o arquivo")
