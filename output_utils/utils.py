import subprocess


def ask_for_output(output):
    generate_output = input("Deseja gerar uma saída? (S/N): ").strip().lower()
    if generate_output == 's':
        output_file = input("Digite o nome do arquivo de saída: ").strip()
        with open(output_file, 'w') as f:
            f.write(output)
            print(f"Saida salva em '{output_file}'\n")
    elif generate_output != 'n':
        print("Opção inválida. Saida não gerada.")
    else:
        print("")


def execute_command(command):
    try:
        print("Comando executado: {}".format(" ".join(command)))
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)

        ask_for_output(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e.output}")
