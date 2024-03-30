import subprocess
from output_utils import utils
from colorama import Fore, Style


def syn_scan_menu():
    print("Escolha uma opção de varredura SYN:")
    print("1. Varredura SYN em um único host:", Fore.RED + Style.BRIGHT + "nmap -sS host" + Style.RESET_ALL)
    print("2. Varredura SYN em uma faixa de IPs:", Fore.RED + Style.BRIGHT + "nmap -sS ip_range" + Style.RESET_ALL)
    print("3. Varredura SYN em várias portas específicas:", Fore.RED + Style.BRIGHT + "nmap -sS -p ports host" + Style.RESET_ALL)
    print("4. Varredura SYN em todas as portas comuns:", Fore.RED + Style.BRIGHT + "nmap -sS -p- host" + Style.RESET_ALL)
    print("5. Varredura SYN com detecção de serviços e versões:", Fore.RED + Style.BRIGHT + "nmap -sS -sV host" + Style.RESET_ALL)

    choice = input("Escolha uma opção (1-5): ")

    if choice == '1':
        print("---------------------------------")
        print("Varredura SYN em um único host:\n")
        host = input("Digite o endereço IP do host: ")
        syn_scan(host)
        print("Varredura SYN em um único host realizada.")
        print("-----------------------------------------")

    elif choice == '2':
        print("----------------------------------")
        print("Varredura SYN em uma faixa de IPs:\n")
        ip_range = input("Digite a faixa de IPs (exemplo: 192.168.1.1-100): ")
        syn_scan(ip_range)
        print("Varredura SYN em uma faixa de IPs realizada.")

    elif choice == '3':
        print("---------------------------------------------")
        print("Varredura SYN em várias portas específicas:\n")
        host = input("Digite o endereço IP do host: ")
        ports = input("Digite as portas que deseja escanear (exemplo: 80,443): ")
        syn_scan(host, ports)
        print("Varredura SYN em várias portas específicas realizada.")
        print("-----------------------------------------------------")

    elif choice == '4':
        print("------------------------------------------")
        print("Varredura SYN em todas as portas comuns:\n")
        host = input("Digite o endereço IP do host: ")
        syn_scan(host, "-p-")
        print("Varredura SYN em todas as portas comuns realizada.")
        print("--------------------------------------------------")

    elif choice == '5':
        print("-------------------------------------------------")
        print("Varredura SYN com detecção de serviços e versões:\n")
        host = input("Digite o endereço IP do host: ")
        syn_scan(host, "-sV")
        print("Varredura SYN com detecção de serviços e versões realizada.")

    else:
        print("Opção inválida.")


def syn_scan(target, options=""):
    command = ["nmap", "-sS", options, target]
    execute_nmap_scan(command)


def execute_nmap_scan(command):
    utils.execute_command(command)
