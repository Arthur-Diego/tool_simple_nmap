import subprocess
from colorama import Fore, Style


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


# command: É uma lista contendo o comando e seus argumentos. Por exemplo, ["nmap", "-PE", "-sn", "192.168.1.1-192.168.1.254"].
# stdout=subprocess.PIPE: Redireciona a saída padrão do processo para um pipe, permitindo que o código Python leia a saída.
# stderr=subprocess.STDOUT: Redireciona a saída de erro padrão para o mesmo pipe usado para a saída padrão, unificando as duas saídas.
# universal_newlines=True: Faz com que a saída seja tratada como texto, independentemente do sistema operacional.
def execute_command(command):
    output_lines = []
    try:
        print("Comando executado:", Fore.MAGENTA + "{}".format(" ".join(command)) + Style.RESET_ALL)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        for line in process.stdout:
            output_lines.append(line.strip())
            print(line.strip())

        ask_for_output('\n'.join(output_lines))
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e.output}")
