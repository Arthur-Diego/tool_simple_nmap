import subprocess
from colorama import Fore, Style
from output_utils import utils


NMAP = "nmap"
CONNECT_SCAN = "-sT"


def execute_nmap_tcp_connect(host=None, ip_range=None, ports=None, detect_services=False):
    command = [NMAP, CONNECT_SCAN]

    if detect_services:
        command.append('-sV')

    if ports:
        command.extend(['-p', ports])

    if ip_range:
        command.append(ip_range)
    elif host:
        command.append(host)
    else:
        print("Erro: Deve fornecer um host ou uma faixa de IPs.")
        return

    try:
        print("Comando executado: {}".format(" ".join(command)))
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)

        utils.ask_for_output(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e.output}")


def tcp_scan_menu():
    print("1. Varredura TCP Connect em um único:", Fore.RED + Style.BRIGHT + "nmap -sT host" + Style.RESET_ALL)
    print("2. Varredura TCP Connect em uma faixa de IPs:", Fore.RED + Style.BRIGHT + "nmap -sT ip_range" + Style.RESET_ALL)
    print("3. Varredura TCP Connect em várias portas específicas:", Fore.RED + Style.BRIGHT + "nmap -sT -p ports host" + Style.RESET_ALL)
    print("4. Varredura TCP Connect em todas as portas comuns:", Fore.RED + Style.BRIGHT + "nmap -sT -p- host" + Style.RESET_ALL)
    print("5. Varredura TCP Connect com detecção de serviços e versões:", Fore.RED + Style.BRIGHT + "nmap -sT -sV host"+ Style.RESET_ALL)
    choice = input("Escolha uma opção (1-5): ")

    if choice == '1':
        host = input("Digite o endereço IP do host: ")
        execute_nmap_tcp_connect(host=host)
    elif choice == '2':
        ip_range = input("Digite a faixa de IPs (exemplo: 192.168.1.1-100): ")
        execute_nmap_tcp_connect(ip_range=ip_range)
    elif choice == '3':
        host = input("Digite o endereço IP do host: ")
        ports = input("Digite as portas que deseja escanear (exemplo: 80,443): ")
        execute_nmap_tcp_connect(host=host, ports=ports)
    elif choice == '4':
        host = input("Digite o endereço IP do host: ")
        execute_nmap_tcp_connect(host=host, ports="-")
    elif choice == '5':
        host = input("Digite o endereço IP do host: ")
        execute_nmap_tcp_connect(host=host, detect_services=True)
    else:
        print("Opção inválida")
