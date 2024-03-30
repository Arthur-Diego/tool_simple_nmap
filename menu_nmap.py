from service import tcp_scanning, udp_scanning, fin_scanning, syn_scanning, icmp_scanning
from colorama import Fore, Style


def nmap_menu():
    print("Menu de Varredura Nmap:")
    print("1. Varredura TCP Connect: ", Fore.RED + "nmap -sT <target>" + Style.RESET_ALL)
    print("2. Varredura SYN Scanning: ", Fore.RED + "nmap -sS <target>" + Style.RESET_ALL)
    print("3. Varredura UDP Scanning: ", Fore.RED + "nmap -sU <target>" + Style.RESET_ALL)
    print("4. Varredura FIN Scanning: ", Fore.RED + "nmap -sF <target>" + Style.RESET_ALL)
    print("5. Varredura ICMP Scanning (Ping): ", Fore.RED + "nmap -PE <target>" + Style.RESET_ALL)

    choice = input("Escolha uma opção (1-5): ")

    if choice == '1':
        tcp_scanning.tcp_scan_menu()
    elif choice == '2':
        syn_scanning.syn_scan_menu()
    elif choice == '3':
        udp_scanning.udp_scan_menu()
    elif choice == '4':
        fin_scanning.fin_scan_menu()
    elif choice == '5':
        icmp_scanning.icmp_scan_menu()
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    try:
        nmap_menu()
    except KeyboardInterrupt:
        print("\nComando interrompido pelo usuário.")