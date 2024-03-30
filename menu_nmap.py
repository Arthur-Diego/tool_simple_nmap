from service import tcp_scanning, udp_scanning, fin_scanning, sys_scanning, icmp_scanning


def nmap_menu():
    print("Menu de Varredura Nmap:")
    print("1. Varredura TCP Scanning")
    print("2. Varredura SYN Scanning")
    print("3. Varredura UDP Scanning")
    print("4. Varredura FIN Scanning")
    print("5. Varredura ICMP Scanning")

    choice = input("Escolha uma opção (1-5): ")

    if choice == '1':
        tcp_scanning.tcp_scan_menu()
    elif choice == '2':
        sys_scanning.syn_scan_menu()
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