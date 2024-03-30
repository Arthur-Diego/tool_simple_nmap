import subprocess
from colorama import Fore, Style


def fin_scan_menu():
    print("Escolha uma opção de varredura FIN:")
    print("1. Varredura FIN em um único host:", Fore.RED + Style.BRIGHT + "nmap -sF host" + Style.RESET_ALL)
    print("2. Varredura FIN em uma faixa de IPs:", Fore.RED + Style.BRIGHT + "nmap -sF ip_range" + Style.RESET_ALL)
    print("3. Varredura FIN em várias portas específicas:", Fore.RED + Style.BRIGHT + "nmap -sF -p ports host" + Style.RESET_ALL)
    print("4. Varredura FIN em todas as portas comuns:", Fore.RED + Style.BRIGHT + "nmap -sF -p- host" + Style.RESET_ALL)
    print("5. Varredura FIN com detecção de serviços e versões:", Fore.RED + Style.BRIGHT + "nmap -sF -sV host" + Style.RESET_ALL)

    choice = input("Escolha uma opção (1-5): ")

    if choice == '1':
        print("---------------------------------")
        print("Varredura FIN em um único host:\n")
        host = input("Digite o endereço IP do host: ")
        fin_scan(host)
        print("Varredura FIN em um único host realizada.")
        print("-----------------------------------------")

    elif choice == '2':
        print("----------------------------------")
        print("Varredura FIN em uma faixa de IPs:\n")
        ip_range = input("Digite a faixa de IPs (exemplo: 192.168.1.1-100): ")
        fin_scan(ip_range)
        print("Varredura FIN em uma faixa de IPs realizada.")
        print("---------------------------------------------")

    elif choice == '3':
        print("---------------------------------------------")
        print("Varredura FIN em várias portas específicas:\n")
        host = input("Digite o endereço IP do host: ")
        ports = input("Digite as portas que deseja escanear (exemplo: 80,443): ")
        fin_scan(host, ports)
        print("Varredura FIN em várias portas específicas realizada.")
        print("-----------------------------------------------------")

    elif choice == '4':
        print("------------------------------------------")
        print("Varredura FIN em todas as portas comuns:\n")
        host = input("Digite o endereço IP do host: ")
        fin_scan(host, "-")
        print("Varredura FIN em todas as portas comuns realizada.")
        print("--------------------------------------------------")

    elif choice == '5':
        print("-------------------------------------------------")
        print("Varredura FIN com detecção de serviços e versões:\n")
        host = input("Digite o endereço IP do host: ")
        fin_scan(host, "-sV")
        print("Varredura FIN com detecção de serviços e versões realizada.")
        print("-----------------------------------------------------")

    else:
        print("Opção inválida.")


def fin_scan(target, options=""):
    command = ["nmap", "-sF", options, target]
    execute_nmap_scan(command)


def execute_nmap_scan(command):
    utils.execute_command(command)
