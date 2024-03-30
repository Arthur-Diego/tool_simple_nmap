import subprocess
from output_utils import utils
from colorama import Fore, Style


def udp_scan_menu():
    print("Escolha uma opção de varredura UDP:")
    print("1. Varredura UDP em um único host:", Fore.RED + Style.BRIGHT + "nmap -sU host" + Style.RESET_ALL)
    print("2. Varredura UDP em uma faixa de IPs:", Fore.RED + Style.BRIGHT + "nmap -sU ip_range" + Style.RESET_ALL)
    print("3. Varredura UDP em várias portas específicas:", Fore.RED + Style.BRIGHT + "nmap -sU -p ports host" + Style.RESET_ALL)
    print("4. Varredura UDP em todas as portas comuns:", Fore.RED + Style.BRIGHT + "nmap -sU -p- host" + Style.RESET_ALL)
    print("5. Varredura UDP com detecção de serviços e versões:", Fore.RED + Style.BRIGHT + "nmap -sU -sV host" + Style.RESET_ALL)

    choice = input("Escolha uma opção (1-5): ")

    if choice == '1':
        print("---------------------------------")
        print("Varredura UDP em um único host:\n")
        host = input("Digite o endereço IP do host: ")
        udp_scan(host)
        print("Varredura UDP em um único host realizada.")
        print("-----------------------------------------")

    elif choice == '2':
        print("----------------------------------")
        print("Varredura UDP em uma faixa de IPs:\n")
        ip_range = input("Digite a faixa de IPs (exemplo: 192.168.1.1-100): ")
        udp_scan(ip_range)
        print("Varredura UDP em uma faixa de IPs realizada.")
        print("---------------------------------------------")

    elif choice == '3':
        print("---------------------------------------------")
        print("Varredura UDP em várias portas específicas:\n")
        host = input("Digite o endereço IP do host: ")
        ports = input("Digite as portas que deseja escanear (exemplo: 80,443): ")
        udp_scan(host, ports)
        print("Varredura UDP em várias portas específicas realizada.")
        print("-----------------------------------------------------")

    elif choice == '4':
        print("------------------------------------------")
        print("Varredura UDP em todas as portas comuns:\n")
        host = input("Digite o endereço IP do host: ")
        udp_scan(host, "-")
        print("Varredura UDP em todas as portas comuns realizada.")
        print("--------------------------------------------------")

    elif choice == '5':
        print("-------------------------------------------------")
        print("Varredura UDP com detecção de serviços e versões:\n")
        host = input("Digite o endereço IP do host: ")
        udp_scan(host, "-sV")
        print("Varredura UDP com detecção de serviços e versões realizada.")
        print("-----------------------------------------------------")

    else:
        print("Opção inválida.")


def udp_scan(target, options=""):
    command = ["nmap", "-sU", options, target]
    execute_nmap_scan(command)


def execute_nmap_scan(command):
    utils.execute_command(command)
