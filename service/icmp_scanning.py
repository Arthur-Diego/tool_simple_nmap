import subprocess
from ipaddress import ip_address
from colorama import Fore, Style


def icmp_scan_menu():
    print("Escolha uma opção de varredura ICMP:")
    print("1. Ping simples em um único host:", Fore.RED + Style.BRIGHT + "nmap -PE host" + Style.RESET_ALL)
    print("2. Ping em uma faixa de IPs:", Fore.RED + Style.BRIGHT + "nmap -PE ip_range" + Style.RESET_ALL)
    print("3. Ping em uma lista de hosts a partir de um arquivo:",
          Fore.RED + Style.BRIGHT + "nmap -iL file" + Style.RESET_ALL)
    print("4. Ping em um intervalo de IPs:", Fore.RED + Style.BRIGHT + "nmap -PE -sn ip_range" + Style.RESET_ALL)
    print("5. Ping com detecção de hosts vivos:", Fore.RED + Style.BRIGHT + "nmap -sn network" + Style.RESET_ALL)

    choice = input("Escolha uma opção (1-5): ")

    if choice == '1':
        print("----------------------------------")
        print("Ping simples em um único host:\n")
        host = input("Digite o endereço IP do host: ")
        icmp_ping(host)
        print("Ping simples em um único host realizado.")
        print("------------------------------------------")

    elif choice == '2':
        print("-----------------------------------")
        print("Ping em uma faixa de IPs:\n")
        ip_range = input("Digite a faixa de IPs (exemplo: 192.168.1.1-100): ")
        icmp_ping(ip_range)
        print("Ping em uma faixa de IPs realizado.")
        print("------------------------------------------")

    elif choice == '3':
        print("---------------------------------------------------")
        print("Ping em uma lista de hosts a partir de um arquivo:\n")
        hosts_file = input("Digite o caminho do arquivo com a lista de hosts: ")
        icmp_ping_from_file(hosts_file)
        print("Ping em uma lista de hosts realizado.")
        print("---------------------------------------------------")

    elif choice == '4':
        print("--------------------------------------------------")
        print("Ping em um intervalo de IPs:\n")
        start_ip = input("Digite o endereço IP inicial: ")
        end_ip = input("Digite o endereço IP final: ")
        icmp_ping_range(start_ip, end_ip)
        print("Ping em um intervalo de IPs realizado.")
        print("--------------------------------------------------")

    elif choice == '5':
        print("---------------------------------------------")
        print("Ping com detecção de hosts vivos em uma rede:\n")
        network = input("Digite a rede (exemplo: 192.168.1.0/24): ")
        icmp_ping_live_hosts(network)
        print("Ping com detecção de hosts vivos realizado.")
        print("---------------------------------------------")

    else:
        print("Opção inválida.")


def icmp_ping(target, options=""):
    command = ["ping", "-c", "4", target]
    execute_ping(command)


def icmp_ping_from_file(file_path):
    with open(file_path, 'r') as file:
        hosts = file.readlines()
        for host in hosts:
            host = host.strip()
            icmp_ping(host)


def icmp_ping_range(start_ip, end_ip):
    start = ip_address(start_ip)
    end = ip_address(end_ip)

    for ip_int in range(int(start), int(end) + 1):
        ip = ip_address(ip_int)
        icmp_ping(str(ip))


def icmp_ping_live_hosts(network):
    command = ["nmap", "-sn", network]
    execute_nmap_scan(command)


def execute_ping(command):
    try:
        print("Comando executado: {}".format(" ".join(command)))
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e.output}")
    except KeyboardInterrupt:
        print("Comando interrompido pelo usuário.")


def execute_nmap_scan(command):
    utils.execute_command(command)
