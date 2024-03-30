import subprocess
from colorama import Fore, Style
from output_utils import utils


NMAP = "nmap"
CONNECT_SCAN = "-sT"


def tcp_scan_menu():
    print("1. Varredura TCP Connect em um único:", Fore.RED + Style.BRIGHT + "nmap -sT host" + Style.RESET_ALL)
    print("2. Varredura TCP Connect em uma faixa de IPs:", Fore.RED + Style.BRIGHT + "nmap -sT ip_range" + Style.RESET_ALL)
    print("3. Varredura TCP Connect em várias portas específicas:", Fore.RED + Style.BRIGHT + "nmap -sT -p ports host" + Style.RESET_ALL)
    print("4. Varredura TCP Connect em todas as portas comuns:", Fore.RED + Style.BRIGHT + "nmap -sT -p- host" + Style.RESET_ALL)
    print("5. Varredura TCP Connect com detecção de serviços e versões:", Fore.RED + Style.BRIGHT + "nmap -sT -sV host"+ Style.RESET_ALL)
    choice = input("Escolha uma opção (1-5): ")

    if choice == '1':
        print("-----------------------------------")
        print("Varredura TCP Connect em um único host:\n")
        host = input("Digite o endereço IP do host: ")
        execute_nmap_tcp_connect(host=host)
        print("Varredura TCP Connect em um único host realizada.")
        print("-------------------------------------------")

    elif choice == '2':
        print("------------------------------------")
        print("Varredura TCP Connect em uma faixa de IPs:\n")
        ip_range = input("Digite a faixa de IPs (exemplo: 192.168.1.1-100): ")
        execute_nmap_tcp_connect(ip_range=ip_range)
        print("Varredura TCP Connect em uma faixa de IPs realizada.")
        print("-----------------------------------------------")

    elif choice == '3':
        print("-------------------------------------------------")
        print("Varredura TCP Connect em várias portas específicas:\n")
        host = input("Digite o endereço IP do host: ")
        ports = input("Digite as portas que deseja escanear (exemplo: 80,443): ")
        execute_nmap_tcp_connect(host=host, ports=ports)
        print("Varredura TCP Connect em várias portas específicas realizada.")
        print("---------------------------------------------------------")

    elif choice == '4':
        print("----------------------------------------------")
        print("Varredura TCP Connect em todas as portas comuns:\n")
        host = input("Digite o endereço IP do host: ")
        execute_nmap_tcp_connect(host=host, ports="-")
        print("Varredura TCP Connect em todas as portas comuns realizada.")
        print("----------------------------------------------")

    elif choice == '5':
        print("---------------------------------------------------------")
        print("Varredura TCP Connect com detecção de serviços e versões:\n")
        option = input("Escolha uma opção (1: Host único, 2: Faixa de IPs): ")

        if option == '1':
            host = input("Digite o endereço IP do host: ")
            execute_nmap_tcp_connect(host=host, detect_services=True)
        elif option == '2':
            print("Digite o endereço de ip na primeira opção e na segunda apenas o final ex: (192.168.0.1-254)")
            start_host = input("Digite o endereço IP inicial: ")
            end_host = input("Digite o endereço IP final: ")
            hosts_range = f"{start_host}-{end_host}"
            execute_nmap_tcp_connect(ip_range=hosts_range, detect_services=True)
        else:
            print("Opção inválida.")

        print("Varredura TCP Connect com detecção de serviços e versões realizada.")
        print("---------------------------------------------------------")

    else:
        print("Opção inválida")


def execute_nmap_tcp_connect(host=None, ip_range=None, ports=None, detect_services=False, hosts_range=None):
    command = [NMAP, CONNECT_SCAN, "-v", "-A"]

    if detect_services:
        command.append('-sV')

    if ports:
        command.extend(['-p', ports])

    if hosts_range:
        command.append(hosts_range)
    elif ip_range:
        command.append(ip_range)
    elif host:
        command.append(host)
    else:
        print("Erro: Deve fornecer um host ou uma faixa de IPs.")
        return

    utils.execute_command(command)



