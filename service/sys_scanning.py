import subprocess


def syn_scan_menu():
    print("Escolha uma opção de varredura SYN:")
    print("1. Varredura SYN em um único host")
    print("2. Varredura SYN em uma faixa de IPs")
    print("3. Varredura SYN em várias portas específicas")
    print("4. Varredura SYN em todas as portas comuns")
    print("5. Varredura SYN com detecção de serviços e versões")

    choice = input("Escolha uma opção (1-5): ")

    if choice == '1':
        host = input("Digite o endereço IP do host: ")
        syn_scan(host)
    elif choice == '2':
        ip_range = input("Digite a faixa de IPs (exemplo: 192.168.1.1-100): ")
        syn_scan(ip_range)
    elif choice == '3':
        host = input("Digite o endereço IP do host: ")
        ports = input("Digite as portas que deseja escanear (exemplo: 80,443): ")
        syn_scan(host, ports)
    elif choice == '4':
        host = input("Digite o endereço IP do host: ")
        syn_scan(host, "-")
    elif choice == '5':
        host = input("Digite o endereço IP do host: ")
        syn_scan(host, "-sV")
    else:
        print("Opção inválida.")


def syn_scan(target, options=""):
    command = ["nmap", "-sS", options, target]
    execute_nmap_scan(command)


def execute_nmap_scan(command):
    try:
        print("Comando executado: {}".format(" ".join(command)))
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e.output}")
    except KeyboardInterrupt:
        print("Comando interrompido pelo usuário.")